import os

class PathUtils():

    @staticmethod
    def checkPath(path):
        return os.path.exists(path)
    
    @staticmethod
    def createPath(path):
        os.makedirs(path)

