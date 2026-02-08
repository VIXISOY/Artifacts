from Private import *
import requests
import json
import time
from datetime import datetime, timezone
from poi import poi_dict #peux pas tester sur portable, sinon c'est juste import poi et ca fonctionne 

class APIClient:
    BASE_URL = "https://api.artifactsmmo.com"
    TOKEN = token
    session = requests.Session()

    def __init__(self):
        self.base_url = self.BASE_URL
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.TOKEN}"
        }

client = APIClient()

def handle_response(response):
    if response.status_code == 200:
        if response.request.method == "POST":
            try:
                print(f'{float(response.json()["data"]["cooldown"]["remaining_seconds"])} seconds remaining [COOLDOWN]')
                return response.json()
            except json.JSONDecodeError:
                print("Error decoding JSON response")
                return None
        return response.json()
    elif response.status_code == 499:
        print(f'Action could not be made {float(response.json()["error"]["message"].split()[5])} seconds remaining [COOLDOWN]')
        return response.json()
    else:
        print(response.json())
        return None
    
def get(endpoint, params=None,Debug = 0):
    if not Debug:
        response = requests.get(client.BASE_URL+endpoint, headers=client.headers, params=params)
        return handle_response(response)
    else:
        prepared = requests.Request("GET", client.BASE_URL+endpoint, headers=client.headers, params=params).prepare()
        print(f'{prepared.method} {prepared.url}\n{prepared.headers}\n{prepared.body}')
        return handle_response(client.session.send(prepared))
        
def post(endpoint, data=None, Debug = 0):
    if not Debug:
        response = requests.post(client.BASE_URL+endpoint, headers=client.headers, json=data)
        return handle_response(response)
    else:
        prepared = requests.Request("POST", client.BASE_URL+endpoint, headers=client.headers, json=data).prepare()
        print(f'{prepared.method} {prepared.url}\n{prepared.headers}\n{prepared.body}')
        return handle_response(client.session.send(prepared))


def json_print(get_response):
    print("Response JSON:\n", json.dumps(get_response, indent=2))


def get_cooldown(end_timestamp):
    ts = datetime.fromisoformat(end_timestamp.replace("Z", "+00:00")).timestamp()
    cooldown = ts - time.time()
    return max(0,int(cooldown+1)) #floor operation

def handle_cooldown(cooldown):
    for i in range(cooldown, 0, -1):
        print(f"\rCooldown: {i}s", end="", flush=True)
        time.sleep(1)
    print()

#region Combat Simulation

def character_combat_info(character_info):
    atk_dict = {}
    atk_dict["fire"] = character_info["data"]["attack_fire"]
    atk_dict["earth"] = character_info["data"]["attack_earth"]
    atk_dict["water"] = character_info["data"]["attack_water"]
    atk_dict["air"] = character_info["data"]["attack_air"]

    res_dict = {}
    res_dict["fire"] = character_info["data"]["res_fire"]
    res_dict["earth"] = character_info["data"]["res_earth"]
    res_dict["water"] = character_info["data"]["res_water"]
    res_dict["air"] = character_info["data"]["res_air"]
    return atk_dict, res_dict

def fighter_combat_info(character_info):
    fighter_atk_dict,fighter_res_dict = character_combat_info(character_info)
    fighter_dmg_mult_dict = {}
    fighter_dmg_mult_dict["fire"] = character_info["data"]["dmg_fire"]
    fighter_dmg_mult_dict["earth"] = character_info["data"]["dmg_earth"]
    fighter_dmg_mult_dict["water"] = character_info["data"]["dmg_water"]
    fighter_dmg_mult_dict["air"] = character_info["data"]["dmg_air"]
    return fighter_atk_dict,fighter_res_dict,fighter_dmg_mult_dict

def monster_calibrated_attack(monster_atk_dict, fighter_res):
    scaled_atk = {k: monster_atk_dict[k] * (1-(fighter_res[k] / 100)) for k in monster_atk_dict}
    return scaled_atk

def fighter_calibrated_attack(fighter_atk_dict, enemy_res, fighter_dmg_mult_dict):
    scaled_atk = {k: fighter_atk_dict[k] * (1-(enemy_res[k] / 100)) for k in fighter_atk_dict}
    super_scaled_atk = {k: scaled_atk[k] * (1+(fighter_dmg_mult_dict[k] / 100)) for k in scaled_atk}
    return super_scaled_atk

def fighter_best_attack(fighter_atk_dict, critical_strike):
    best_atk = max(fighter_atk_dict, key=fighter_atk_dict.get)
    best_value = fighter_atk_dict[best_atk]
    return best_atk  , int(best_value) * (1+(critical_strike/100))

def monster_average_attack(monster_atk_dict, critical_strike):
    possible_attacks = [atk for atk in monster_atk_dict.values() if atk > 0]
    average_atk = sum(possible_attacks) / len(possible_attacks)
    return int(average_atk) * (1 + critical_strike/100)

