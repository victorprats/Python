# https://pyautogui.readthedocs.io/en/latest/mouse.html
#! python3

# example_1
import pyautogui, sys


print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
    
# example_2
import pyautogui


pyautogui.displayMousePosition()

