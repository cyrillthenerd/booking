#.Find Animal
#.Author mozzie
#.Version 1.1

ImportAnimal = open("Animals.txt", "r", encoding="utf8")
Animal = ImportAnimal.readlines()

Challenge = "e"

for Item in Animal:
    if Challenge in Item:
        f = open(Challenge + "Animals.txt", "a+", encoding="utf8")
        f.write(Item)
        print(Item)




