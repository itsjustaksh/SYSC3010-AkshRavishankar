import urllib.request
import json
from pip._vendor import requests

def readThingspeakData():
    URL = "https://api.thingspeak.com/channels/1149760/fields/1.json?api_key="
    KEY = "VULBB49PHYRFJQGH"
    HEADER = "&results=5"
    NEW_URL = URL + KEY + HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)

    getData = requests.get(NEW_URL).json()
    print(getData)
    channelID = getData['channel']['id']

    field1 = getData['feeds']
    valueList = []
    for value in field1:
        valueList.append(value['field1'])

if __name__ == '__main__':
    readThingspeakData()
    


