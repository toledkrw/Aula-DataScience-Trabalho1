import argparse

from handlers import handleSearch

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--search", help="Search Items in market", action="store_true", required=False)
parser.add_argument("-a", "--appId", help="App ID of the game you are looking for", type=int, required=False)
parser.add_argument("-q", "--query", help="Query String: What are you looking for", type=str, required=False)

args = parser.parse_args()

search = args.search

app_id = str(args.appId)
query = str(args.query).replace("\"", "").replace("\'", "")

if(search):
    handleSearch.handleSearch(app_id, query)
