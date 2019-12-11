# Trying to pull data via python from mysql and store values in a variable

import pymysql
#Connect the DB

db = pymysql.connect("localhost", "cyrill", "Banane99%", "sys")

#-----------------------------------------

#User input section

name = str(input("Enter your name:     "))
userlastname = str(input("Enter your lastname:     "))

#-----------------------------------------

#DB Commands
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS testing (username TEXT, lastname text)")
insert = ("INSERT INTO testing (username, lastname) VALUES (%s, %s)")

cursor.execute(insert, (name, userlastname))

db.commit()

cursor.execute("SELECT * FROM testing")
print(cursor.fetchall())

for username, lastname in str(cursor.execute("SELECT * FROM testing")):
    print(username)
    print(lastname)

cursor.close()

db.close()

def exitcode():
    answer = input("Do you want to exit the tool? (y/n)")
    if answer == "y":
        print("The program has officially ended")
    elif answer == "n":
        print("Too bad...we are very tired and close the tool anyway :-P")
    else:
        print("Wrong input Motherfucker!")

print("-" * 150)

exitcode()

#End of Tool





