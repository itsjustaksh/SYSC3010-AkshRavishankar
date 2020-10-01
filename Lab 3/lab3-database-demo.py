import sqlite3
#parameter definition
id = 0
sensor = ""
zone = ""
#connect to database file
conn = sqlite3.connect("my.db")

#set up access point 
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

#create new table
#cursor.execute('create table security(id INTEGER PRIMARY KEY, sensor TEXT, zone TEXT)')

#populate table
cursor.execute('''insert into security values (?,?,?)''',(id, "door", "kitchen"))
id += 1
cursor.execute('''insert into security values (?,?,?)''',(id, "temperature", "kitchen"))
id += 1 
cursor.execute('''insert into security values (?,?,?)''',(id, "door", "garage"))
id += 1
cursor.execute('''insert into security values (?,?,?)''',(id, "temperature", "garage"))
id += 1
cursor.execute('''insert into security values (?,?,?)''',(id, "motion", "garage"))
#print data
cursor.execute('SELECT * FROM security')
for row in cursor:
    print(row['id'],row['sensor'],row['zone'])
#close connection
conn.close()




