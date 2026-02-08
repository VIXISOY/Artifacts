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
        self.move(x, y, Debug=Debug)

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

    def gather(self, item, Debug=0):
        self.move_to(item, Debug=Debug)  # we move to the location before gathering, to be sure we are in range
        handle_cooldown(self.get_cooldown())
        print("===GATHER===")
        response = post(f"/my/{self.name}/action/gathering", Debug=Debug)
        print(f"{self.name} gathered {item}")
        return response

BAGAR = Character("BAGAR")

if __name__ == "__main__":

    #json_print(get_chars_status(1))

    #print("Number of Players Online:", get_number_of_players())

    #BAGAR.move_to("cow")
    #BAGAR.move_to("mountain_entrance")
    BAGAR.gather("ash_tree")