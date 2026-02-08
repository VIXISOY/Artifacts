from Private import *
import requests
import json
import time
from datetime import datetime, timezone
from poi import poi_dict

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

def get_server_status():
    return get("/")

def get_number_of_players():
    return get("/")["data"]["characters_online"]

if __name__ == "__main__":

    print("Number of Players Online:", get_number_of_players())