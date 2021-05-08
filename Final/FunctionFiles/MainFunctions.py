import json
from typing import cast
import regex as re
import numpy as np
from FieldScrappers import *

def analyzeJSON(path: str):
    try:
        with open(path, mode='r') as fp:
            data = json.load(fp)
    except:
        #IOError or file not found
        print("Error file not found")
        return None
    
    keys = data.keys()
    # array of dictionaries for the final zip
    dicArr = []

    for filename in data.keys():
        dic = {} 
        #Cache the text so we dont have to keep addressing the HashMap
        currentText = data[filename]
        # we will store all information inside this dic
        # findNIF searches the file with a regex and returns all
        # NIFS in the file
        nif = findNIF(currentText)
        dic["NIF"] = nif
        # get all dates on the file
        datesList = getAllDates(currentText)
        dic["FechasExpedición"] = datesList

        ####################################################
        # The code inside this section performs all operations related with
        # the prices
        (allPrices, total) = getAllPricesAndTotal(currentText)
        dic["ListaPrecios"] = allPrices
        dic["PrecioTotal"] = total
    
        dicArr.append(dic)
    

    return zip(data.keys(), dicArr)


if __name__ == "__main__":
    provisionalDic = analyzeJSON("./TrabajoPython2021/dict_wB.json")

    for key in provisionalDic.keys():
        print(f"{key}: {provisionalDic[key]}")
