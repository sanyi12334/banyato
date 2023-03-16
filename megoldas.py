# 1. feladat
# Olvassa be és tárolja el a melyseg.txt állomány adatait, és annak felhasználásával oldja
# meg a következő feladatokat! 

melysegek=[]
with open("./banyato/melyseg.txt","r",encoding="utf-8") as fm1:
    fm1.readline()
    fm1.readline()
    for sor in fm1:
        seged_lista=list(map(int,sor.strip().split()))
        #print(seged_lista)
        melysegek.append(seged_lista)

#print(melysegek)

from colorama import Fore, Back

for melyseg_sor in melysegek:
    for melyseg in melyseg_sor:
        if melyseg>0:
            print(f"{Back.BLUE}{Fore.RED}{melyseg:2d}", end=" ",)
        else:
            print(f"{Back.RESET}{Fore.BLACK}{melyseg:2d}", end=" ",)
    print()



# 2. feladat
# Kérje be egy mérési eredmény sor- és oszlopazonosítóját, majd írassa ki az adott helyen
# mért adatot a képernyőre! (A sorok és oszlopok számozása kezdődjön 1-gyel!)