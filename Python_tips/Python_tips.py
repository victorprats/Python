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
def Search():
    pass
  
  
