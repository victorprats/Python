import random

index = -1
dictionary = ("abella", "aranya", "ase", "bou", "burro", "balena", "cabra", "camell", "canari", "cangur", "castor",
              "cavall", "conill", "cargol", "cigne", "cigonya", "coala", "cobra", "cocodril", "colom", "conill",
              "elefant", "escarabat", "formiga", "gos", "gall", "gallina", "gat", "girafa", "guineu", "granota",
              "guepard", "guineu", "jaguar", "llebre", "lloro", "llop", "mico", "mosca", "mosquit", "ocell", "ovella",
              "papallona", "peix", "porc", "rata", "rinoceront", "ruc", "tigre", "toro", "tortuga", "vaca", "zebra")


def inici_joc():
    word = random.choice(dictionary)
    word_len = len(word)
    guess = ""
    attempt = 0
    enter = ""
    #print(word)
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
            break
        elif attempt == 10:
            guess = input(">>> Per acabar, la paraula és? ")
            if guess == word:

                print("\t\t*********** Felicitats!!! Has endevinat la paraula *************")
            else:
                print("")
                print("\t\t*********** Ohhh... Quina mala sort!!! *************")
                print("\t\t -------> La paraula era: ", word)
                print("")

if __name__ == '__main__':
    inici_joc()
    
