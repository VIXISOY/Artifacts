from Reseau import *

class Character:
    def __init__(self, name, api=APIClient()):
        self.name = name
        self.client = api

    def get_cooldown(self):
        cooldown_timestamp = get(f"/characters/{self.name}")["data"]["cooldown_expiration"]
        cooldown = calculate_cooldown(cooldown_timestamp)
        return cooldown

    def move(self, x, y, poi=None, Debug=0):
        handle_cooldown(self.get_cooldown())
        print("===MOVE===", end=" ")
        response = post(f"/my/{self.name}/action/move", {"x": x, "y": y}, Debug=Debug)
        print(f"{self.name} is at: {x}, {y} {poi}")
        return response

    def move_to(self, poi, Debug=0):
        if poi_dict[poi] != None:
            x, y = poi_dict[poi]["x"], poi_dict[poi]["y"]
            if (x, y) != self.get_position():
                return self.move(x, y, poi, Debug=Debug)
        else:
            print("ERROR poi name not found")

    def rest(self, Debug=0):
        handle_cooldown(self.get_cooldown())
        print("===REST===", end=" ")
        response = post(f"/my/{self.name}/action/rest", Debug=Debug)
        return response

    def fight(self, enemy, quantity=1, Debug=0):
        self.move_to(enemy, Debug=Debug)
        handle_cooldown(self.get_cooldown())
        print("===FIGHT===", end=" ")
        response = post(f"/my/{self.name}/action/fight", Debug=Debug)
        print(f"{self.name} fought {enemy} and {response['data']['fight']['result']}")
        return response

    def gather(self, poi, quantity=1, Debug=0):
        self.move_to(poi, Debug=Debug)
        handle_cooldown(self.get_cooldown())
        print("===GATHER===", end=" ")
        response = post(f"/my/{self.name}/action/gathering", Debug=Debug)
        print(f"{self.name} gathered at {poi}")
        return response

    def farm_item(self, loot, quantity=1, Debug=0):
        for i in range(quantity):
            match loot_dict[loot]["action"]:
                case "gather":
                    self.gather(loot_dict[loot]["location"],quantity, Debug=Debug)
                case "fight":
                    self.fight(loot_dict[loot]["location"],quantity, Debug=Debug)
    
    def craft(self, item, amount, Debug=0):
        self.move_to(get_item(item)["data"]["craft"]["skill"], Debug=Debug)
        handle_cooldown(self.get_cooldown())
        print("===CRAFTING===", end=" ")
        response = post(f"/my/{self.name}/action/crafting",{"code": item, "quantity": amount} ,Debug=Debug)
        print(f"{self.name} crafted {amount} {item}")
        return response
        
    def bank_deposit_item(self,item, amount, Debug=0):
        self.move_to("bank", Debug=Debug)
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_BANK===", end=" ")
        response = post(f"/my/{self.name}/action/bank/deposit/item",[{"code": item, "quantity": amount}] ,Debug=Debug)
        print(f"{self.name} deposited {amount} {item} in the bank")
        return response

    def bank_withdraw_item(self,item, amount, Debug=0):
        self.move_to("bank", Debug=Debug)
        handle_cooldown(self.get_cooldown())
        print("===WITHDRAW_BANK===", end=" ")
        response = post(f"/my/{self.name}/action/bank/withdraw/item",[{"code": item, "quantity": amount}] ,Debug=Debug)
        print(f"{self.name} withdrew {amount} {item} from the bank")
        return response

    def get_inventory(self, Debug=0):
        response = get(f"/characters/{self.name}", Debug=Debug)
        return response["data"]["inventory"]

    def print_inventory(self, Debug=0):
        print("===INVENTORY===", end=" ")
        print(f"{self.name}")
        inventory = self.get_inventory(Debug=Debug)
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

    def get_position(self, Debug=0):
        response = get(f"/characters/{self.name}", Debug=Debug)
        return response["data"]["x"], response["data"]["y"]

    def bank_deposit_full_inventory(self, Debug=0):
        self.move_to("bank", Debug=Debug)
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_FULL_INVENTORY===", end=" ")
        full = [item for item in self.get_inventory() if item["quantity"] > 0]
        response = post(f"/my/{self.name}/action/bank/deposit/item", full, Debug=Debug)
        print(full)
        print(f"{self.name} deposited full inventory in the bank")
        return response

BAGAR = Character("BAGAR")
FEMME = Character("FEMME")

if __name__ == "__main__":

    #json_print(get_chars_status(1))
    FEMME.print_inventory()
    #print(FEMME.get_position())
    FEMME.bank_deposit_full_inventory()

    #print("Number of Players Online:", get_number_of_players())
    #BAGAR.craft("copper_axe",1)
    #BAGAR.farm_item("ash_wood", Debug=0)
