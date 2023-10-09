import json, os

class JsonUtils():
    
    @staticmethod
    def writeJson(data, filename):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)