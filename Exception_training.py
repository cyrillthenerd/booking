#Author: Cyrill
#Version: V0.1
#This is a training file to challenge ourselves
#Todays challenge will be to know how to to error handling.

number = input("Please enter a number:")


try:
  result = int(number + number)
  print(result)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")