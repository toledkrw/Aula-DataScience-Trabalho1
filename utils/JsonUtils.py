import json, os

class JsonUtils():
    
    @staticmethod
    def writeJson(data:dict, filename:str)-> None:
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
    
    def readJson(filename:str) -> dict:
        with open(filename) as json_file:
            data = json.load(json_file)
            return data