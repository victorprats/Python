# -*- coding: utf-8 -*-
#
# --------------------------------------
#            Endevina el número v1.0
# --------------------------------------
# Script Name : Game_Endevina_num.py
# Author : Victor Prats
# Created : 3 Nov 2018
# Version : 1.0
# Description : Joc per endevinar número (proba random)


import random
import os


a = random.randrange(0, 10)


print()
print("----------------------------------------------------------------------")
print("                    Hola, benvingut al joc...")
print("        ´Encerta el número que pensa en Pyston, perdó Python´")
print("----------------------------------------------------------------------")

contador = 0


def inici_joc():
    global contador
    contador += 1
    print()
    b = int(input("> En quin número penso? "))

    if b < a:
        print()
        print("> El número que tens que endevinar es més gran.")
        inici_joc()

    if b > a:
        print()
        print("> El número que tens que endevinar es més petit.")
        inici_joc()

    else:
        print()
        print("> Felicitats!!! ")
        print(" -> Enhorabona!!! ")
        print(" --> Molt bé!!! ")
        print(" ---> Well done!!!")
        print()
        print("*** El número era el: ", b)
        print("*** Ho has encertat en", contador, "intents :)")

    # Continuem jugant?
        continua = str(input("> Vols fer un altre partida (s/n)? "))

        if continua == "s":
            contador = 0
            os.system('python "C:/Python_projects/Game_Endevina_num.py"')

        else:
            exit()


if __name__ == '__main__':
    inici_joc()
