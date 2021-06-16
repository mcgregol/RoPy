from appJar import gui
from roku import Roku
from pynput import keyboard
from pynput.keyboard import Key
import threading

roku = Roku('192.168.1.5')

def press(button):
    if button == "Home":
        roku.home()
    elif button == "Go to Search":
        roku.search()
    elif button == "Back":
        roku.back()
    elif button == "OK":
        roku.select()
    elif button == "Settings":
        roku.home()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.down()
        roku.select()
    elif button == "Submit":
        userInput = app.getEntry("Send text:")
        roku.literal(userInput)
    elif button == "Backspace":
        roku.backspace()
    elif button == "⬆️":
        roku.up()
    elif button == "⬅️":
        roku.left()
    elif button == "➡️":
        roku.right()
    elif button == "⬇️":
        roku.down()
    elif button == "NETFLIX":
        netflix.launch()
    elif button == "SLING":
        sling.launch()
    elif button == "AMAZON":
        amazon.launch()
    else:
        hbo.launch()

def rokuSubmitText():
        userInput = app.getEntry("Send text:")
        roku.literal(userInput)

# Keybindings
def on_press(key):
    if(key==Key.left):
        roku.left()
    elif(key==Key.right):
        roku.right()
    elif(key==Key.down):
        roku.down()
    elif(key==Key.up):
        roku.up()
    elif(key==Key.enter):
        rokuSubmitText()

def listenKeyboard():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# daemon=True stops thread when gui is closed
keyboard_listener = threading.Thread(target=listenKeyboard, daemon=True)
keyboard_listener.start()

# Channel shortcuts
sling = roku['Sling TV']
netflix = roku['Netflix']
amazon = roku['Prime Video']
hbo = roku['HBO Max']

# End of backend code, just frontend from here on out
app = gui("Main", "1600x900")

app.addLabel("title", "RoPy Roku Client")
app.setLabelFg("title", "purple")
app.setLabelFont("title", size=28, family='Times')

app.addButtons(["Home", "Go to Search", "Back", "Settings"], press)

app.addLabelEntry("Send text:")
app.setLabelFont("Send text:", size=10)
app.addButtons(["Submit", "Backspace"], press)

app.addButtons(["⬆️"], press)
app.addButtons(["⬅️", "OK", "➡️"], press)
app.addButtons(["⬇️"], press)

app.addButtons(["NETFLIX", "SLING", "AMAZON", "HBO"], press)
app.setButtonBg("NETFLIX", "red")
app.setButtonBg("SLING", "yellow")
app.setButtonBg("AMAZON", "blue")
app.setButtonBg("HBO", "pink")

app.go()
