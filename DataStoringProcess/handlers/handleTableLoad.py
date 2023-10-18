import pandas as pd
from pandas import DataFrame

from utils.JsonUtils import JsonUtils

from DataStoringProcess.handlers.handleSaveTable import handleSaveTable


def readItem(path:str) -> DataFrame:
    df = pd.read_json(path)
    return df

def readMarket(path:str) -> DataFrame:
    market_dict = JsonUtils.readJson(path)
    df = pd.DataFrame(market_dict, index=[0])
    return df


def whatTable(file_path:str) -> str:
    folder = file_path.split('/')[-2]
    table = folder.split("-")[-1]
    
    if(table == "market_batch"):
        return "f_market"
    if(table == "item_batch"):
        return "f_item"
    else:
        return None

def getDataframe(table, file_path:str) -> DataFrame:
    if(table == "f_market"):
        return readMarket(file_path)
    if(table == "f_item"):
        return readItem(file_path)


def handleTableLoad(file_path:str) -> None:
    table = whatTable(file_path)

    df = getDataframe(table, file_path)

    if(df is None):
        raise Exception("Table not found")

    handleSaveTable(df, table)
