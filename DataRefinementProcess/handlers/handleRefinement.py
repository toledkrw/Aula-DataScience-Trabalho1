import pandas as pd

from utils.CheckpointUtils import CheckpointUtils
from utils.SearchUtils import SearchUtils
from utils.PathUtils import PathUtils
from utils.JsonUtils import JsonUtils

from DataRefinementProcess.handlers.handleFileRefinement import handleFileRefinement



def saveFile(file:dict, folder:str, old_file_name:str) -> None:
    current_folder = folder.split("/")[-1]
    old_file_name = old_file_name.split("/")[-1].replace(".json", "")

    target_path = "./DATA/REFINED/" + current_folder

    if(not PathUtils.checkFolder(target_path)):
        PathUtils.createPath(target_path)

    JsonUtils.writeJson(file, target_path + "/" + old_file_name + ".json")


def processFolder(folder:str) -> None:
    available_files_list = SearchUtils.getFiles(folder)

    checkpoint = CheckpointUtils.readCheckpoint("REFINED", folder)

    if(not checkpoint == ""):
        print("Found a checkpoint!")

        checkpoint_index = available_files_list.index(checkpoint) + 1
        available_files_list = available_files_list[checkpoint_index:]
    
    for file in available_files_list:
        f_market_batch, f_item_batch = handleFileRefinement(file)

        saveFile(f_market_batch, folder + '-market_batch', old_file_name = file)
        saveFile(f_item_batch, folder + '-item_batch', old_file_name = file)
        
        CheckpointUtils.updateCheckPoint("REFINED", folder, file)


def handleRefinement() -> None:
    try:
        path = './DATA/TRUSTED'

        available_folders = SearchUtils.getFolders(path)

        for folder in available_folders:
            processFolder(folder)

    except Exception as e:
        print(e)
    else:
        pass
    finally:
        pass