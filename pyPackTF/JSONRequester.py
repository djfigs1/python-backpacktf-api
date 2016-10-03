import requests, json

def requestJSON(url):
    r = requests.get(url)
    retrieved_json = r.json()
    return retrieved_json