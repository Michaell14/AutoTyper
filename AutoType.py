import pyautogui, time
import PySimpleGUI as sg

sg.theme("DarkAmber")

#1 = Write
#2 = Press a key
action=[]
values=[]
numCombo=0

layout1=[[sg.Text("How many iterations of the combination: ")],
        [sg.Text("Enter: "), sg.InputText()],
        [sg.OK(), sg.Cancel()]]
layout2=[[sg.Text("1) Write (What to type on the screen)\n2) Key (What to press)")],
        [sg.Text("Option"), sg.InputText(do_not_clear=False)],
        [sg.Text("Value: "), sg.InputText(do_not_clear=False)],
        [sg.Text("Amount: "), sg.InputText(do_not_clear=False)],
        [sg.OK(), sg.Cancel()]]

window=sg.Window("Spammer.py", layout1)

event, vals=window.read()
numCombo = int(vals[0])
window.close()

window=sg.Window("Spammer.py", layout2)
while True:
    event, vals=window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    action.append(int(vals[0]))
    values.append([vals[1], int(vals[2])])

window.close()
print(action)
print(values)

print("STARTING...")


def main():
    for i in range(len(values)):
        val=values[i][0]

        for x in range(values[i][1]):
            if action[i]==1:
                pyautogui.write(val)
            else:
                pyautogui.press(val)
                time.sleep(.5)

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

for i in range(numCombo):
    main()
    time.sleep(1)

"""
print("Starting...")
time.sleep(2)
for i in range(10):
    pyautogui.write("$w")
    pyautogui.press("Enter")
    time.sleep(.5)
"""
"""
screenWidth, screenHeight=pyautogui.size()
print("starting")
time.sleep(2)

currMouseX, currMouseY = pyautogui.position()
print(currMouseX, " ", currMouseY)
"""

'''
time.sleep(3)


for i in range(1, 100):
    pyautogui.typewrite("Testing: " + str(i))
    pyautogui.press("Enter")


#pyautogui.typewrite("!clear 10")
#pyautogui.press("Enter")
'''

"""
pyautogui.move(x,y) #moves mouse relative to current position
pyautogui.doubleClick() #double clicks
pyautogui.moveTo(x,y, duration=seconds, tween=pyautogui.easeInOutQuad)

pyautogui.write(message, interval) #pause in between each key press
pyautogui.press('esc') #press the esc key. All key names are in pyautogui.KEY_NAMES

with pyautogui.hold("shirt"):
    pyautogui.press(['left','left','left','left']) #press left arrow key 4 times

pyautogui.hotkey("ctrl", "c") #press the ctrl-c hotkey combination
pyautogui.alert("This is the message to display") #Make alert box appear
"""