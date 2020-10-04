from urllib.request import * 
from urllib.parse import *
from pip._vendor import requests
import json
import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa


# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

getData = requests.get(url).json()

#print (results)

#connect database
conn = sqlite3.connect("my.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()



#Convert the json result to a dictionary
#See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

weather = data["main"]
wind = data["wind"]
degreeSym = chr(176)

print ("Temperature: %d%sF" % (weather["temp"], degreeSym ))
print ("Humidity: %d%%" % weather["humidity"])
print ("Pressure: %d" % weather["pressure"] )
cursor.execute('''INSERT INTO weather(temperature,humidity,pressure,wind) VALUES(%d,%d,%d,%d)''' % (weather["temp"],weather["humidity"],weather["pressure"],wind["speed"]))

current = data["wind"]
print ("Wind : %d" % current["speed"])

#print database
cursor.execute('SELECT * FROM weather')
for row in cursor:
    print(row['id'],row['temperature'],row['humidity'],row['pressure'],row['wind'])
    
#save and close database file
conn.commit()
cursor.close()