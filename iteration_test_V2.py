#for loop

#Define List

NumberList = [1, 2, 3, 4, 5, 6, 7]

for Item in NumberList:
    (MultipliedNumber) = Item * 7
    print(str(Item) + " x 7 = " + str(MultipliedNumber))

StartNumber = 1
while StartNumber < 10:
    print("Number is less than 10: " + str(StartNumber))
    StartNumber += 1
print("Number is equal or greater than 10: " + str(StartNumber))

while StartNumber > 1:
    print("Number is greater than 1: " + str(StartNumber) + " counting down to 5...")
    if StartNumber == 5:
        break
    StartNumber -= 1
print("Loop was broken... Number which is now saved in StartNumber Variable: " + str(StartNumber))
