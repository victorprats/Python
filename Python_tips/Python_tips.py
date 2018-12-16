# -*- coding: utf-8 -*-
#
# --------------------------------------
#    List of Python tips and tricks 
# --------------------------------------
# Script Name : Python_tips.py
# Author : Victor Prats
# Created : 21 Oct 2018
# Version : 1.0
# Description : List of Python tips and tricks from internet

# --- Poem Tim Peters ---
import this


# --- Reverse list ---
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b.reverse()
print (b)


# --- Reverse string ---
s = "Hello world"
s = s[::-1]
print (s)


# --- Adding 2 lists ---
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = a + b

print (c)


# --- Calendar yy-mm ---
import calendar
print(calendar.month(2018, 10))


# --- Print help from imported module in html ---
# --- list of modules 'https://docs.python.org/3/py-modindex.html')
import pydoc

pydoc.writedoc("tkinter.messagebox")


# --- Python help ---
help("tkinter")
help("datetime")
help("os")


# --- Identify functions pending to implement with TODO and pass ---
# TODO
def search():
    pass


# --- Print date and time ---
import datetime

now = datetime.datetime.now()
time_now = (now.day, now.month, now.year, now.hour, now.minute, now.second)
print(time_now)
print(now.day, "/", now.month, "/", now.year)
print(now.hour, ":", now.minute, ":", now.second)


# --- Print Python version ---
import sys

print("Current Python version: ", sys.version)


# 1. Simple HTTP Server from cmd...:
# python -m http.server
# python -m http.server 8080
# python -m http.server --help
# ------------------------------
# 2. From internet explorer:
# localhost:8000
# Directory listing for /


# How to know all packages installed with pip
# ----
# pip list
# ---


