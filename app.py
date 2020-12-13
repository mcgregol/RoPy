import sys
import PySimpleGUI as sg
from roku import Roku

roku = Roku('192.168.1.60')

def callback_function1():
    roku.home()


def callback_function2():
    roku.home()
    roku.down()
    roku.down()
    roku.down()
    roku.down()
    roku.down()
    roku.right()


layout = [[sg.Text('Liam\'s Roku App')],
          [sg.Button('Home'), sg.Button('Search')]]

window = sg.Window('Liam\'s Roku App', layout, margins=(600, 300))

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Home':
        callback_function1()        # call the "Callback" function
    elif event == 'Search':
        callback_function2()        # call the "Callback" function

window.close()
