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
                print(f'{float(response.json()["data"]["cooldown"]["remaining_seconds"])} seconds [COOLDOWN]')
                return response.json()
            except json.JSONDecodeError:
                print("Error decoding JSON response")
                return None
        return response.json()
    elif response.status_code == 499:
        print(f'Action could not be made {float(response.json()["error"]["message"].split()[5])} seconds [COOLDOWN]')
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


def calculate_cooldown(end_timestamp):
    ts = datetime.fromisoformat(end_timestamp.replace("Z", "+00:00")).timestamp()
    cooldown = ts - time.time()
    return max(0,int(cooldown+1)) #floor operation

def handle_cooldown(cooldown):
    print("===COOL===")
    if cooldown != 0:
        for i in range(cooldown, 0, -1):
            print(f"\rCooldown: {i}s", end="", flush=True)
            time.sleep(1)
        print()
    else:
        print("No cooldown")

class Character:

    def __init__(self, name, api=APIClient()):
        self.name = name
        self.client = api
        
    def get_cooldown(self):
        cooldown_timestamp = get(f"/characters/{self.name}")["data"]["cooldown_expiration"]
        cooldown = calculate_cooldown(cooldown_timestamp)
        return cooldown

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
        handle_cooldown(self.get_cooldown())
        print("===REST===")
        response = post(f"/my/{self.name}/action/rest", Debug=Debug)
        return response 
    
    def fight(self, enemy, Debug = 0):
        self.move_to(enemy, Debug=Debug) #we move to the enemy before fighting, to be sure we are in range
        handle_cooldown(self.get_cooldown())
        print("===FIGHT===")
        response = post(f"/my/{self.name}/action/fight", {"enemy": enemy}, Debug=Debug)
        print(f"{self.name} fought {enemy} and {response['data']['fight']['result']}")
        return response

def get_server_status():
    return get("/")

def get_number_of_players():
    return get("/")["data"]["characters_online"]

BAGAR = Character("BAGAR")

if __name__ == "__main__":

    #json_print(get_chars_status(1))

    #print("Number of Players Online:", get_number_of_players())

    BAGAR.move_to("cow")
    BAGAR.move_to("mountain_entrance")