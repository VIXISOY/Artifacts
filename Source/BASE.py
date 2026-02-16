from Source.Reseau import *

class Character:
    def __init__(self, name, api=APIClient()):
        self.name = name
        self.client = api
        self.fighting_smart = False

    def get_cooldown(self):
        cooldown_timestamp = get(f"/characters/{self.name}")["data"]["cooldown_expiration"]
        cooldown = calculate_cooldown(cooldown_timestamp)
        return cooldown

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
                return self.move(x, y, poi)
        else:
            print("ERROR poi name not found")

    def rest(self):
        handle_cooldown(self.get_cooldown())
        print("===REST===", end=" ")
        response = post(f"/my/{self.name}/action/rest")
        return response

    def fight(self, enemy):
        self.move_to(enemy)
        handle_cooldown(self.get_cooldown())
        print("===FIGHT===", end=" ")
        response = post(f"/my/{self.name}/action/fight")
        print(f"{self.name} fought {enemy} and {response['data']['fight']['result']}")
        print(f"Drops: {response['data']['fight']['characters'][0]['drops']}")
        return response
    
    def fight_smart(self, loot, eating_item = "cooked_gudgeon", potion_item = "small_health_potion"):
        info = self.get_character()

        potion_quantity = 30
        potion_amount =  info["utility1_slot_quantity"] if info["utility1_slot"]==potion_item else 0
        potion_amount += info["utility2_slot_quantity"] if info["utility2_slot"]==potion_item else 0
        
        eating_quantity = 10
        eating_amount = self.get_item_quantity(eating_item)
        eating_heal_amount = get(f'/items/{eating_item}')["data"]["effects"][0]["value"]

        if potion_amount < 10 and get_bank_item_quantity(potion_item) > potion_quantity:
            self.bank_withdraw_item(potion_item, potion_quantity)
            self.equip(potion_item, quantity=potion_quantity)

        if eating_amount == 0 and get_bank_item_quantity(eating_item) > 0:
            self.bank_withdraw_item(eating_item, eating_quantity)


        missing_health = info["max_hp"]-info["hp"]
        self.use(eating_item,min((missing_health+(eating_heal_amount/3))//eating_heal_amount, eating_quantity))
        self.rest()
        self.fight(loot_dict[loot]["location"])

    def gather(self, poi):
        self.move_to(poi)
        handle_cooldown(self.get_cooldown())
        print("===GATHER===", end=" ")
        response = post(f"/my/{self.name}/action/gathering")
        print(f"{self.name} gathered at {poi}")
        return response

    def farm_item(self, loot, quantity=1):
        subtype = get_item(loot)["data"]["subtype"]
        if self.inventory_space() == 0:
            self.bank_deposit_full_inventory([loot])
        if loot_dict[loot]["action"] == "fight":
            #print(f"Want to fight {loot_dict[loot]["location"]}")
            weapons = []
            monster = get_monster(loot_dict[loot]["location"])["data"]
            resistances = {
                "res_fire": (100-monster["res_fire"])/100,
                "res_air": (100-monster["res_air"])/100,
                "res_earth": (100-monster["res_earth"])/100,
                "res_water": (100-monster["res_water"])/100,
            }
            for item in self.get_inventory():
                if item["code"] != "":
                    tmp = get_item(item["code"])
                    if (tmp["data"]["type"] == "weapon" and tmp["data"]["subtype"] == ""):
                        weapons.append(tmp)
            weapons.append(get_item(self.get_character()["weapon_slot"]))
            best_score = 0
            for weapon in weapons:
                score = 0
                effects = {effect["code"]: effect["value"] for effect in weapon["data"]["effects"]}
                score += effects.get("attack_earth",0)*resistances.get("res_earth")
                score += effects.get("attack_water", 0) * resistances.get("res_water")
                score += effects.get("attack_fire", 0) * resistances.get("res_fire")
                score += effects.get("attack_air", 0) * resistances.get("res_air")
                score *= (1+effects.get("critical_strike")/100)
                #print(f"{weapon["data"]["code"]} score: {score}", end= " ")
                if score > best_score :
                    best_score = score
                    best_weapon = weapon["data"]["code"]
            #print(f"Best weapon is {best_weapon}")
            if self.get_character()["weapon_slot"] != best_weapon:
                self.equip(best_weapon)
        else:
            for item in self.get_inventory():
                if item["code"] != "":
                    tmp = get_item(item["code"])
                    if len(tmp["data"]["effects"]) >= 2:
                        if tmp["data"]["effects"][1]["code"] == subtype:
                            self.equip(item["code"])
        for i in range(quantity):
            match loot_dict[loot]["action"]:
                case "gather":
                    self.gather(loot_dict[loot]["location"])
                case "fight":
                    if self.fighting_smart == False :
                        if (self.get_character()["hp"]/self.get_character()["max_hp"]<= 0.75):
                            if not self.heal():
                                self.bank_withdraw_item("cooked_shrimp",50)
                        if (self.get_character()["hp"]/self.get_character()["max_hp"]<= 0.5):
                            self.rest()
                        self.fight(loot_dict[loot]["location"])
                    else:
                        self.fight_smart(loot)

    def craft(self, item, amount=1):
        self.move_to(get_item(item)["data"]["craft"]["skill"])
        handle_cooldown(self.get_cooldown())
        print("===CRAFTING===", end=" ")
        response = post(f"/my/{self.name}/action/crafting",{"code": item, "quantity": amount})
        print(f"{self.name} crafted {amount} {item}")
        return response
        
    def bank_deposit_item(self,item, amount=1):
        self.move_to("bank")
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_BANK===", end=" ")
        response = post(f"/my/{self.name}/action/bank/deposit/item",[{"code": item, "quantity": amount}])
        print(f"{self.name} deposited {amount} {item} in the bank")
        return response

    def bank_withdraw_item(self,item, amount=1):
        self.move_to("bank")
        handle_cooldown(self.get_cooldown())
        print("===WITHDRAW_BANK===", end=" ")
        response = post(f"/my/{self.name}/action/bank/withdraw/item",[{"code": item, "quantity": amount}])
        print(f"{self.name} withdrew {amount} {item} from the bank")
        return response

    def get_inventory(self):
        response = get(f"/characters/{self.name}")
        return response["data"]["inventory"]

    def get_item_quantity(self, code):
        items = [item for item in self.get_inventory() if item["code"] == code]
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

    def bank_deposit_full_inventory(self, blacklist = []):
        self.move_to("bank")
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_FULL_INVENTORY===", end=" ")
        full = []
        for item in self.get_inventory() :
            if (item["quantity"] > 0):
                if get_item(item["code"])["data"]["type"] == "weapon" or get_item(item["code"])["data"]["type"] == "consumable":
                    continue
                if item["code"] in blacklist:
                    continue
                full.append(item)
        if len(full) == 0:
            print("Inventory is empty")
        else:
            response = post(f"/my/{self.name}/action/bank/deposit/item", full)
            print(full)
            print(f"{self.name} deposited full inventory in the bank, except blacklist")
            return response
    
    def get_character(self):
        response = get(f"/characters/{self.name}")
        return response["data"]
    
    def use(self, item, quantity=1):
        handle_cooldown(self.get_cooldown())
        print("===USE===", end=" ")
        response = post(f"/my/{self.name}/action/use",{"code": item, "quantity": quantity})
        print(f"{self.name} used {quantity} {item}")
        return response
    
    def equip(self, item, slot=None, quantity=1):
        handle_cooldown(self.get_cooldown())
        if slot is None:
            slot = get_item(item)["data"]["type"]
            if slot == "ring" :
                slot = "ring1"
            elif slot == "utility" :
                slot = "utility1"
        print("===EQUIP===", end=" ")
        response = post(f"/my/{self.name}/action/equip",{"code": item, "slot": slot, "quantity": quantity})
        print(f"{self.name} equiped {quantity} {item} on slot {slot}")
        return response

    def auto_craft(self,code,ammount=1):
        handle_cooldown(self.get_cooldown())
        print("===AUTOCRAFT===", end=" ")
        print(f"{self.name} auto craft {ammount} {code}")
        for items in get_item(code)["data"]["craft"]["items"]:
            missing = items["quantity"] * ammount - get_bank_item_quantity(items["code"]) - self.get_item_quantity(items["code"])
            if missing > 0:
                print(f"Missing {missing} {items['code']}")
                print(f"Estimated Time before retrieval: {int(missing * 30 / 60)}m {missing * 30 % 60}s")
                if loot_dict.get(items["code"]) == None:
                    self.auto_craft(items["code"],missing)
                else:
                    start = self.get_item_quantity(items["code"])
                    current = self.get_item_quantity(items["code"])
                    while current - start < missing :
                        self.farm_item(items["code"],missing)
            print(f"Enough {items["code"]} in Bank and/or Inventory")
        self.bank_deposit_full_inventory()
        for items in get_item(code)["data"]["craft"]["items"]:
                self.bank_withdraw_item(items["code"], items["quantity"] * ammount)
        self.craft(code, ammount)
        self.bank_deposit_full_inventory()
        return None

    def auto_craft_self_only(self,code,ammount=1):
        handle_cooldown(self.get_cooldown())
        print("===AUTOCRAFT-SELF===", end=" ")
        print(f"{self.name} auto craft {ammount} {code}")
        for items in get_item(code)["data"]["craft"]["items"]:
            missing = items["quantity"] * ammount - self.get_item_quantity(items["code"])
            if missing > 0:
                print(f"Missing {missing} {items['code']}")
                print(f"Estimated Time before retrieval: {int(missing * 30 / 60)}m {missing * 30 % 60}s")
                if loot_dict.get(items["code"]) == None:
                    self.auto_craft_self_only(items["code"],missing)
                else:
                    start = self.get_item_quantity(items["code"])
                    while self.get_item_quantity(items["code"])-start < missing :
                        self.farm_item(items["code"],missing)
            print(f"Enough {items["code"]} in Inventory")
        self.craft(code, ammount)
        return None
    
    def recycle(self, code, quantity=1):
        poi = get_item(code)["data"]["craft"]["skill"] # /!\ no security
        self.move_to(poi)
        handle_cooldown(self.get_cooldown())
        print("===RECYCLE===", end=" ")
        response = post(f"/my/{self.name}/action/recycling",{"code": code, "quantity": quantity})
        print(f"{self.name} recycled {quantity} {code}")
        return response
    
    def inventory_space(self):
        space = self.get_character()["inventory_max_items"]
        inventory = self.get_inventory()
        for item in inventory:
            space -= item["quantity"]
        return space

    def heal(self):
        handle_cooldown(self.get_cooldown())
        print("===HEAL===", end=" ")
        for item in self.get_inventory() :
            if (item["quantity"] > 0):
                if get_item(item["code"])["data"]["type"] == "consumable":
                    char = self.get_character()
                    missing_health = char["max_hp"] - char["hp"]
                    required = math.ceil(missing_health/get_item(item["code"])["data"]["effects"][0]["value"])
                    ammount = min(item["quantity"], required)
                    print()
                    self.use(item["code"],ammount)
                    return True
        print(f"No healing item")
        return False


BAGAR = Character("BAGAR")
FEMME = Character("FEMME")
CHILD = Character("CHILD")
CHOPA = Character("CHOPA")
KRYST = Character("KRYST")

if __name__ == "__main__":

    #json_print(CHILD.fight("chicken"))
    BAGAR.auto_craft("copper_pickaxe")