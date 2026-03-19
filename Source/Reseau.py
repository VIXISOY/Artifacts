from Source.Private import *
import requests
import json
import time
from datetime import datetime, timezone
from Source.poi import poi_dict
from Source.loot import loot_dict
from Source.heal_items import heal_items
import math

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
                print(f'{float(response.json()["data"]["cooldown"]["remaining_seconds"])} seconds [COOLDOWN]', end=' | ')
                return response.json()
            except json.JSONDecodeError:
                print("Error decoding JSON response")
                return None
        return response.json()
    elif response.status_code == 499:
        print(f'Action could not be made {float(response.json()["error"]["message"].split()[5])} seconds [COOLDOWN]')
        return response.json()
    else:
        try:
            print(response.json())
            return None
        except ValueError:
            print("Error decoding JSON response")
            return None
    
def get(endpoint, params=None, delay=30):
    for attempt in range(10):
        try:
            response = requests.get(client.BASE_URL+endpoint, headers=client.headers, params=params)
        except (requests.exceptions.ConnectionError,requests.exceptions.Timeout,requests.exceptions.RequestException) as e:
            print(f"Connection Error, retrying in {delay} seconds")
            time.sleep(delay)
            delay += 30
            continue
        else:
            return handle_response(response)
        
def post(endpoint, data=None, delay=30):
    for attempt in range(10):
        try:
            response = requests.post(client.BASE_URL+endpoint, headers=client.headers, json=data)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout,requests.exceptions.RequestException) as e:
            print(f"Connection Error, retrying in {delay} seconds")
            time.sleep(delay)
            delay += 30
            continue
        else:
            return handle_response(response)

def json_print(get_response):
    print("Response JSON:\n", json.dumps(get_response, indent=2))

def calculate_cooldown(end_timestamp):
    ts = datetime.fromisoformat(end_timestamp.replace("Z", "+00:00")).timestamp()
    cooldown = ts - time.time()
    return max(0,int(cooldown+1)) #floor operation

def handle_cooldown(cooldown):
    if cooldown != 0:
        time.sleep(cooldown)
        #for i in range(cooldown, 0, -1):
        #    print(f"\r===COOL=== Cooldown: {i-1}s", end="", flush=True)
        #    time.sleep(1)
        #print()seconds [COOLDOWN]

def get_server_status():
    return get("/")

def get_number_of_players():
    return get("/")["data"]["characters_online"]

def get_item(code):
    return get(f"/items/{code}")

def get_bank_items(code=None):
    if code == None:
        resp = get(f"/my/bank/items", params={"size": 100})
        bank = resp["data"]
        page = 1
        while resp["page"] < resp["pages"]:
            page +=1
            resp = get(f"/my/bank/items", params={"page": page,"size": 100})
            bank += resp["data"]
        bank_total = {item["code"]: item["quantity"] for item in bank}
        return bank_total
    else:
        return get(f"/my/bank/items", params={"item_code": code})

def get_bank_item_quantity(code, bank=None):
    if bank == None:
        bank = get_bank_items()
    return bank.get(code,0)

def get_monster(code):
    return get(f"/monsters/{code}")

if __name__ == "__main__":

    print("Number of Players Online:", get_number_of_players())