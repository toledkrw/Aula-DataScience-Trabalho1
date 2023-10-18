from utils.PathUtils import PathUtils

class SearchUtils():

    #Strategy pattern would be recommended, however, there is no need to implement it.
    @staticmethod
    def getFiles(path) -> list:
        content = PathUtils.listContent(path)

        files = []

        for item in content:
            content_path = path + "/" + item
            if(PathUtils.checkFile(content_path)):
                files.append(content_path)

        files.sort()
        return files
    
    @staticmethod
    def getFolders(path) -> list:
        content = PathUtils.listContent(path)
        folders = []

        for item in content:
            content_path = path + "/" + item
            if(PathUtils.checkFolder(content_path)):
                folders.append(content_path)

        folders.sort()
        return folders