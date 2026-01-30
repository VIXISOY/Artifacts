from Private import *
import requests
import certifi
import json


base_url = "https://api.artifactsmmo.com"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}
def nice_json(response):
    return json.dumps(response, indent=2)

def get(url):
    return requests.get(base_url+url, headers=headers, verify=False).json()

def nice_get(url):
    return nice_json(get(url))

def serverStatus():
    return nice_get("/")

if __name__ == "__main__":

    print(serverStatus())