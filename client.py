import tkinter as tk
from tkinter import ttk
from tkinter import *
from roku import Roku
import keyboard



def getInputBoxValue():
    global userInput
    userInput = deviceIP.get()


def connectDevice():
    getInputBoxValue()
    selector.destroy()


selector = Tk()

selector.geometry('550x270')
selector.configure(background='#8A2BE2')
selector.title('Connect Device')


deviceIP = Entry(selector)
deviceIP.place(x=124, y=125)


Button(selector, text='Connect', bg='#E0EEEE', font=(
    'arial', 12, 'normal'), command=connectDevice).place(x=284, y=115)


Label(selector, text='Roku IP:', bg='#8A2BE2', font=(
    'arial', 10, 'normal')).place(x=44, y=125)


selector.mainloop()

######################################################################################

try:
    roku = Roku(userInput)

    # Channel shortcuts
    sling = roku['Sling TV']
    netflix = roku['Netflix']
    amazon = roku['Prime Video']
    nbc = roku['NBC News']
    hbo = roku['HBO Max']

    # Keybindings
    keyboard.add_hotkey(72, lambda: roku.up())
    keyboard.add_hotkey(75, lambda: roku.left())
    keyboard.add_hotkey(77, lambda: roku.right())
    keyboard.add_hotkey(80, lambda: roku.down())
    keyboard.add_hotkey(14, lambda: roku.backspace())
    keyboard.add_hotkey(28, lambda: rokuSubmitText())

    def rokuHome():
        roku.home()

    def rokuSearch():
        roku.search()

    def rokuBack():
        roku.back()

    def rokuOK():
        roku.select()

    def rokuSettings():
        roku.home()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.select()

    def rokuSubmitText():
        userInput = sendText.get()
        roku.literal(userInput)

    def rokuBackspace():
        roku.backspace()

    def rokuUp():
        roku.up()

    def rokOK():
        roku.select()

    def rokuLeft():
        roku.left()

    def rokuRight():
        roku.right()

    def rokuDown():
        roku.down()

    def rokuNetflix():
        netflix.launch()

    def rokuSling():
        sling.launch()

    def rokuAmazon():
        amazon.launch()

    def rokuHBO():
        hbo.launch()

    def rokuNBC():
        nbc.launch()

    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('870x550')
    root.configure(background='#8A2BE2')
    root.title('Liam\'s Roku Client v2.2')

    Button(root, text='Home', bg='#F0F8FF', font=(
        'arial', 12, 'normal'), command=rokuHome).place(x=241, y=101)

    Label(root, text='Liam\'s Roku Client', bg='#8A2BE2',
          font=('arial', 20, 'bold')).place(x=11, y=11)

    Button(root, text='Go to Search', bg='#F0F8FF', font=(
        'arial', 12, 'normal'), command=rokuSearch).place(x=331, y=101)

    Button(root, text='Back', bg='#F0F8FF', font=(
        'arial', 12, 'normal'), command=rokuBack).place(x=471, y=101)

    Button(root, text='OK', bg='#F0F8FF', font=(
        'arial', 12, 'normal'), command=rokuOK).place(x=561, y=101)

    Button(root, text='Settings', bg='#F0F8FF', font=(
        'arial', 12, 'normal'), command=rokuSettings).place(x=631, y=101)

    sendText = Entry(root)
    sendText.place(x=291, y=171)

    Button(root, text='Submit', bg='#F0F8FF', font=('arial', 12,
                                                    'normal'), command=rokuSubmitText).place(x=451, y=161)

    Button(root, text='Backspace', bg='#F0F8FF', font=(
        'arial', 12, 'normal'), command=rokuBackspace).place(x=551, y=161)

    Button(root, text='↑', bg='#F0F8FF', font=(
        'arial', 12, 'normal'), command=rokuUp).place(x=413, y=231)

    Button(root, text='OK', bg='#F0F8FF', font=(
        'arial', 12, 'normal'), command=rokOK).place(x=404, y=282)

    Button(root, text='←', bg='#F0F8FF', font=('arial', 12,
                                               'normal'), command=rokuLeft).place(x=348, y=282)

    Button(root, text='→', bg='#F0F8FF', font=('arial', 12,
                                               'normal'), command=rokuRight).place(x=469, y=284)

    Button(root, text='↓', bg='#F0F8FF', font=('arial', 12,
                                               'normal'), command=rokuDown).place(x=413, y=333)

    Button(root, text='NETFLIX', bg='#EE2C2C', font=(
        'arial', 12, 'normal'), command=rokuNetflix).place(x=131, y=401)

    Button(root, text='SLING', bg='#1874CD', font=(
        'arial', 12, 'normal'), command=rokuSling).place(x=261, y=401)

    Button(root, text='AMAZON', bg='#00688B', font=(
        'arial', 12, 'normal'), command=rokuAmazon).place(x=381, y=401)

    Button(root, text='HBO', bg='#FF69B4', font=(
        'arial', 12, 'normal'), command=rokuHBO).place(x=511, y=401)

    Button(root, text='NBC NEWS', bg='#FFF68F', font=(
        'arial', 12, 'normal'), command=rokuNBC).place(x=621, y=401)

    root.mainloop()

except:
    connectionError = Tk()

    connectionError.geometry('530x280')
    connectionError.configure(background='#8A2BE2')
    connectionError.title('Connection Error')

    Label(connectionError, text='Wrong IP!', bg='#8A2BE2',
          font=('arial', 17, 'bold')).place(x=216, y=122)

    connectionError.mainloop()
