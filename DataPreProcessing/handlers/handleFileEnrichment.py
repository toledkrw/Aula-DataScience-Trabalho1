from utils.JsonUtils import JsonUtils

def addTimestamp(file:str) -> dict:
    readable_dict = JsonUtils.readJson(file)
    
    file_name_split = file.split("_")
    file_date = file_name_split[0].split("/")[-1].replace("-", "/")
    file_date_time = file_name_split[1].replace("-", ":").replace(".json", "")

    file_timestamp =  file_date + " " + file_date_time

    readable_dict["timestamp"] = file_timestamp
    
    return readable_dict


def handleFileEnrichment(file:str) -> dict:
    return addTimestamp(file)
