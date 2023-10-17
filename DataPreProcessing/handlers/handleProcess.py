from utils.CheckpointUtils import CheckpointUtils
from utils.JsonUtils import JsonUtils
from utils.PathUtils import PathUtils

from DataPreProcessing.handlers.handleFileEnrichment import handleFileEnrichment
from DataPreProcessing.handlers.handleFolderSearch import handleFolderSearch
from DataPreProcessing.handlers.handleFileSearch import handleFileSearch

def saveFile(file:dict, folder:str, old_file_name:str) -> None:
    current_folder = folder.split("/")[-1]
    old_file_name = old_file_name.split("/")[-1].replace(".json", "")

    trusted_path = "./DATA/TRUSTED/" + current_folder

    if(not PathUtils.checkFolder(trusted_path)):
        PathUtils.createPath(trusted_path)

    JsonUtils.writeJson(file, trusted_path + "/" + old_file_name + ".json")


def processFolder(folder:str) -> None:
    available_files_list = handleFileSearch(folder)

    checkpoint = CheckpointUtils.readCheckpoint("TRUSTED", folder)

    if(not checkpoint == ""):
        print("Found a checkpoint!")

        checkpoint_index = available_files_list.index(checkpoint) + 1
        available_files_list = available_files_list[checkpoint_index:]
    
    for file in available_files_list:
        new_file = handleFileEnrichment(file)
        saveFile(new_file, folder, old_file_name = file)
        CheckpointUtils.updateCheckPoint("TRUSTED", folder, file)
    

def handleProcess():
    try:
        path = './DATA/RAW'
        
        available_folders = handleFolderSearch(path)

        for folder in available_folders:
            processFolder(folder)
       
    except Exception as e:
        print(e)
    else:
        None
    finally:
        None