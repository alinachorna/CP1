import json with open("rand_dd.json") as file:
    data = json.load(file)
    for k,v in data.items():
        print(k,":",v)