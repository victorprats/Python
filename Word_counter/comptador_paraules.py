# -*- coding: utf-8 -*-
#
# --------------------------------------
#      Comptador de paraules v1.0
# --------------------------------------
# Script Name : comptador_paraules.py
# Author : Victor Prats
# Created : 6 Dec 2018
# Version : 1.0
# Description : Compta les paraules d'un arxiu txt


def inici():
    # pair of braces creates an empty dictionary: {}
    # https://docs.python.org/3/tutorial/datastructures.html
    comptador = {}

    arxiu = input("\nQuin arxiu (*.txt) vols analitzar? ")
    print("\n - Analitzant document...")

    with open(arxiu, 'r') as document:
        for line in document:
            # Treiem caracters de puntuació i passem el text a minúscules
            llista_paraules = line.replace(',', '').replace('\'', '').replace('/', '').replace('.', '').replace('-', '').\
                replace('*', '').replace('!', '').lower().split()

            # Fiquem les paraules en una llista
            for paraula in llista_paraules:
                # Afegim un contador de cada paraula
                if paraula not in comptador:
                    comptador[paraula] = 1
                else:
                    # Si la paraula existeix +1 al contador
                    comptador[paraula] = comptador[paraula] + 1

    # Imprimerix títol de columna en posició determinada
    print('-' * 30)
    print("Paraula", "\t Comptador")
    print('-' * 30)

    # Imprimim les paraules i el comptador.
    for (paraula, occurencia) in comptador.items():
        print('{:15}{:10}'.format(paraula, occurencia))


# Un altre document?
def vols_continuar():
    continua = str(input("\n> Vols analitzar un altre document(s/n)? "))

    if continua == "s":
        inici()
    elif continua == "n":
        exit()
    else:
        vols_continuar()


if __name__ == '__main__':
    inici()
    while True:
        vols_continuar()