def fight_simulation(character,enemy):
    enemy_info=get(f"/monsters/{enemy}")
    fighter_info = get(f"/characters/{character}")

    enemy_atk, enemy_res = character_combat_info(enemy_info)
    #print(f'Enemy atk: {enemy_atk}\nEnemy res: {enemy_res}')
    fighter_atk_dict,fighter_res_dict,fighter_dmg_mult_dict = fighter_combat_info(fighter_info)
    #print(f'Fighter atk: {fighter_atk_dict}\nFighter res: {fighter_res_dict}\nFighter dmg mult: {fighter_dmg_mult_dict}')

    enemy_calibrated_atk = monster_calibrated_attack(enemy_atk, fighter_res_dict)
    #print(f'Calibrated Enemy atk: {enemy_calibrated_atk}')
    fighter_calibrated_atk = fighter_calibrated_attack(fighter_atk_dict, enemy_res, fighter_dmg_mult_dict)
    #print(f'Calibrated Fighter atk: {fighter_calibrated_atk}')
    fighter_best_atk, fighter_best_value = fighter_best_attack(fighter_calibrated_atk, fighter_info["data"]["critical_strike"])
    #print(f'Best Fighter atk: {fighter_best_atk} with value {fighter_best_value}')
    enemy_average_atk = monster_average_attack(enemy_calibrated_atk, enemy_info["data"]["critical_strike"])         
    #print(f'Average Enemy atk: {enemy_average_atk}')

    fighter_round = int(1+(enemy_info["data"]["hp"] / fighter_best_value))
    enemy_round = int(1+(fighter_info["data"]["hp"] / enemy_average_atk))
    max_enemy_round = int(1+(fighter_info["data"]["max_hp"] / enemy_average_atk))
    
    #print(f'Fighter needs {fighter_round} rounds to defeat the enemy of {enemy_info["data"]["hp"]} hp')
    #print(f'Enemy needs {enemy_round} rounds to defeat the fighter of {fighter_info["data"]["hp"]} hp')
    #print(f'Enemy needs {max_enemy_round} rounds to defeat the fighter at full hp of {fighter_info["data"]["max_hp"]} hp')
    
    initiative = (enemy_info["data"]["initiative"] < fighter_info["data"]["initiative"]) #are we the 1 st one to attack.

    if (fighter_round > enemy_round):
        if( fighter_round > max_enemy_round):
            print("can't win")
            return "unwinable", 0
        print("Fighter need rest")
        return "rest", 0
    elif (fighter_round < enemy_round):
        print("Fighter is likely to win")
        HP_lost = fighter_round * enemy_average_atk
        if initiative:
            HP_lost += enemy_average_atk #we get one more attack than the enemy, so we substract one attack from the lost HP
        return "fight", HP_lost
    else:
        print("It's a tie")
        if(fighter_info["data"]["max_hp"] > fighter_info["data"]["hp"]):
            print("rest before tie fight")
            return "rest", 0
        if initiative:            
            print("Fighter wins the tie due to initiative")
            return "fight", fighter_round-1 * enemy_average_atk 
        else:            
            print("Enemy wins the tie due to initiative")
        return "unwinable", 0
    
#endregion

class Character:

    def __init__(self, name, api=APIClient()):
        self.name = name
        self.client = api
        
    def get_cooldown(self):
        cooldown_timestamp = get(f"/characters/{self.name}")["data"]["cooldown_expiration"]
        cooldown = get_cooldown(cooldown_timestamp)
        return cooldown
        
    def handle_cooldown(self):
        for i in range(self.get_cooldown(), 0, -1):
            print(f"\rCooldown: {i}s", end="", flush=True)
            time.sleep(1)
        print()

    def move(self, x, y, Debug = 0):
        handle_cooldown(self.get_cooldown())
        print("===MOVE===")
        response = post(f"/my/{self.name}/action/move",{"x": x, "y": y}, Debug=Debug)
        print(f"{self.name} is at: {x}, {y}")
        return response
        
    def move_to(self, poi, Debug = 0):
        if poi_dict[poi] != None :
            x, y = poi_dict[poi]["x"], poi_dict[poi]["y"]
        self.move(x, y, Debug=Debug)
        
    def rest(self, Debug = 0):
        print("===REST===")
        response = post(f"/my/{self.name}/action/rest", Debug=Debug)
        return response
    
    def fight(self, enemy, Debug = 0):
        print("===FIGHT===")
        self.move_to(enemy, Debug=Debug) #we move to the enemy before fighting, to be sure we are in range
        response = post(f"/my/{self.name}/action/fight", {"enemy": enemy}, Debug=Debug)
        return response
    
    def careful_fight(self, enemy, Debug = 0):
        result = fight_simulation(self.name, enemy)
        if result[0] == "fight":
            return self.fight(enemy, Debug=Debug)
        elif result[0] == "rest":
            while result[0] == "rest":
                self.rest(Debug=Debug)
                result = fight_simulation(self.name, enemy)
            return self.fight(enemy, Debug=Debug)
        else:
            return None
    
def get_server_status(Debug=0):
    return get("/", Debug=Debug)

def get_number_of_players(Debug=0):
    return get("/", Debug=Debug)["data"]["characters_online"]

def get_char_status(Debug=0):
    return get("/my/characters", Debug=Debug)

BAGAR = Character("BAGAR")

if __name__ == "__main__":

    #json_print(get_char_status(1))
    #fight_simulation("BAGAR", "chicken")

    #print("Number of Players Online:", get_number_of_players())

    #BAGAR.move_to("cow")
    #BAGAR.move_to("mountain_entrance")
    #json_print(BAGAR.fight("chicken"))
    json_print(BAGAR.careful_fight("cow"))