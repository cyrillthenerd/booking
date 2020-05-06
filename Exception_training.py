# Author: Cyrill
# Version: V0.1
# This is a training file to challenge ourselves
# Today's challenge will be to know how to to error handling.

number = 0
checker = True


def inputer():
    try:
        number = int(input('Enter your age: '))
    except:
        print('You have entered an invalid value.')
        exit()
    return number

def agecheck():
    if number >= 18:
        checker = True
    elif number <= 17:
        checker = False
    return checker

inputer()
oldenough = agecheck()
print("Are you old enough? " + str(oldenough))


