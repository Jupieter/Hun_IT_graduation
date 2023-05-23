import os
from time import sleep

os.system('cls')

def beolvasas(fajlnev="kep.txt"):
    beolvasni = "Forras/4_RGBszinek/" + fajlnev
    forrasfajl = open(beolvasni)
    lista = forrasfajl.readlines()
    lista_végek_nélkül = []
    for elem in lista:
        elem_str = elem.strip().split()
        elem_int = [int(x) for x in elem_str]
        triplets = [elem_int[i:i+3] for i in range(0, len(elem_int), 3)]
        lista_végek_nélkül.append(triplets)
    forrasfajl.close()

    # print(lista_végek_nélkül)
    return lista_végek_nélkül

def képpont_adat(lista, sor, oszlop):
    r = lista[sor][oszlop][0]
    g = lista[sor][oszlop][1]
    b = lista[sor][oszlop][2]
    #  print(f"A képpont színe RGB({r},{g},{b})")
    return r, g, b


def világos_pont(lista):
    i = 0
    for sor in lista:
        for oszlop in sor:
             három_összege = oszlop[0] + oszlop[1] + oszlop[2]
             if három_összege > 600:
                 i += 1
    return i
        
def söté_pont(lista):
    legsötét = lista[0][0][0] + lista[0][0][1] +lista[0][0][2]
    sötét_lista = []
    print(legsötét)
    for sor in lista:
        for oszlop in sor:
             három_összege = oszlop[0] + oszlop[1] + oszlop[2]
             if három_összege < legsötét:
                 legsötét = három_összege
    for sor in lista:
        for oszlop in sor:
             három_összege = oszlop[0] + oszlop[1] + oszlop[2]
             if három_összege == legsötét:
                 sötét_rgb = [oszlop[0], oszlop[1], oszlop[2]]
                 sötét_lista.append(oszlop)
    return sötét_lista
    
def hatar(sor, delta=10):
    blue_start = sor[0][2] + delta
    for oszlop in sor:
        blue = oszlop[2]
        print(blue_start, " start/ blue", blue, "delta", delta)
        if blue > blue_start:
            return True
    return False



fajlnev = "kep.txt"
lista = beolvasas(fajlnev)
# print(lista)
os.system('cls')
print("2. feladat:")
print("Kérem egy képpont adatait!")
sor = int(input("Sor: "))
oszlop = int(input("Oszlop: "))
r, g, b = képpont_adat(lista, sor, oszlop)
print(f"A képpont színe RGB({r},{g},{b})")

print("3. feladat:")
világos_db = világos_pont(lista)
print(f"A világos képpontok száma: {világos_db}")

print("4. feladat:")
sötét_lista = söté_pont(lista)
for i in sötét_lista:
    print(f"RGB({i[0]}, {i[1]}, {i[2]})")

print("6. feladat:")
kezd = 0
zár = 0
for key, sor in enumerate(lista):
    van_e = hatar(sor, 10)
    print(key, van_e)
    if kezd == 0 and van_e == True:
        kezd = key
    if zár == 0 and kezd != 0 and van_e == False:
        zár = key
print(f"A felhő legfelső sora: {kezd}")
print(f"A felhő legalsó sora: {zár}")