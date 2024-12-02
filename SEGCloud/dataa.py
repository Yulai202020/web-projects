import json
def reader(pyth):
    with open (pyth , "r") as files:
        textjson = files.read() 
        return textjson
gbused = json.loads(reader("condata.json"))