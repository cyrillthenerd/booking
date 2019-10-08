#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","cyrill","Banane99%","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "INSERT INTO user (id_user, user_name) VALUES ('02', 'KevinTheNerd')"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

cursor.execute(sql)

# disconnect from server
db.close()