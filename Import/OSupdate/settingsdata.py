import json
def read(pyth):
    with open (pyth , "r") as files:
        textjson = files.read() 
        return textjson
data = ["..\\data\\Configes\\pythdata.json","..\\data\\Configes\\osa.json","..\\data\\Configes\\owa.json","..\\data\\Configes\\logs.json"]
progfiles = json.loads(read(data[0]))
OSA = json.loads(read(data[1]))
OWA = json.loads(read(data[2]))
Logs = json.loads(read(data[3]))