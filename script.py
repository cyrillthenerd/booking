import os
import random
from subprocess import call
from time import sleep

def screen_clear():

   _ = call('clear' if os.name =='posix' else 'cls')

print("Ready smartass? Just keep the number in your head.")
sleep(2)
screen_clear()
value = random.randrange(1000, 9999)
print(value)
sleep(2)
screen_clear()
print("Still got the number?")

def numberguessing():

   correctnumber = False
   while not correctnumber:
      number = input('Yallah: ')
      if (number) == value:
           correctnumber = True
           print( "YEAHBOOOOY" )
      else:
            print('Nope, try again')

numberguessing()