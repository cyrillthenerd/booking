#.Find Keyword
#.Author cyrillthenerd
#.Version 1.0
import os.path

import os

import a as a

arr = os.listdir()
for Item in arr:
        f = open("Files.txt", "a+", encoding="utf8")
        f.write(Item + '\n')
        print(Item)
        f.close()

#ImportHack = open("MalwareBytes.org.txt", "r", encoding="utf8")
#Hack = ImportHack.readlines()

Challenge = ".ch:"
#print (os.listdir('.'))

#os.listdir('.') = f.open("Files.txt", "a+", encoding="utf8")

#def ItemCheck():
#    for Item in f:
#        if Challenge in Item:
#            f = open(Challenge + "Hack.txt", "a+", encoding="utf8")
#            f.write(Item)
#            print(Item)

#for fname in os.listdir('.'):
# print (os.listdir('.'))

for fname in os.listdir('.'):
    print (os.listdir('.'))
    if os.path.isfile(fname):
        f = open(fname, encoding="utf8")
        f = f.readlines()
        for f in os.path.isfile(fname):
            for Item in f:
                if Challenge in Item:
                    f = open(Challenge + "Hack.txt", "a+", encoding="utf8")
                    f.write(Item)
                    print(Item)
                    f.close()

