# -*- coding: utf-8 -*-
#
# --------------------------------------
#            Base dades llibres
# --------------------------------------
# Script Name : Base_dades_llibres.py
# Author : Victor Prats
# Created : 27 Oct 2018
# Version : 1.0
# Description : Base de dades de llibres
# Source: This script is a personalized version of ...
# https://www.sourcecodester.com/tutorials/python/11334/python-simple-crud-application-using-sqlite-part-1.html
# https://www.sourcecodester.com/tutorials/python/11349/python-simple-crud-application-using-sqlite-part-2.html

from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Els meus llibres - Base de dades -")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1200
height = 500
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)


# ------------------------- Funcions (Crear bbdd, crear entrada nova, llegir bbddd,...) -------------------------
def Database():
    global conn, cursor
    conn = sqlite3.connect('els_meus_llibres.db')
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `taula` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, titol TEXT, autor TEXT, valoracio TEXT, isbn TEXT, data TEXT, comentaris TEXT)")
        
def Create():
    if TITOL.get() == "" or AUTOR.get() == "" or VALORACIO.get() == "" or ISBN.get() == "" or DATA.get() == "" or COMENTARIS.get() == "":
        txt_result.config(text="Si us plau omple tots els camps!", fg="red", bg="white")
    else:
        Database()
        cursor.execute(
            "INSERT INTO `taula` (titol, autor, valoracio, isbn, data, comentaris) VALUES(?, ?, ?, ?, ?, ?)",
            (str(TITOL.get()), str(AUTOR.get()), str(VALORACIO.get()), str(ISBN.get()), str(DATA.get()),
             str(COMENTARIS.get())))
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `taula` ORDER BY `autor` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        conn.commit()
        TITOL.set("")
        AUTOR.set("")
        VALORACIO.set("")
        ISBN.set("")
        DATA.set("")
        COMENTARIS.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Base de dades creada!", fg="green", bg="white")


def Read():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `taula` ORDER BY `autor` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    cursor.close()
    conn.close()
    txt_result.config(text="Base de dades llegida correctament.", fg="green", bg="white")


