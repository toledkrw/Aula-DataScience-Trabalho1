def handleSearch(app_id, query):
    if(app_id == None):
        raise Exception("App ID is None")
    else:
        try:
            from datetime import datetime
            from market import search
            from utils.JsonUtils import JsonUtils
            from utils.PathUtils import PathUtils

            data = search.search_market_items(app_id, query)
            
            if(data == None):
                raise Exception("Data is empty!")
            else:
                path = "../DATA/RAW/" + str(app_id) 

                file_name = str(datetime.now())
                file_name = file_name.replace(" ", "_").replace(".",":").replace(":","-") + ".json" 

                if(not PathUtils.checkPath(path)):
                    PathUtils.createPath(path)
                    
                JsonUtils.writeJson(data, path + "/" + file_name)

        except Exception as e:
            print(e)
        else:
            print("Search was concluded successfully and stored!") 
        finally:
            exit()
