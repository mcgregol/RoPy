import sys
import PySimpleGUI as sg
from roku import Roku

roku = Roku('192.168.1.60')

def go_home():
    roku.home()


def go_search():
    roku.home()
    roku.down()
    roku.down()
    roku.down()
    roku.down()
    roku.down()
    roku.right()


layout = [[sg.Text('Liam\'s Roku App')],
          [sg.Button('Home'), sg.Button('Go to Search')], 
	      [sg.Text('Search:', size =(15, 1)), sg.InputText()],
          [sg.Submit()]]

window = sg.Window('Liam\'s Roku App', layout, margins=(600, 300))

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Home':
        go_home()        # call the "Callback" function
    elif event == 'Search':
        go_search()        # call the "Callback" function
    elif event == 'Submit':
        roku.literal(values[0])

window.close()
