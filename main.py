import argparse

from DataExtractionProcess.handlers import handleExtraction
from DataPreProcessing.handlers import handleProcess
from DataRefinementProcess.handlers import handleRefinement
from DataStoringProcess.handlers import handleStoring

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--extract", help="Search and Extract Items in market", action="store_true", required=False)

parser.add_argument("-a", "--appId", help="App ID of the game you are looking for", type=int, required=False)
parser.add_argument("-q", "--query", help="Query String: What are you looking for", type=str, required=False)


parser.add_argument("-p", "--process", help="Pre Process the data extracted", action="store_true", required=False)
parser.add_argument("-r", "--refine", help="Refine the data extracted", action="store_true", required=False)
parser.add_argument("-M", "--store", help="Store the data in a MYSQL instance on a Docker", action="store_true", required=False)

args = parser.parse_args()

extract = args.extract
process = args.process
refine = args.refine
store = args.store

app_id = str(args.appId)
query = str(args.query).replace("\"", "").replace("\'", "")


if(extract):
    handleExtraction.handleExtraction(app_id, query)

if(process):
    handleProcess.handleProcess()

if(refine):
    handleRefinement.handleRefinement()

if(store):
    handleStoring.handleStoring()