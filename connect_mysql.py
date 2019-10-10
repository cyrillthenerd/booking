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



#!/usr/bin/python3

import pymysql

variable = input("Type your desired user number like thos (01):   ")
variable1 = input("Type your desired nickname:   ")

# Open database connection
db = pymysql.connect("localhost", "cyrill", "Banane99%", "sys")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "INSERT INTO user (id_user, user_name) VALUES (?, ?)"
cursor.execute("INSERT INTO table user (%s, %s)", (variable, variable1))
try:
   # Execute the SQL command
   cursor.execute(sql, variable, variable1)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

