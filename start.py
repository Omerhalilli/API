import requests
from spell import spell_search
from charachter import charachter_search

while True:
    cmd = input("ne etmek isteyiriniz? Spell or charachter")
    if cmd.lower() == 'spell':
        spell_search()
    elif cmd.lower() == 'charachters':
        charachter_search()
    elif cmd.lower() == 'exit':
        break
    else:
        print('command is not found')
