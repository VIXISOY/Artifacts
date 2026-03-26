from Source.Reseau import *

class Character:
    def __init__(self, name, api=APIClient()):
        self.name = name
        self.client = api
        self.proxy_zone = None
        char = self.get_character()
        self.layer = char["layer"]
        if char["layer"] != "overworld" :
            if char["layer"] == "underground":
                if char["y"] < -2:
                    if char["x"] < 2:
                        self.proxy_zone = "priestess"
                    else:
                        self.proxy_zone = "mine_nord"
                elif char["y"] < 7:
                    self.proxy_zone = "mine_ouest"
                elif char["y"] < 9:
                    self.proxy_zone = "lich"
            elif char["layer"] != "interior":
                if char["y"] < 13:
                    self.proxy_zone = "spider_house"

    def get_cooldown(self):
        cooldown_timestamp = get(f"/characters/{self.name}")["data"]["cooldown_expiration"]
        cooldown = calculate_cooldown(cooldown_timestamp)
        return cooldown

    #brique
    def move(self, x, y, poi=None):
        handle_cooldown(self.get_cooldown())
        print("===MOVE===", end=" ")
        response = post(f"/my/{self.name}/action/move", {"x": x, "y": y})
        print(f"{self.name} is at: {x}, {y} {poi}")
        return response

    def move_to(self, poi):
        if poi_dict[poi] != None:
            x, y = poi_dict[poi]["x"], poi_dict[poi]["y"]
            if (x, y) != self.get_position():
                if self.proxy_zone == poi_dict[poi].get("proxy", None) or (self.layer == "overworld" and "overworld" in poi_dict[poi].get("layer", None)):
                    #print("Can go directly to", poi)
                    return self.move(x, y, poi)
                else:
                    if self.proxy_zone != None :
                        if poi_dict.get(poi_dict[poi].get("proxy", "void")).get("proxy", None) == self.proxy_zone:
                            print(1)
                            self.move_to(poi_dict[poi].get("proxy"))
                        else:
                            print("Go back outside")
                            self.move_to(self.proxy_zone)
                        self.layer = self.transition()["data"]["transition"]["layer"]
                        if self.layer == "overworld":
                            self.proxy_zone = None
                        else:
                            self.proxy_zone = poi_dict[poi].get("proxy")
                        print("Is now in the zone",self.proxy_zone)
                        return self.move_to(poi)
                    else:
                        print("Want to go to",poi_dict[poi]["proxy"])
                        self.move_to(poi_dict[poi]["proxy"])
                        self.layer = self.transition()["data"]["transition"]["layer"]
                        self.proxy_zone = poi_dict[poi]["proxy"]
                        print("Is now in the zone",self.proxy_zone)
                        return self.move_to(poi)
        else:
            print("ERROR poi name not found")

    #brique
    def transition(self):
        handle_cooldown(self.get_cooldown())
        print("===TRANSITION===", end=" ")
        response = post(f"/my/{self.name}/action/transition")
        print(f"{self.name} transitioned to layer {response["data"]["transition"]["layer"]}")
        return response

    #brique
    def rest(self):
        handle_cooldown(self.get_cooldown())
        print("===REST===", end=" ")
        response = post(f"/my/{self.name}/action/rest")
        print()
        return response

    #brique
    def buy_NPC(self, code, quantity=1):
        self.move_to(loot_dict[code]["location"])
        handle_cooldown(self.get_cooldown())
        print("===BUY NPC===", end=" ")
        response = post(f"/my/{self.name}/action/npc/buy",{"code": code, "quantity": quantity})
        print(f"{self.name} traded {quantity} {code}")
        return response


    def fight(self, enemy):
        handle_cooldown(self.get_cooldown())
        print("===FIGHT===", end=" ")
        response = post(f"/my/{self.name}/action/fight")
        print(f"{self.name} -> {enemy} {response.get("data").get("fight").get("result")}", end=' ')
        print(f"Drops: {response.get("data").get("fight").get("characters", [{}])[0].get("drops")}")
        return response

    def gather(self, poi):
        handle_cooldown(self.get_cooldown())
        print("===GATHER===", end=" ")
        response = post(f"/my/{self.name}/action/gathering")
        print(f"{self.name} gathered at {poi}")
        return response
    
    def equip_best(self,enemy):
        weapons = []
        monster = get_monster(enemy)["data"]
        char = self.get_character()
        resistances = {
            "res_fire": (100 - monster["res_fire"]) / 100,
            "res_air": (100 - monster["res_air"]) / 100,
            "res_earth": (100 - monster["res_earth"]) / 100,
            "res_water": (100 - monster["res_water"]) / 100,
        }
        # equipements = []
        # slots = ["helmet_slot","body_armor_slot","leg_armor_slot","boots_slot","amulet_slot","shield_slot","ring1_slot","ring2_slot"]
        # for slot in slots:
        #     print(7)
        #     if char[slot] != "":
        #         equipements.append(get_item(char[slot]))
        # dmg_fire = 0
        # dmg_air = 0
        # dmg_earth = 0
        # dmg_water = 0
        # for equipement in equipements:
        #     effects = {effect["code"]: effect["value"] for effect in equipement["data"]["effects"]}
        #     dmg_fire += effects.get("dmg_fire",0)
        #     dmg_earth += effects.get("dmg_earth",0)
        #     dmg_water += effects.get("dmg_water",0)
        #     dmg_air += effects.get("dmg_air",0)
        dmgs = {
            "dmg_fire": (100 + char["dmg_fire"]) / 100,
            "dmg_air": (100 + char["dmg_air"]) / 100,
            "dmg_earth": (100 + char["dmg_earth"]) / 100,
            "dmg_water": (100 + char["dmg_water"]) / 100,
        }
        # print(dmgs)
        if char["weapon_slot"] != "" :
            weapons.append(get_item(char["weapon_slot"]))
        for item in self.get_inventory(char=char):
            if item["code"] != "":
                if item["quantity"] < 2 :
                    tmp = get_item(item["code"])
                    if (tmp["data"]["type"] == "weapon" and tmp["data"]["subtype"] == "" and tmp["data"]["level"] <= char["level"] ):
                        weapons.append(tmp)
        best_score = 0
        for weapon in weapons:
            score = 0
            effects = {effect["code"]: effect["value"] for effect in weapon["data"]["effects"]}
            score += effects.get("attack_earth", 0) * resistances.get("res_earth") * dmgs.get("dmg_earth", 0)
            score += effects.get("attack_water", 0) * resistances.get("res_water") * dmgs.get("dmg_water", 0)
            score += effects.get("attack_fire", 0) * resistances.get("res_fire") * dmgs.get("dmg_fire", 0)
            score += effects.get("attack_air", 0) * resistances.get("res_air") * dmgs.get("dmg_air", 0)
            score *= (1 + effects.get("critical_strike",0) / 2 / 100)
            #print(f"{weapon["data"]["code"]} score: {score}")
            if score > best_score:
                best_score = score
                best_weapon = weapon["data"]["code"]
        # print(f"Best weapon is {best_weapon}")
        if char["weapon_slot"] != best_weapon:
            self.equip(best_weapon)

    def farm_item(self, loot, quantity=1,task=False,char=None):
        if char is None:
            char = self.get_character()
        if self.inventory_space(char=char) <= 5:
            print("Inventory full !")
            if task:
                self.bank_deposit_full_inventory(char=char)
            else:
                self.bank_deposit_full_inventory([loot],char=char)

        if loot_dict[loot]["action"] == "trade" or loot_dict[loot]["action"] == "reward":
            if loot_dict[loot]["action"] == "trade":
                trader = loot_dict[loot]["location"]
                for trade in get(f'/npcs/items/{trader}')['data']:
                    if trade["code"] == loot:
                        currency = trade["currency"]
                        quantity_item = trade["buy_price"]
                        break
                if currency =="gold":
                    pass #TODO
            char = self.get_character()
            if loot_dict[loot]["action"] == "reward":
                currency = "tasks_coin"
                quantity_item = 6
                currency_amount = self.get_item_quantity(currency,char=char) + get_bank_item_quantity(currency) - 5
            else:
                currency_amount = self.get_item_quantity(currency,char=char) + get_bank_item_quantity(currency)
            currency_needed_amount = quantity_item * quantity
            while currency_amount < currency_needed_amount:
                self.farm_item(currency)
                char = self.get_character()
                currency_amount = self.get_item_quantity(currency,char=char) + get_bank_item_quantity(currency)
            if currency_needed_amount-self.get_item_quantity(currency_amount,char=char) > 0:
                self.bank_withdraw_item(currency,currency_needed_amount-self.get_item_quantity(currency,char=char))
            if loot_dict[loot]["action"] == "trade":
                self.buy_NPC(loot, quantity)
            if loot_dict[loot]["action"] == "reward":
                self.task_exchange()
            return #quit function
        
        elif loot_dict[loot]["action"] == "task":
            self.task_farm()

        elif loot_dict[loot]["action"] == "gather":
            #TODO Optimize speed here
            subtype = get_item(loot)["data"]["subtype"]
            for item in self.get_inventory(char=char):
                if item["code"] != "":
                    tmp = get_item(item["code"])
                    if len(tmp["data"]["effects"]) >= 2:
                        if tmp["data"]["effects"][1]["code"] == subtype:
                            self.equip(item["code"])

        elif loot_dict[loot]["action"] == "fight":
            self.equip_best(loot_dict[loot]["location"])
            #TODO Optimize equip best speed
        for i in range(quantity):
            char = self.get_character()
            if self.inventory_space(char=char) <= 5:
                print("Inventory full !")
                if task:
                    self.bank_deposit_full_inventory(char=char)
                else:
                    self.bank_deposit_full_inventory([loot],char=char)
            match loot_dict[loot]["action"]:
                case "gather":
                    if(poi_dict[loot_dict[loot]["location"]].get("event") != None):
                        self.event_gather(loot)
                    self.move_to(loot_dict[loot]["location"])
                    self.gather_at(loot_dict[loot]["location"])
                case "fight":
                    char = self.get_character()
                    self.heal_logic(char=char)
                    if poi_dict[loot_dict[loot]["location"]]["event"] == True:
                        self.event_fight(loot_dict[loot]["location"])
                    else:
                        self.move_to(loot_dict[loot]["location"])
                        self.fight(loot_dict[loot]["location"])

    def heal_logic(self, char=None):
        if char == None:
            char = self.get_character()
        hp_percent = char["hp"] / char["max_hp"]
        if (hp_percent <= 0.75):
            if not self.heal(char=char):
                if self.inventory_space(char=char) >= 60:
                    bank = get_bank_items()
                    if get_bank_item_quantity("minor_health_potion", bank=bank) > 30 and char["level"] > 5 and char["utility1_slot"] == "":
                        self.bank_withdraw_item("minor_health_potion", 30)
                        self.equip("minor_health_potion", quantity=30)
                    if get_bank_item_quantity("cooked_trout", bank=bank) > 50 and char["level"] > 20:
                        self.bank_withdraw_item("cooked_trout", 50)
                    elif get_bank_item_quantity("cooked_shrimp", bank=bank) > 50 and char["level"] > 10:
                        self.bank_withdraw_item("cooked_shrimp", 50)
                    elif get_bank_item_quantity("cooked_beef", bank=bank) > 50:
                        self.bank_withdraw_item("cooked_beef", 50)
        # char = self.get_character()
        # hp_percent = char["hp"] / char["max_hp"]
        if (hp_percent <= 0.5):
            self.rest()
        return None

    #brique
    def craft(self, item, amount=1):
        self.move_to(get_item(item)["data"]["craft"]["skill"])
        handle_cooldown(self.get_cooldown())
        print("===CRAFTING===", end=" ")
        response = post(f"/my/{self.name}/action/crafting", {"code": item, "quantity": amount})
        print(f"{self.name} crafted {amount} {item}")
        return response
    
    #brique    
    def bank_deposit_item(self,item, amount=1):
        self.move_to("bank")
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_BANK===", end=" ")
        response = post(f"/my/{self.name}/action/bank/deposit/item", [{"code": item, "quantity": amount}])
        print(f"{self.name} deposited {amount} {item} in the bank")
        return response

    #brique
    def bank_withdraw_item(self,item, amount=1):
        self.move_to("bank")
        handle_cooldown(self.get_cooldown())
        print("===WITHDRAW_BANK===", end=" ")
        response = post(f"/my/{self.name}/action/bank/withdraw/item", [{"code": item, "quantity": amount}])
        print(f"{self.name} withdrew {amount} {item} from the bank")
        return response

    def get_inventory(self,char=None):
        if char is None:
            response = get(f"/characters/{self.name}")
            return response["data"]["inventory"]
        else:
            return char["inventory"]

    def get_item_quantity(self, code, char=None):
        items = [item for item in self.get_inventory(char=char) if item["code"] == code]
        if len(items) == 0:
            return 0
        return items[0]["quantity"]

    def print_inventory(self):
        print("===INVENTORY===", end=" ")
        print(f"{self.name}")
        inventory = self.get_inventory()
        inventory = sorted(inventory,key=lambda x: x.get("quantity"),reverse=True)
        if inventory[0]["quantity"] != 0:
            for item in inventory[0:10]:
                if item["quantity"] > 0:
                    print(f"{item["code"]} : {item['quantity']}", end=" | ")
            print()
            if item["quantity"] > 0:
                for item in inventory[10:20]:
                    if item["quantity"] > 0:
                        print(f"{item["code"]} : {item['quantity']}", end=" | ")
                print()
        else:
            print("Inventory is empty")

    def get_position(self):
        response = get(f"/characters/{self.name}")
        return response["data"]["x"], response["data"]["y"]

    def bank_deposit_full_inventory(self, blacklist = [], consumable=False, char=None):
        if char == None:
            char = self.get_character()
        self.move_to("bank")
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_FULL_INVENTORY===", end=" ")

        full = []
        for item in self.get_inventory(char=char) :
            if (item["quantity"] > 0):
                if item["code"] in blacklist:
                    continue
                if get_item(item["code"])["data"]["type"] == "weapon"  :
                    continue
                if consumable and "cooked" in item["code"]:
                    continue
                full.append(item)
        if len(full) == 0:
            print("Inventory is empty")
        else:
            response = post(f"/my/{self.name}/action/bank/deposit/item", full)
            print(full)
            print(f"{self.name} deposited full inventory in the bank, except {blacklist}")
            return response
    
    def get_character(self):
        response = get(f"/characters/{self.name}")
        return response["data"]

    #brique    
    def use(self, item, quantity=1):
        handle_cooldown(self.get_cooldown())
        print("===USE===", end=" ")
        response = post(f"/my/{self.name}/action/use", {"code": item, "quantity": quantity})
        print(f"{self.name} used {quantity} {item}")
        return response

    #brique    
    def equip(self, item, slot=None, quantity=1):
        handle_cooldown(self.get_cooldown())
        if slot is None:
            slot = get_item(item)["data"]["type"]
            if slot == "ring" :
                slot = "ring1"
            elif slot == "utility" :
                slot = "utility1"
        print("===EQUIP===", end=" ")
        response = post(f"/my/{self.name}/action/equip", {"code": item, "slot": slot, "quantity": quantity})
        print(f"{self.name} equiped {quantity} {item} on slot {slot}")
        return response

    def auto_craft(self, code, amount=1, depth = 0, char=None, recycle = False, deposit = True, equip = False, solo = False):
        handle_cooldown(self.get_cooldown())
        print("===AUTOCRAFT===", end=" ")
        print(f"{self.name} auto craft {amount} {code}")

        if char == None:
            char = self.get_character()
        space = 50
        if solo:
            space = 90
        if self.inventory_space(char=char) < space:
            print("Not enough Inventory space < ", space)
            self.bank_deposit_full_inventory(char=char)
        
        for items in get_item(code)["data"]["craft"]["items"]:
            char = self.get_character()

            bank_items = get_bank_items()
            item_needed_quantity = items["quantity"] * amount
            bank_quantity =  get_bank_item_quantity(items["code"],bank=bank_items) 
            missing = item_needed_quantity - self.get_item_quantity(items["code"],char=char) - bank_quantity
            if solo:
                missing += bank_quantity
                
            if missing > 0:
                print(f"Missing {missing} {items['code']}")
                if loot_dict.get(items["code"]) == None:
                    self.auto_craft(items["code"],missing, depth+1, char=char, solo=solo)
                else:
                    start_inventory = self.get_item_quantity(items["code"],char=char)
                    start_bank = get_bank_item_quantity(items["code"],bank=bank_items)
                    if solo:
                        start_bank = 0
                    current = 0
                    while current < missing :
                        self.farm_item(items["code"],missing - current,char=char)
                        char = self.get_character()
                        bank_quantity =  get_bank_item_quantity(items["code"]) - start_bank
                        current = self.get_item_quantity(items["code"],char=char) - start_inventory + bank_quantity
                        if solo:
                            current -= bank_quantity
            print(f"Enough {items["code"]} in Bank and/or Inventory")
        if not solo:
            for items in get_item(code)["data"]["craft"]["items"]:
                already_have = self.get_item_quantity(items["code"])
                if already_have < (items["quantity"] * amount) :
                    self.bank_withdraw_item(items["code"], (items["quantity"] * amount) - already_have )

        self.craft(code, amount)
        if recycle:
            self.recycle(code,amount)
        elif equip:
            self.equip(code)
        elif depth == 0:
            if deposit:
                self.bank_deposit_item(code,amount)
        return None

    def auto_craft_old(self,code,ammount=1,depth=0,recycle=False,equip=False,char=None):
        handle_cooldown(self.get_cooldown())
        print("===AUTOCRAFT===", end=" ")
        print(f"{self.name} auto craft {ammount} {code}")
        if char == None:
            char = self.get_character()
        if self.inventory_space(char=char) < 50:
            print("Not enough Inventory space (<50)")
            self.bank_deposit_full_inventory(char=char)
        for items in get_item(code)["data"]["craft"]["items"]:
            char = self.get_character()
            bank = get_bank_items()
            missing = items["quantity"] * ammount - get_bank_item_quantity(items["code"],bank=bank) - self.get_item_quantity(items["code"],char=char)
            if missing > 0:
                print(f"Missing {missing} {items['code']}")
                #print(f"Estimated Time before retrieval: {int(missing * 30 / 60)}m {missing * 30 % 60}s")
                if loot_dict.get(items["code"]) == None:
                    self.auto_craft_old(items["code"],missing,depth+1,char=char)
                else:
                    start = self.get_item_quantity(items["code"],char=char)
                    start_bank = get_bank_item_quantity(items["code"],bank=bank)
                    current = 0
                    while current < missing :
                        self.farm_item(items["code"],missing - current,char=char)
                        char = self.get_character()
                        current = self.get_item_quantity(items["code"],char=char) - start + get_bank_item_quantity(items["code"]) - start_bank
            print(f"Enough {items["code"]} in Bank and/or Inventory")
        for items in get_item(code)["data"]["craft"]["items"]:
            already_have = self.get_item_quantity(items["code"])
            if already_have < (items["quantity"] * ammount) :
                self.bank_withdraw_item(items["code"], (items["quantity"] * ammount) - already_have )
        self.craft(code, ammount)
        if recycle:
            self.recycle(code,ammount)
        elif equip:
            self.equip(code)
        elif depth == 0:
            self.bank_deposit_item(code,ammount)
        return None

    def auto_craft_self_only(self,code,ammount=1):
        handle_cooldown(self.get_cooldown())
        print("===AUTOCRAFT-SELF===", end=" ")
        print(f"{self.name} auto craft {ammount} {code}")
        for items in get_item(code)["data"]["craft"]["items"]:
            missing = items["quantity"] * ammount - self.get_item_quantity(items["code"])
            if missing > 0:
                print(f"Missing {missing} {items['code']}")
                #print(f"Estimated Time before retrieval: {int(missing * 30 / 60)}m {missing * 30 % 60}s")
                if loot_dict.get(items["code"]) == None:
                    self.auto_craft_self_only(items["code"],missing)
                else:
                    start = self.get_item_quantity(items["code"])
                    current = 0
                    while current < missing :
                        self.farm_item(items["code"],missing)
                        current = self.get_item_quantity(items["code"]) - start
            print(f"Enough {items["code"]} in Inventory")
        self.craft(code, ammount)
        return None

    #brique    
    def recycle(self, code, quantity=1):
        poi = get_item(code)["data"]["craft"]["skill"]
        self.move_to(poi)
        handle_cooldown(self.get_cooldown())
        print("===RECYCLE===", end=" ")
        response = post(f"/my/{self.name}/action/recycling", {"code": code, "quantity": quantity})
        print(f"{self.name} recycled {quantity} {code}")
        return response
    
    def inventory_space(self,char=None):
        if char == None:
            char = self.get_character()
        space = char["inventory_max_items"]
        space_unique = 0
        inventory = char["inventory"]
        for item in inventory:
            space -= item["quantity"]
            if item["code"] == "":
                space_unique += 1
        if space_unique <= 3:
            return space_unique
        return space

    def heal(self,char=None):
        if char == None:
            char = self.get_character()
        print("===HEAL===", end=" ")
        for item in char["inventory"] :
            if (item["quantity"] > 0):
                if item["code"] in heal_items :
                    missing_health = char["max_hp"] - char["hp"]
                    required = math.ceil(missing_health/get_item(item["code"])["data"]["effects"][0]["value"])
                    ammount = min(item["quantity"], required)
                    self.use(item["code"],ammount)
                    return True
        print(f"No healing item")
        return False

    def get_task_type(self):
        return self.get_character()["task_type"]

    #brique
    def task_accept(self,type):
        if type == "monster":
            self.move_to("tasks_master_monster")
            handle_cooldown(self.get_cooldown())
            print("===TASK ACCEPT===", end=" ")
            response = post(f"/my/{self.name}/action/task/new")
            print()
            return response["data"]
        else:
            return #TODO task_item

    #brique
    def task_cancel(self):
        if self.get_item_quantity("tasks_coin") < 1 :
            if get_bank_item_quantity("tasks_coin") < 1:
                print("Not enough coins to cancel task")
                return None
            self.bank_withdraw_item("tasks_coin",1)
        self.move_to("tasks_master_monster")
        handle_cooldown(self.get_cooldown())
        print("===TASK CANCEL===", end=" ")
        response = post(f"/my/{self.name}/action/task/cancel")
        print()
        if response.get("data",0) != 0:
            return response["data"]

    #brique
    def task_exchange(self):
        self.move_to("tasks_master_monster")
        handle_cooldown(self.get_cooldown())
        print("===TASK EXCHANGE===", end=" ")
        response = post(f"/my/{self.name}/action/task/exchange")
        print(f"Reward: {response.get("data").get("rewards")}")
        return response["data"]
    
    #brique
    def task_complete(self,type):
        if type == "monster":
            self.move_to("tasks_master_monster")
            handle_cooldown(self.get_cooldown())
            print("===TASK COMPLETE===", end=" ")
            response = post(f"/my/{self.name}/action/task/complete")
            print()
            return response["data"]
        else:
            return #TODO task_item

    def task_farm(self):
        if self.get_task_type() == "":
            self.task_accept("monster")

        char = self.get_character()
        if get_monster(char["task"])["data"]["level"] >= 25 :
            self.task_cancel()

        print(f"===TASK FARM=== {char["task_progress"]}/{char["task_total"]} {char["task"]}")
        if self.get_task_type() == "monsters":
            quantity=char["task_total"]-char["task_progress"]
            loot=get_monster(char["task"])["data"]["drops"][0]["code"]
            while char["task_total"]-char["task_progress"] > 0 :
                self.farm_item(loot,quantity,task=True)
                char = self.get_character()
                quantity = char["task_total"] - char["task_progress"]
            self.task_complete("monster")
        else:
            return #TODO item_task

    def boss_fight(self,enemy,participant1=None,participant2=None):
        self.move_to(enemy)
        participants = []
        if participant1 != None:
            participants.append(participant1.name)
            participant1.move_to(enemy)
        if participant2 != None:
            participants.append(participant2.name)
            participant2.move_to(enemy)
        handle_cooldown(self.get_cooldown())
        if participant1 != None:
            handle_cooldown(participant1.get_cooldown())
        if participant2 != None:
            handle_cooldown(participant2.get_cooldown())
        print("===FIGHT BOSS===", end=" ")
        response = post(f"/my/{self.name}/action/fight", {"participants": participants})
        print(f"{self.name} and {participants} -> {enemy} {response.get("data").get("fight").get("result")}", end=' ')
        print(f"Drops: {response.get("data").get("fight").get("characters", [{}])[0].get("drops")}")
        return response

    def boss_farm(self,enemy,participant1=None,participant2=None,quantity=1,char=None):
        if char == None:
            char = self.get_character()
        if self.inventory_space(char=char) <= 5:
            print("Inventory full !")
            self.bank_deposit_full_inventory(char=char)
        self.equip_best(enemy)
        if participant1 != None:
            if participant1.inventory_space() <= 5:
                print("Inventory full !")
                participant1.bank_deposit_full_inventory()
            participant1.equip_best(enemy)
        if participant2 != None:
            if participant2.inventory_space() <= 5:
                print("Inventory full !")
                participant2.bank_deposit_full_inventory()
            participant2.equip_best(enemy)

        for i in range(quantity):
            self.heal_logic()
            if participant1 != None:
                participant1.heal_logic()
            if participant2 != None:
                participant2.heal_logic()
            self.boss_fight(enemy,participant1,participant2)

    def event_fight(self, enemy):
        event_code = poi_dict[enemy].get("event_code")# using get() to protect non existing keys
        location = active_event_location(event_code)
        if (location is not  None):
            self.move(location[0], location[1], enemy)
            self.fight(enemy)
        else:
            print(event_code," not active")
            return None

    def event_gather(self, code):
        event_code = poi_dict[loot_dict[code]["location"]].get("event_code")# using get() to protect non existing keys
        location = active_event_location(event_code)
        if (location is None):
            self.move(location[0], location[1], loot_dict[code]["location"])
            self.gather(code)
        else:
            print(event_code," not active")
            return None
        
if __name__ == "__main__":

    #json_print(CHILD.fight("chicken"))
    BAGAR.auto_craft("copper_pickaxe")