# -*- coding: utf-8 -*-
#
# --------------------------------------
#          Automation exmples
# --------------------------------------
# Script Name : Automation.py
# Author : Victor Prats
# Created : 16 Dec 2018
# Version : 1.0
# Description : Exemples d'automatització amb Python + Selenium

from tkinter import *


# ---------- Create window object ----------
root = Tk()
title = root.title("Automation v1.0")

# ---------- Status bar ----------
status = Label(root, text="--> (Under development) <--", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill="x")

# ---------- Center new window ----------
w = 640  # width for the Tk window
h = 480  # height for the Tk window

# get screen width and height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

# set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(0, 0)

# ---------- Create Top frame and Title ----------
Top_frame = Frame(root, width=400, height=480, relief=SUNKEN)
Top_frame.pack(side=TOP)

lblInfo = Label(Top_frame, font=('arial', 20, 'bold'),
                text="                   > Automation examples <                   ", bg="dodger blue", fg="white",
                bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

# ---------- Create Bottom Frame  ----------
bottom_frame = Frame(root, background="gray76", width=640, height=480, relief=SUNKEN)
bottom_frame.pack(side=BOTTOM)

filename = PhotoImage(file="C:/Python_projects/images/Sky.png")
background_label = Label(bottom_frame, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(bottom_frame, text="Més exemples:", font=2, bg="SteelBlue1", bd=1, relief=FLAT, anchor=W).place(x=30, y=120)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Example 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# --- Windows notepad and alert window
def windows_desktop():
    import pyautogui
    import time

    pyautogui.hotkey('win')
    time.sleep(1)

    pyautogui.typewrite('notepad.exe')
    pyautogui.hotkey('enter')

    time.sleep(3)

    pyautogui.typewrite('Hola')
    pyautogui.press('enter')
    pyautogui.typewrite('Exemple de com obrir notepad.')
    pyautogui.press('enter')
    pyautogui.typewrite('de pas el robot pot escriure un text.')
    pyautogui.press('enter')
    pyautogui.typewrite('Ara obrirem una finestra nova...')
    time.sleep(3)
    pyautogui.press('enter')

    time.sleep(2)
    pyautogui.alert(text='Que us sembla? :)', title='Finestra', button='OK')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Example 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Búsqueda navegador - Obrir Chrome i fer una búsqueda
def busqueda_navegador():
    import webbrowser
    import pyautogui
    import time

    url = "https://www.google.com/"

    #webbrowser.open(url, new=new)
    webbrowser.open(url)

    time.sleep(3)

    pyautogui.typewrite('python news')
    pyautogui.press('enter')
    pyautogui.alert(text='Resultats sobre... python news', title='Resultats', button='OK')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Example 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Busquem al navegador i fem una captura
def navegador_captura():
    import time
    from selenium import webdriver
    import pyautogui
    import pyautogui as ptg

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Python_projects\chromedriver_win32\chromedriver.exe')
    driver.get('https://ipaddress.ip-adress.com/')
    #driver.get('https://arallegeixo.blogspot.com/')

    # Let the user actually see something!
    time.sleep(1)

    # Go to Search entry
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('83.44.43.14')
    search_box.submit()

    # Let the user actually see something!
    #time.sleep(3)

    #driver.quit()

    #take screenshot
    ptg.screenshot('myscreen.png')

    pyautogui.alert(text='Pantalla capturada com a "myscreen.png" !!! ', title='Finestra', button='OK')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Example 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Búsqueda per objecte en una web
def busqueda_id():
    from selenium import webdriver
    import pyautogui

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options, executable_path=r'C:\Python_projects\chromedriver_win32\chromedriver.exe')
    driver.get('https://www.magiccubemall.com/')

    # Go to Search entry
    driver.find_element_by_id('txtkeyword').send_keys('8x8x8')
    driver.find_element_by_id('btnsearch').click()

    pyautogui.alert(text='Resultats de la búsqueda 8x8x8 en una web.', title='Finestra', button='OK')


# --- Next functions to be defined
def to_be_defined():
    pass


# ---------- Function to Close window ----------
def close_window():
    root.destroy()


# ---------- Create buttons and actions ----------
button_1 = Button(bottom_frame, text="Windows notepad", width=25, height=2, command=windows_desktop).place(x=30, y=20)
button_2 = Button(bottom_frame, text="Búsqueda navegador", width=25, height=2, command=busqueda_navegador).place(x=230, y=20)
button_3 = Button(bottom_frame, text="Navegador + Captura", width=25, height=2, command=navegador_captura).place(x=430, y=20)

# --- Direct access ---
button_4 = Button(bottom_frame, text="Búsqueda en una web", width=25, height=2, fg="dark slate blue", command=busqueda_id).place(x=30, y=150)
button_5 = Button(bottom_frame, text="- TBD -", width=25, height=2, fg="dark slate blue", command=to_be_defined).place(x=230, y=150)
button_6 = Button(bottom_frame, text="- TBD -", width=25, height=2, fg="dark slate blue", command=to_be_defined).place(x=430, y=150)
button_7 = Button(bottom_frame, text="- TBD -", width=25, height=2, fg="deep sky blue4", command=to_be_defined).place(x=30, y=190)
button_8 = Button(bottom_frame, text="- TBD -", width=25, height=2, fg="deep sky blue4", command=to_be_defined).place(x=230, y=190)
button_9 = Button(bottom_frame, text="- TBD -", width=25, height=2, fg="blue3", command=to_be_defined).place(x=430, y=190)
button_10 = Button(bottom_frame, text="- TBD -", width=25, fg="purple4", height=2, command=to_be_defined).place(x=30, y=230)
button_11 = Button(bottom_frame, text="- TBD -", width=25, fg="purple4", height=2, command=to_be_defined).place(x=230, y=230)
button_100 = Button(bottom_frame, text="Sortir", width=18, command=close_window).place(x=240, y=360)

if __name__ == '__main__':
    root.mainloop()
