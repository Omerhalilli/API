
import requests
def spell_search():
        
    res = requests.get('https://hp-api.onrender.com/api/spells').json()
    y = input("Sehiri daxil et: ")
    for d in res:
        if y.lower()==d['name'].lower():
            print(d['description'])