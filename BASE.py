from Private import *
import requests

base_url = "https://api.artifactsmmo.com"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}"
}

def request(url):
    return requests.get(base_url+url, headers=headers)

def serverStatus():
    return request("/")

if __name__ == "__main__":

    print(serverStatus().json())