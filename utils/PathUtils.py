import os

class PathUtils():

    @staticmethod
    def checkPath(path: str) -> bool:
        return os.path.exists(path)
    
    @staticmethod
    def checkFile(path: str) -> bool:
        return os.path.isfile(path)
    
    @staticmethod
    def checkFolder(path:str) -> bool:
        return os.path.isdir(path)
    
    @staticmethod
    def listContent(path: str) -> list:
        return os.listdir(path)

    @staticmethod
    def createPath(path: str) -> None:
        os.makedirs(path)

    @staticmethod
    def getExecutionPath() -> str:
        return os.getcwd()


    
    
    
