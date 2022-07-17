from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
import data
import symbolData
import random

app = Flask(__name__)
api = Api(app)

@app.route('/api', methods=['GET'])
def api():
    args = request.args
    country = args.get("country", default="All", type=str)
    exchange = args.get("exchange", default="ALL", type=str)
    sector = args.get("sector", default="ALL", type=str)
        
    return validateGetRequest(country.title(), exchange.upper(), sector.title())
        
def validateGetRequest(country, exchange, sector):
    '''
    country: str: country of the company
    exchange: str: exchange of the company
    sector: str: sector of the company
    
    validates the request and if it passes calls filesToSearch() to get files to search.
    '''
    validSectors = []
    validExchanges = []    
    validCountries = ["All", "Us", "Canada", "Australia", "Egypt", "South Africa", "Sweden", "Turkey"]

    
    if country not in validCountries:
        abort(404, error_message='Incorrect exchange for the given country')

    for exch in data.countryObject[(country)]:
        validExchanges.append(exch)
    if exchange not in validExchanges:
        abort(404, error_message='Incorrect exchange for the given country')

    for sec in data.countryObject[country][exchange]:
        validSectors.append(sec)
    if sector not in validSectors:
        abort(404, error_message='Incorrect secotr for the given exchange and country')    
        

    return filesToSearch(country, exchange, sector)

def filesToSearch(country, exchange, sector):
    '''
    country: str: country of the company
    exchange: str: exchange of the company
    sector: str: sector of the company
    
    return the files to search based on exchange, country and sector
    '''    
    # files to search
    files = {"Us":["nasdaq","nyse", "amex"], "Canada":["tsx","tsxv", "cse", "neo"], "Australia": ["asx"], "Egypt": ["egx"], "Sweden": ["six"], "South Africa": ["jse"], "Turkey": ["bist"],};    
    fileSearch = [];
    if (country == "ALL" and exchange == "ALL"):
        fileSearch.append("nasdaq","nyse", "amex", "tsx","tsxv", "cse", "neo", "asx", "six", "egx")
    elif (country != "ALL" and exchange == "ALL"):
        fileSearch = files[country];
    else:
        fileSearch.append(exchange.lower());        
        
    # sectors to search
    sectorSearch = []
    if (sector == "All"): sectorSearch = data.USsector + data.allCad;
    else: sectorSearch.append(sector)
    
    return getRandomData(fileSearch, sectorSearch)
    
def getRandomData(fileSearch, sectorSearch):
    '''
    fileSearch: list: list of files to search
    sectorSearch: list: list of sector to search
    
    gets the data from files to search and validates it based on sector
    '''
    
    filesData = {"nasdaq": symbolData.nasdaq,"nyse": symbolData.nyse,"amex": symbolData.amex,"tsx": symbolData.tsx,"tsxv": symbolData.tsxv,"cse": symbolData.cse,"neo": symbolData.neo,"asx": symbolData.asx,"six": symbolData.six,"jse": symbolData.jse,"egx": symbolData.egx,"bist": symbolData.bist}
    total = 0
    fileSizes = []
    validData = []   
    for file in fileSearch:
        exchangeData = filesData[file]    
        for data in exchangeData:
            if data["Sector"] in sectorSearch:
                data["exchange"] = file
                validData.append(data)
           
        total += len(exchangeData)
        fileSizes . append(len(exchangeData))
        
    if total == 0: abort(404, error_message='Invalid query')    
                
    num = random.randint(0, len(validData))
    
    #randomExchangeFound = ""
    #for number, size in enumerate(fileSizes):
        #print(size, num, number)
        #if size > num:
            #randomExchangeFound = fileSearch[number]
        #else:
            #num = num - size
    
    

    return validData[num]
    
if __name__ == "__main__":
    app.run(debug=True)