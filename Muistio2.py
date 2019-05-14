#-*- coding: cp1252 -*-

import pickle
import time

def readfile(name):
    while True:
        try:
            readfile = open(name,'r')
            content = readfile.read()
            readfile.close()
            return content
        except IOError:
            emptyfile(name)
            if name == "muistio.txt":
                print("Oletusmuistioa ei l�ydy, luodaan tiedosto.")
            else:
                print("Tiedostoa ei l�ydy, luodaan tiedosto.")
                
def writefile(name, uinput):
    try:
        uinput = uinput+":::"
        uinput += time.strftime("%X %x")
        addfile = open(name,'a')
        addfile.write(uinput+"\n")
        addfile.close()
    except IOError:
        return False
    
def emptyfile(name):
    try:
        emptyfile = open(name,'w')
        emptyfile.close()
    except IOError:
        return False

def main():
    filename="muistio.txt"
    readfile(filename)
    while True:
        print("K�ytet��n muistiota:", filename)
        selection=input('''(1) Lue muistikirjaa
(2) Lis�� merkint�
(3) Tyhjenn� muistikirja
(4) Vaihda muistiota
(5) Lopeta
Mit� haluat tehd�?: ''')
        if selection=='1':
            content=readfile(filename)
            print(content)
        elif selection=='2':
            uinput=input("Kirjoita uusi merkint�: ")
            writefile(filename, uinput)
        elif selection=='3':
            emptyfile(filename)
            print("Muistio tyhjennetty.")
        elif selection=='4':
            filename=input("Anna tiedoston nimi: ")
            readfile(filename)
        elif selection=='5':
            print("Lopetetaan")
            break

if __name__ == "__main__":
    main()
