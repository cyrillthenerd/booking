#Author: Cyrill
#Version: V0.1
#This is a training file to challenge ourselves
#Todays challenge will be to know how to to error handling.

number = input("Please enter your age:")


try:
  number >= 18
  print("Welcome to our website!")
  number < 18
  print("Sorry but you are not allowed to enter this website!")
except:
  print("This is not a valid age you entered")

print(number + " is the age you provided us with")
