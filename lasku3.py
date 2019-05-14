# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-


import math
a = int(input("Anna ensimmäinen numero:"))
b = int(input("Anna toinen numero:"))
    
while True:
    print ("(1) +")
    print ("(2) -")
    print ("(3) *")
    print ("(4) /")
    print ("(5) sin(luku1/luku2)")
    print ("(6) cos(luku1/luku2)")
    print ("(7) Vaihda luvut")
    print ("(8) Lopeta")
    print ("Valitut luvut:", a, b,)
    valinta = input("Tee valinta (1-8): ")
    if valinta == "1" :
        tulos = a+b
        print ("Tulos on: ",tulos)
    elif valinta == "2" :
        tulos = a-b
        print("Tulos on:", tulos)

    elif valinta == "3" :
        tulos = a*b
        print("Tulos on:", tulos)

    elif valinta == "4" :
        tulos = a/b
        print("Tulos on:", tulos)
    elif valinta == "5" :
        tulos = math.sin(a/b)
        print("Tulos on:", tulos)
    elif valinta == "6" :
        tulos = math.cos(a/b)
        print("Tulos on:", tulos)
    elif valinta == "7":
        a = int(input("Anna ensimmäinen numero:"))
        b = int(input("Anna toinen numero:"))
    elif valinta == "8":
        break

    else:
        print ("Valintaa ei tunnistettu.")
