import sys
import PySimpleGUI as sg
from roku import Roku

roku = Roku('192.168.1.60')

sling = roku['Sling TV']
netflix = roku['Netflix']
cbs = roku['CBS News']
amazon = roku['Prime Video']
motortrend = roku['MotorTrend - Stream Car Shows']
hgtv = roku['HGTV GO']
nbc = roku['NBC News']

layout = [[sg.Text('Liam\'s Roku App')],
          [sg.Button('Home'), sg.Button('Go to Search'), sg.Button('Back'), sg.Button('OK'), sg.Button('Settings')], 
	      [sg.Text('Send Text:', size=(7, 1)), sg.InputText(), sg.Submit(), sg.Button('Backspace')],
          [sg.Button('Up')], 
          [sg.Button('Left'), sg.Button('Right')],
          [sg.Button('Down')],
          [sg.Text('Apps:')],
          [sg.Button('Sling'), sg.Button('Amazon'), sg.Button('CBS News'), sg.Button('Netflix'), sg.Button('MotorTrend')],
          [sg.Button('HGTV'), sg.Button('NBC News')],
          ]

window = sg.Window('Liam\'s Roku App', layout, margins=(100, 70))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Home':
        roku.home()
    elif event == 'Go to Search':
        roku.search()
    elif event == 'Submit':
        roku.literal(values[0])
    elif event == 'Backspace':
        roku.backspace()
    elif event == 'Up':
        roku.up()
    elif event == 'Down':
        roku.down()
    elif event == 'Left':
        roku.left()
    elif event == 'Right':
        roku.right()
    elif event == 'Back':
        roku.back()
    elif event == 'OK':
        roku.select()
    elif event == 'Settings':
        roku.home()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.select()
    elif event == 'Sling':
        sling.launch()
    elif event == 'CBS News':
        cbs.launch()
    elif event == 'Amazon':
        amazon.launch()
    elif event == 'MotorTrend':
        motortrend.launch()
    elif event == 'HGTV':
        hgtv.launch()
    elif event == 'NBC News':
        nbc.launch()

window.close()
