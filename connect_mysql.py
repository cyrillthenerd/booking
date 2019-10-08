#Trying to connect a MySQL DB

#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","cyrill","Banane99%","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()

