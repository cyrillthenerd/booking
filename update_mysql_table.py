#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost", "cyrill", "Banane99%", "sys")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO user(id_user,
   user_name)
   VALUES ('03', 'MartinTheNerd')"""
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

# disconnect from server
db.close()
