from utils.PathUtils import PathUtils

def getFolders(path, content) -> list:
    folders = []

    for item in content:
        content_path = path + "/" + item
        if(PathUtils.checkFolder(content_path)):
            folders.append(content_path)

    return folders


def handleFolderSearch(path:str) -> list:
    paths_content = PathUtils.listContent(path)

    folders = getFolders(path, paths_content)
    folders.sort()
    return folders


