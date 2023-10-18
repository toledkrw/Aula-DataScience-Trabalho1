from utils.SearchUtils import SearchUtils
from utils.CheckpointUtils import CheckpointUtils

from DataStoringProcess.handlers.handleTableLoad import handleTableLoad

def processFolder(folder:str) -> None:
    available_files_list = SearchUtils.getFiles(folder)

    checkpoint = CheckpointUtils.readCheckpoint("BATCH", folder)

    if(not checkpoint == ""):
        print("Found a checkpoint!")

        checkpoint_index = available_files_list.index(checkpoint) + 1
        available_files_list = available_files_list[checkpoint_index:]
        
    for file in available_files_list:
        handleTableLoad(file)
        CheckpointUtils.updateCheckPoint("BATCH", folder, file)

def handleStoring():
    try:
        path = './DATA/REFINED'

        available_folders = SearchUtils.getFolders(path)

        for folder in available_folders:
            processFolder(folder)
    
    except Exception as e:
        raise e
    else:
        pass
    finally:
        pass