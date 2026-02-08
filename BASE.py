from Reseau import *

class Character:
    def __init__(self, name, api=APIClient()):
        self.name = name
        self.client = api

    def get_cooldown(self):
        cooldown_timestamp = get(f"/characters/{self.name}")["data"]["cooldown_expiration"]
        cooldown = calculate_cooldown(cooldown_timestamp)
        return cooldown

    def move(self, x, y, Debug=0):
        handle_cooldown(self.get_cooldown())
        print("===MOVE===")
        response = post(f"/my/{self.name}/action/move", {"x": x, "y": y}, Debug=Debug)
        print(f"{self.name} is at: {x}, {y}")
        return response

    def move_to(self, poi, Debug=0):
        if poi_dict[poi] != None:
            x, y = poi_dict[poi]["x"], poi_dict[poi]["y"]
        return self.move(x, y, Debug=Debug)

    def move_to_loot(self, loot, Debug=0):
        poi = loot_dict[loot]["location"][0]  # we take the first location of the item, 
        return self.move_to(poi, Debug=Debug)

    def rest(self, Debug=0):
        handle_cooldown(self.get_cooldown())
        print("===REST===")
        response = post(f"/my/{self.name}/action/rest", Debug=Debug)
        return response

    def fight(self, enemy, Debug=0):
        self.move_to(enemy, Debug=Debug)  # we move to the enemy before fighting, to be sure we are in range
        handle_cooldown(self.get_cooldown())
        print("===FIGHT===")
        response = post(f"/my/{self.name}/action/fight", Debug=Debug)
        print(f"{self.name} fought {enemy} and {response['data']['fight']['result']}")
        return response
    
    def fight_for(self, loot, Debug=0):
        poi = loot_dict[loot]["location"][0]
        return self.fight(poi, Debug=Debug)

    def gather(self, poi, Debug=0):
        self.move_to(poi, Debug=Debug) 
        handle_cooldown(self.get_cooldown())
        print("===GATHER===")
        response = post(f"/my/{self.name}/action/gathering", Debug=Debug)
        print(f"{self.name} gathered at {poi}")
        return response

    def gather_loot(self, loot, Debug=0):
        poi = loot_dict[loot]["location"][0]
        return self.gather(poi, Debug=Debug)
    
    def craft(self, item, amount, Debug=0):
        self.move_to_loot(item, Debug=Debug)  
        handle_cooldown(self.get_cooldown())
        print("===CRAFTING===")
        response = post(f"/my/{self.name}/action/crafting",{"code": item, "quantity": amount} ,Debug=Debug)
        print(f"{self.name} crafted {amount} {item}")
        return response
        
    def bank_deposit_item(self,item, amount, Debug=0):
        self.move_to("bank", Debug=Debug)
        handle_cooldown(self.get_cooldown())
        print("===DEPOSIT_BANK===")
        response = post(f"/my/{self.name}/action/bank/deposit/item",{"code": item, "quantity": amount} ,Debug=Debug)
        print(f"{self.name} deposited {amount} {item} in the bank")
        return response

    def bank_withdraw_item(self,item, amount, Debug=0):
        self.move_to("bank", Debug=Debug)
        handle_cooldown(self.get_cooldown())
        print("===WITHDRAW_BANK===")
        response = post(f"/my/{self.name}/action/bank/withdraw/item",{"code": item, "quantity": amount} ,Debug=Debug)
        print(f"{self.name} withdrew {amount} {item} from the bank")
        return response

BAGAR = Character("BAGAR")

if __name__ == "__main__":

    #json_print(get_chars_status(1))

    #print("Number of Players Online:", get_number_of_players())

    #BAGAR.move_to("cow")
    #BAGAR.move_to("mountain_entrance")
    while True:
        BAGAR.loot("copper_rocks")