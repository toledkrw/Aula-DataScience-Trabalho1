import os, sys
sys.path.append(os.getcwd())

from utils.PathUtils import PathUtils

def getFiles(path, content) -> list:
    files = []

    for item in content:
        content_path = path + "/" + item
        if(PathUtils.checkFile(content_path)):
            files.append(content_path)

    return files

def handleFileSearch(path) -> list:
    paths_content = PathUtils.listContent(path)

    files = getFiles(path, paths_content)
    files.sort()
    return files