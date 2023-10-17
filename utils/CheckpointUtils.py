import json, os
from utils.PathUtils import PathUtils
from utils.JsonUtils import JsonUtils

class CheckpointUtils():
    self_path = './CHECKPOINT'
    
    @staticmethod
    def readCheckpoint(layer: str, folder: str) -> str:
        path = __class__.self_path + "/" + layer + "/checkpoint.json"
        
        if(not PathUtils.checkFile(path)):
            return ""
        else:
            data = JsonUtils.readJson(path)
            for item in data:
                if item["folder"] == folder:
                    return item.get("lastFile")
            return ""
            
    @staticmethod
    def createCheckPoint(layer: str, folder: str, lastFile: str) -> None:
        path = __class__.self_path + "/" + layer + "/checkpoint.json"
        
        if(not PathUtils.checkFile(path)):
            checkpoint = [{"folder": folder, "lastFile": lastFile}]
            with open(path, 'w') as f:
                json.dump(checkpoint, f)
        else:
            with open(path, 'r') as f:
                data = json.load(f)
            data.append({"folder": folder, "lastFile": lastFile})
            with open(path, 'w') as f:
                json.dump(data, f)
    
    @staticmethod
    def updateCheckPoint(layer: str, folder: str, lastFile: str) -> None:
        path = __class__.self_path + "/" + layer + "/checkpoint.json"
        
        if(not PathUtils.checkFile(path)):
            CheckpointUtils.createCheckPoint(layer, folder, lastFile)
        else:
            with open(path, 'r') as f:
                data = json.load(f)
            for item in data:
                if item["folder"] == folder:
                    item["lastFile"] = lastFile
                    break
            else:
                data.append({"folder": folder, "lastFile": lastFile})
            with open(path, 'w') as f:
                json.dump(data, f)
