# -*- coding: utf-8 -*-
#
# --------------------------------------
#           El Penjat v1.0
# --------------------------------------
# Script Name : Game_Penjat.py
# Author : Victor Prats
# Created : 24 Nov 2018
# Version : 1.0
# Description : Joc per endevinar paraula (proba random)


import random

index = -1
dictionary = ("abella", "aranya", "ase", "bou", "burro", "balena", "cabra", "camell", "canari", "cangur", "castor",
              "cavall", "conill", "cargol", "cigne", "cigonya", "coala", "cobra", "cocodril", "colom", "conill",
              "elefant", "escarabat", "formiga", "gos", "gall", "gallina", "gat", "girafa", "guineu", "granota",
              "grill", "guepard", "guineu", "jaguar", "llebre", "lloro", "llop", "mico", "mosca", "mosquit", "ocell",
              "ovella", "papallona", "peix", "porc", "rata", "rinoceront", "ruc", "serp", "tigre", "toro", "tortuga",
              "vaca", "zebra")


def inici_joc():
    word = random.choice(dictionary)
    word_len = len(word)
    guess = ""
    attempt = 0
    enter = ""
    temp = "_" * word_len


    print("")
    print("\t\t\t                    =====")
    print("\t\t\t          ==========================")
    print("\t\t\t        ==============================")
    print("\t\t\t      ==================================")
    print("\t\t\t      Benvingut a un nou joc d'en Pyston")
    print("\t\t\t      ==================================")
    print("")
    print("\t\t\t En aquest joc has d'endevinar una paraula")
    print("\t\t La paraula que ha escollit en Pyston te", word_len,"lletres.")
    print("\t\t  Escriu una lletra a veure si forma part de la paraula.")
    print("\t\t Recorda que només tens màxim 10 intents.\n")
    print("\t\t\t\t   MOLTA SORT!!!\n\n\n\n")

    for i in range(0, 10):
        attempt +=1
        guess = input("> Intent no. "+str(attempt)+": ")
        if guess in word and guess != enter:
            for i in range(0, word_len):
                if guess == word[i]:
                    temp = temp[:i] + guess +temp[i+1:]
            print("Correcte!\n" + temp)
        if guess not in word:
            print("Aquesta lletra no hi es. \n")
        if "_" not in temp:
            print("\t\t*********** Felicitats!!! Has endevinat la paraula *************")
            print("")
            vols_continuar()
        elif attempt == 10:
            guess = input(">>> Per acabar, la paraula és? ")
            if guess == word:
                print("\t\t*********** Felicitats!!! Has endevinat la paraula *************")
            else:
                print("")
                print("\t\t*********** Ohhh... Quina mala sort!!! *************")
                print("\t\t -------> La paraula era: ", word)
                print("")
                vols_continuar()

# Continuem jugant?
def vols_continuar():
    continua = str(input("> Vols fer un altre partida (s/n)? "))

    if continua == "s":
        inici_joc()
    elif continua == "n":
        exit()
    else:
        vols_continuar()


if __name__ == '__main__':
    inici_joc()
