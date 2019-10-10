#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost", "cyrill", "Banane99%", "sys")

# prepare a cursor object using cursor() method
cursor = db.cursor()
name = str(input("Enter your name:"))

#cursor.execute("INSERT INTO user (id_user, user_name) VALUES (%s, %s)", (variable, variable1))

sql = ("INSERT INTO users (user_id, username) VALUES ('01' , 'CyrillTheNerd')")

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
