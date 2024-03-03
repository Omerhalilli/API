
import requests
def charachter_search():
    resp = requests.get("https://hp-api.onrender.com/api/characters").json()
    x = input("adini daxil et:")
    for i in resp:
        if i['name'].lower()==x.lower():
            print(i['name'], i['house'])
