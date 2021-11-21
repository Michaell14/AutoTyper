"""
This project was created to complete long, repetitive typing tasks. You are prompted to enter a series of combinations which will be repeated.
The series of either messages or keyboard presses will activate for a given amount of times. As you sit back and relax, the program will do the work for you.

Using:
- Pyautogui: typing and keyboard presses
- PySimpleGUI: User interface
"""

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