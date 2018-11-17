# -*- coding: utf-8 -*-
#
# --------------------------------------
#            Endevina el número v1.0
# --------------------------------------
# Script Name : Game_Mentalista.py
# Author : Victor Prats
# Created : 16 Nov 2018
# Version : 1.0
# Description : Joc per endevinar els diners que tens a la butxaca i el nombre de germanes i germans

from os import system

print()
print("----------------------------------------------------------------------")
print("                    Hola, benvingut a un altre joc...                 ")
print()
print("        T'encertaré:                                                  ")
print("            1. La quantitat de diners que tens a la butxaca           ")
print("            2. Les germanes i els germans que tens.                   ")
print("----------------------------------------------------------------------")

print(" Si us plau no facis trampes, recorda que sóc una màquina. :)")
print()
print("Mira quans diners (€) tens a la butxaca i no ho diguis en veu alta, (jo et podria sentir)")
print("1. Multiplica els diners que tens x10")
print("2. Suma al resultat +25")
print("3. Suma-li el número de germanes que tens")
print("4. Multiplica el resultat x10")
print("5. Suma-li el número de germans que tens")
print("6. Per acabar, resta al resultat -250")
print()


def inici_joc():
    num = (input("Escriu el resultat que t'ha donat (4 xifres): "))

    if len(num) > 4:
        print("Hmm, crec que m'estàs enredant. No pot ser...")
        print("Torna-ho a provar")
        print()
        inici_joc()

    if len(num) < 4:
        print("Si us plau escriu un número de 4 xifres")
        print()
        inici_joc()

    else:
        print("------------------------------------------")
        print("> Els diners que tens a la butxaca son: ", num[-4], num[-3], " €", sep="")
        print("> El nombre de germanes que tens es:", num[-2])
        print("> El nombre de germans que tens es:", num[-1])
        print()
        input(">> Apreta una tecla per continuar.")

# Continuem jugant?
def vols_continuar():
    continua = str(input("> Vols fer un altre partida (s/n)? "))

    if continua == "s":
        system('cls')
        system('python "C:/Python_projects/Game_Mentalista.py"')

    if continua == "n":
        exit()

    else:
        vols_continuar()


if __name__ == '__main__':
    inici_joc()
