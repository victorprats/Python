# https://pyautogui.readthedocs.io/en/latest/mouse.html
#! python3


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
  
# import pyautogui
# pyautogui.displayMousePosition()
