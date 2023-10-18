from utils.JsonUtils import JsonUtils
import re

def deleteKey(data:dict, key:str):
    del data[key]

def removeNonNumeric(string:str) -> str:
    return re.sub(r'[^0-9.]', '', string)

def prepareMarketData(data: dict, app_id:str) -> dict:
    """
    todo: 

    """
    deleteKey(data, 'searchdata')
    deleteKey(data, 'success')
    deleteKey(data, 'start')
    deleteKey(data, 'pagesize')
    deleteKey(data, 'results')

    data["app_id"] = app_id
    data["ingestion_date"] = data.pop("timestamp")

def prepareItemData(data: dict, ingestion_date:str) -> dict:
    """
    todo: 
    """
    deleteKey(data, 'app_icon')
    deleteKey(data, 'app_name')
    
    data["name"] = data.pop("hash_name")
    data["sell_price"] = removeNonNumeric(data.pop("sell_price_text"))
    data["sale_price"] = removeNonNumeric(data.pop("sale_price_text"))

    interesting_data = data.pop("asset_description")
    
    data["app_id"] = interesting_data.pop("appid")
    data["item_type"] = interesting_data.pop("type")
    data["currency"] = interesting_data.pop("currency")
    data["tradable"] = interesting_data.pop("tradable")

    data["ingestion_date"] = ingestion_date


def handleFileRefinement(file:str) -> dict:
    current_app_id = file.split("/")[-2]
    readable_dict = JsonUtils.readJson(file)
    
    market_data = readable_dict.copy()
    prepareMarketData(market_data, current_app_id)

    ingestion_date = market_data["ingestion_date"]
    results = readable_dict.pop("results")

    cleansed_items = []
    
    for item in results:
        prepareItemData(item, ingestion_date)
        cleansed_items.append(item)
    
    del results, readable_dict

    return market_data, cleansed_items


    print("u here")
    

    




    



    
    

