# -*- coding: utf-8 -*-
#
# --------------------------------------
#            System tools v1.0
# --------------------------------------
# Script Name : System_tools.py
# Author : Victor Prats
# Created : 19 Aug 2018
# Version : 1.0
# Description : System information: host name, IP, external IP, MAC address, screen resolution,...

from tkinter import *
import platform
import time
import socket
import urllib.request
import uuid
from subprocess import call

host_name = StringVar
host_ip = StringVar
external_ip = StringVar
mac = StringVar
screen_width = StringVar
screen_height = StringVar
os = StringVar
cpu = StringVar
arc = StringVar


# ---------- Create window object ----------
root = Tk()
title = root.title("Sysinfo v1.0")

# ---------- Status bar ----------
status = Label(root, text="Created by VPC", bd=1, relief=SUNKEN, anchor=W)
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
Top_frame = Frame(root, width=480, height=400, relief=SUNKEN)
Top_frame.pack(side=TOP)

lblInfo = Label(Top_frame, font=('arial', 20, 'bold'), text="System information", fg="black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)


# ---------- Add Date and Time ----------
def get_date_time():
    localtime = time.asctime(time.localtime(time.time()))
    lblInfo = Label(Top_frame, font=('arial', 10, 'bold'), text=localtime, fg="Steel Blue", bd=5, anchor='w')
    lblInfo.grid(row=1, column=0)

get_date_time()


# ---------- Function to display (hostname and IP address) ----------
def get_host_name_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)

        Label(Bottom_r_Frame, text=host_name, width=50, relief=RAISED).place(x=50, y=10)  # Display results
        Label(Bottom_r_Frame, text=host_ip, width=50, relief=RAISED).place(x=50, y=30)  # Display results

        print("Hostname :  ", host_name)
        print("Internal IP : ", host_ip)

    except:
        print("Unable to get Hostname and IP")


# ---------- Function to display (External IP address) ----------
def get_external_ip():
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    Label(Bottom_r_Frame, text=external_ip, width=50, relief=RAISED).place(x=50, y=60)

    print("External IP: ", external_ip)


# ---------- Function to display (MAC address) ----------
def get_mac_address():
    from uuid import getnode as get_mac
    mac = get_mac()
    print("The MAC address in formatted way is : ", end="")
    print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                    for ele in range(0, 8 * 6, 8)][::-1]))
    Label(Bottom_r_Frame, text=mac, width=50, relief=RAISED).place(x=50, y=100)


# ---------- Function to get Screen size ----------
def get_screen_size():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    Label(Bottom_r_Frame, text=screen_width, width=50, relief=RAISED).place(x=50, y=140)
    Label(Bottom_r_Frame, text=screen_height, width=50, relief=RAISED).place(x=50, y=160)

    print("Screen width:", screen_width)
    print("Screen height:", screen_height)


# ---------- Function to get OS ----------
def get_os():
    os = platform.platform()
    cpu = platform.processor()
    arc = platform.architecture()

    Label(Bottom_r_Frame, text=os, width=50, relief=RAISED).place(x=50, y=180)  # Display results
    Label(Bottom_r_Frame, text=cpu, width=50, relief=RAISED).place(x=50, y=200)  # Display results
    Label(Bottom_r_Frame, text=arc, width=50, relief=RAISED).place(x=50, y=220)  # Display results

    print("OS:", os)
    print("CPU:", cpu)
    print("Architecture:", arc)


# ---------- Function calls Calendar.py ----------
def call_Calendar_py():
    call('python Calendar.py', shell=True)


# ---------- Function to Close window ----------
def close_window():
    root.destroy()


# ---------- Left Frame and Create buttons and actions ----------
Left_frame = Frame(root, background="gray76", width=170, height=380, relief=SUNKEN)
Left_frame.pack(side=LEFT)

button_1 = Button(Left_frame, text="Get hostname and IP", width=18, command=get_host_name_ip).place(x=10, y=20)
button_2 = Button(Left_frame, text="External IP address", width=18, command=get_external_ip).place(x=10, y=60)
button_3 = Button(Left_frame, text="MAC address", width=18, command=get_mac_address).place(x=10, y=100)
button_4 = Button(Left_frame, text="Screen size", width=18, command=get_screen_size).place(x=10, y=140)
button_5 = Button(Left_frame, text="Operating System", width=18, command=get_os).place(x=10, y=180)


button_9 = Button(Left_frame, text="Calendar", width=18, command=call_Calendar_py).place(x=10, y=300)

button_10 = Button(Left_frame, text="Close", width=18, command=root.quit).place(x=10, y=340)

# ---------- Bottom right Frame and results ----------
Bottom_r_Frame = Frame(root, background="gray76", width=470, height=380)
Bottom_r_Frame.pack(side=RIGHT)

root.mainloop()
