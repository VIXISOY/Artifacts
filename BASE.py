from Private import *
import requests
import json

class APIClient:
    BASE_URL = "https://api.artifactsmmo.com"
    TOKEN = token

    def __init__(self):
        self.base_url = self.BASE_URL
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }

client = APIClient()

def handle_response(response):
    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Error decoding JSON response")
            return None
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

def get(endpoint, params=None):
    response = requests.get(client.BASE_URL+endpoint, headers=client.headers, params=params)
    return handle_response(response)

def post(endpoint, data=None):
    response = requests.post(client.BASE_URL+endpoint, headers=client.headers, json=data)
    return handle_response(response)

def json_print(get_response):
    print("Response JSON:\n", json.dumps(get_response, indent=2))


class Character:

    def __init__(self, name, api=APIClient()):
        self.name = name
        self.client = api

    def move(self, x, y, map_id=0):
        response = post(f"/my/{self.name}/action/move",f'"x"={x},"y"={y},"map_id"={map_id}')
        return response

def get_server_status():
    return get("/")

def get_number_of_players():
    return get("/").get("data").get("characters_online")

if __name__ == "__main__":

    json_print(get_server_status())

    print("Number of Players Online:", get_number_of_players())

    Bonga = Character("Bonga")
