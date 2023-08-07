import json

with open('person.json') as f:
    print(json.load(f))