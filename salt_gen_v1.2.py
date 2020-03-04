#.Salt Generator
#.Author mozzie
#.Version 1.1

import random
ImportLocation = open("Locations.txt", "r", encoding="utf8")
Location = ImportLocation.readlines()

ImportAnimal = open("Animals.txt", "r", encoding="utf8")
Animal = ImportAnimal.readlines()

Salt = "Salz"

LocationCount = len(Location)
AnimalCount = len(Animal)

def SaltRandomizer():
    LocationRandomizer = random.randrange(0,LocationCount)
    AnimalRandomizer = random.randrange(0,AnimalCount)
    return LocationRandomizer,AnimalRandomizer

SaltRandomizer()

MagicSalt = Location[(SaltRandomizer()[0])].capitalize().strip() + " " + Animal[(SaltRandomizer()[1])].strip() + " " + Salt

print("Dein magisches Salz ist: " + MagicSalt)
print("Es wird nach deinem magischen Salz gesucht...")

SaltRandomizer()

GeneratedSalt = Location[(SaltRandomizer()[0])].capitalize().strip() + " " + Animal[(SaltRandomizer()[1])].strip() + " " + Salt

SaltCount = 0

while MagicSalt != GeneratedSalt:

    SaltRandomizer()

    GeneratedSalt = Location[(SaltRandomizer()[0])].capitalize().strip() + " " + Animal[(SaltRandomizer()[1])].strip() + " " + Salt

    print(GeneratedSalt)

    SaltCount += 1

    if GeneratedSalt == MagicSalt:
        break

print("Du hast nach " + MagicSalt + " gesucht und hast nach " + str(SaltCount) + " Versuchen " + GeneratedSalt + " gefunden!")

ImportLocation.close()
ImportAnimal.close()