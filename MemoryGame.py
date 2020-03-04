import PySimpleGUI as sg
import random
GuessNumber = random.randrange(100,999)
GuessCount = 0
sg.theme('Dark Blue 1')  # please make your creations colorful


layout1 = [[sg.Text(GuessNumber)]]

window = sg.Window('Memory Game', layout1, no_titlebar=True, alpha_channel=.5, grab_anywhere=True)

event, log = window.Read(timeout=2000)
window.close()

layout2 = [	[sg.Text('Enter the number you just memorized')],
          	[sg.Input()],
	  		[sg.OK()]]

window = sg.Window('Memory Game', layout2)

event, Guess = window.Read()

Guess = Guess.get(0)
print (Guess)
Guess = str(Guess)
print (GuessNumber)
GuessNumber = str(GuessNumber)

while Guess != GuessNumber:
    layout4 = [[sg.Text('Wrong number BITCH. Try again!')],
               [sg.Input()],
               [sg.OK(), sg.Exit()]]
    window = sg.Window('Memory Game', layout4)
    event, Guess = window.Read()
    Guess = Guess.get(0)
    if event == "Exit":
        break
    if Guess == GuessNumber:
        break

window.close()

layout3 = [	[sg.Text('You did it Bitch!')],
	  		[sg.OK('Let me go!')]]

window = sg.Window('You won!', layout3)

event, Exit = window.Read()
