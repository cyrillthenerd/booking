from typing import Any, Union

import pymysql
from pymysql.cursors import Cursor

name = input("Write your email here:     ")

db = pymysql.connect("localhost", "cyrill", "Banane99%", "sys")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
cursor.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, %s)", name)
cursor.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")


cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchall())

#print(cursor.fetchone())
#print(cursor.fetchone())
#print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()
db.close()