def Update():
    Database()
    if VALORACIO.get() == "":
        txt_result.config(text="Valoració", fg="red")
    else:
        tree.delete(*tree.get_children())
        cursor.execute(
            "UPDATE `taula` SET `titol` = ?, `autor` = ?, `valoracio` =?,  `isbn` = ?,  `data` = ?, `comentaris` = ? WHERE `mem_id` = ?",
            (str(TITOL.get()), str(AUTOR.get()), str(VALORACIO.get()), str(ISBN.get()), str(DATA.get()),
             str(COMENTARIS.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `taula` ORDER BY `autor` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        cursor.close()
        conn.close()
        TITOL.set("")
        AUTOR.set("")
        VALORACIO.set("")
        ISBN.set("")
        DATA.set("")
        COMENTARIS.set("")
        btn_create.config(state=NORMAL)
        btn_read.config(state=NORMAL)
        btn_update.config(state=DISABLED)
        btn_delete.config(state=NORMAL)
        txt_result.config(text="Base de dades actualitzada correctament.", fg="green", bg="white")


def OnSelected(event):
    global mem_id;
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    TITOL.set("")
    AUTOR.set("")
    VALORACIO.set("")
    ISBN.set("")
    DATA.set("")
    COMENTARIS.set("")
    TITOL.set(selecteditem[1])
    AUTOR.set(selecteditem[2])
    ISBN.set(selecteditem[4])
    DATA.set(selecteditem[5])
    COMENTARIS.set(selecteditem[6])
    btn_create.config(state=DISABLED)
    btn_read.config(state=DISABLED)
    btn_update.config(state=NORMAL)
    btn_delete.config(state=DISABLED)


def Delete():
    if not tree.selection():
        txt_result.config(text="Selecciona un element de la llista", fg="red")
    else:
        result = tkMessageBox.askquestion('Els meus llibres',
                                          'Estàs segur de voler esborrar aquesta entrada?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `taula` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            txt_result.config(text="Entrada esborrada correctament.", fg="green", bg="white")


def Exit():
    result = tkMessageBox.askquestion('Els meus llibres', 'Estàs segur de voler sortir?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


# ------------------------ Definim les variables ------------------------
TITOL = StringVar()
AUTOR = StringVar()
VALORACIO = StringVar()
ISBN = StringVar()
DATA = StringVar()
COMENTARIS = StringVar()

# ------------------------- Creem els Frames -----------------------------

Top = Frame(root, background="White", width=900, height=50, bd=8, bg="white", relief="groove")
Top.pack(side=TOP)
Left = Frame(root, background="White", width=300, height=500, bd=8, bg="white", relief="flat")
Left.pack(side=LEFT)

Right = Frame(root, width=600, height=500, bd=8, bg="white", relief="raise")
Right.pack(side=RIGHT)

Forms = Frame(Left, width=300, height=450, bg="white")
Forms.pack(side=TOP)

filename = PhotoImage(file="C:/Python_projects/white_bg.png") # Fons del frame
background_label = Label(Forms, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Buttons = Frame(Left, width=300, height=100, bd=8, bg="white", relief="raise")
Buttons.pack(side=BOTTOM)

# Afegit "tristatevalue=0" per evitar tots els radiobuttons seleccionats
RadioGroup = Frame(Forms)
Excellent = Radiobutton(RadioGroup, tristatevalue=0,  text="Excel·lent", variable=VALORACIO, value="Excellent",
                        font=('arial', 10), bg="white").pack(side=LEFT)
Bo = Radiobutton(RadioGroup,text="Bo", tristatevalue=0, variable=VALORACIO, value="Bo",
                 font=('arial', 10) , bg="white").pack(side=LEFT)
Normal = Radiobutton(RadioGroup, tristatevalue=0, text="Normal", variable=VALORACIO, value="Normal",
                     font=('arial', 10), bg="white").pack(side=LEFT)
Dolent = Radiobutton(RadioGroup, tristatevalue=0, text="Dolent", variable=VALORACIO, value="Dolent",
                     font=('arial', 10), bg="white").pack(side=LEFT)


# ------------------------- Creem les etiquetes a la finestra -------------------------
txt_title = Label(Top, width=900, font=('arial', 24), text="Els meus llibres - v1.0", fg="white", bg="medium blue")
txt_title.pack()
txt_titol = Label(Forms, text="Títol:", font=('arial', 16), bd=10, bg="white")
txt_titol.grid(row=0, sticky="e")
txt_autor = Label(Forms, text="Autor:", font=('arial', 16), bd=10, bg="white")
txt_autor.grid(row=1, sticky="e")
txt_valoracio = Label(Forms, text="Valoració:", font=('arial', 16), bd=10, bg="white")
txt_valoracio.grid(row=2, sticky="e")
txt_isbn = Label(Forms, text="ISBN:", font=('arial', 16), bd=10, bg="white")
txt_isbn.grid(row=3, sticky="e")
txt_data = Label(Forms, text="Data (dd/mm/aa):", font=('arial', 16), bd=15, bg="white")
txt_data.grid(row=4, sticky="e")
txt_comentaris = Label(Forms, text="Comentaris:", font=('arial', 16), bd=15, bg="white")
txt_comentaris.grid(row=5, sticky="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

# ------------------------- Disposició de les entrades -------------------------
titol = Entry(Forms, textvariable=TITOL, width=30)
titol.grid(row=0, column=1)
autor = Entry(Forms, textvariable=AUTOR, width=30)
autor.grid(row=1, column=1)
RadioGroup.grid(row=2, column=1)
isbn = Entry(Forms, textvariable=ISBN, width=30)
isbn.grid(row=3, column=1)
data = Entry(Forms, textvariable=DATA, width=30)
data.grid(row=4, column=1)
comentaris = Entry(Forms, textvariable=COMENTARIS, width=30)
comentaris.grid(row=5, column=1)

# ------------------------- Butons del menú -------------------------------------
btn_create = Button(Buttons, width=10, text="Crear", command=Create, fg="green", bg="white")
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Llegir BBDD", command=Read, fg="blue", bg="white")
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Actualitzar", command=Update, bg="white", state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Esborrar", command=Delete, fg="red", bg="white")
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Sortir", command=Exit, fg="orange", bg="white")
btn_exit.pack(side=LEFT)

# ------------------------- Finestra de resultats (dreta) -------------------------
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("ID", "Titol", "Autor", "Valoracio", "ISBN", "Data", "Comentaris"),
                    selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=W)
tree.heading('Titol', text="Titol", anchor=W)
tree.heading('Autor', text="Autor", anchor=W)
tree.heading('Valoracio', text="Valoracio", anchor=W)
tree.heading('ISBN', text="ISBN", anchor=W)
tree.heading('Data', text="Data", anchor=W)
tree.heading('Comentaris', text="Comentaris", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=150)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

# ------------------------- Inicialització del programa -------------------------
if __name__ == '__main__':
    root.mainloop()
