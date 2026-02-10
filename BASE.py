from Reseau import *

class Character:
    def __init__(self, name, api=APIClient()):
        self.name = name
        self.client = api

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
        return response

    def gather(self, poi):
        self.move_to(poi)
        handle_cooldown(self.get_cooldown())
        print("===GATHER===", end=" ")
        response = post(f"/my/{self.name}/action/gathering")
        print(f"{self.name} gathered at {poi}")
        return response

    def farm_item(self, loot, quantity=1):
        for i in range(quantity):
            match loot_dict[loot]["action"]:
                case "gather":
                    self.gather(loot_dict[loot]["location"])
                case "fight":
                    self.fight(loot_dict[loot]["location"])

    def craft(self, item, amount=1):
        self.move_to(get_item(item)["data"]["craft"]["skill"])
        handle_cooldown(self.get_cooldown())
        print("===CRAFTING===", end=" ")
        response = post(f"/my/{self.name}/action/crafting",{"code": item, "quantity": amount})
        print(f"{self.name} crafted {amount} {item}")
        return response
        
    def bank_deposit_item(self,item, amount):
        self.move_to("bank")
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_BANK===", end=" ")
        response = post(f"/my/{self.name}/action/bank/deposit/item",[{"code": item, "quantity": amount}])
        print(f"{self.name} deposited {amount} {item} in the bank")
        return response

    def bank_withdraw_item(self,item, amount):
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

    def bank_deposit_full_inventory(self):
        self.move_to("bank")
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_FULL_INVENTORY===", end=" ")
        full = [item for item in self.get_inventory() if item["quantity"] > 0]
        response = post(f"/my/{self.name}/action/bank/deposit/item", full)
        print(full)
        print(f"{self.name} deposited full inventory in the bank")
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
    
    def equip(self, item, slot, quantity=1):
        handle_cooldown(self.get_cooldown())
        print("===EQUIP===", end=" ")
        response = post(f"/my/{self.name}/action/equip",{"code": item, "slot": slot, "quantity": quantity})
        print(f"{self.name} equiped {quantity} {item} on slot {slot}")
        return response

BAGAR = Character("BAGAR")
FEMME = Character("FEMME")
CHILD = Character("CHILD")
CHOPA = Character("CHOPA")
KRYST = Character("KRYST")

if __name__ == "__main__":
    
    json_print(CHILD.fight("chicken",1))