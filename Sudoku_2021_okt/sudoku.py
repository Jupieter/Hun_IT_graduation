# https://www.informatikatanarok.hu/media/uploads/Informatika_erettsegi/Emelt/e_inf_21okt_fl.pdf
import os
print("\033[0;37;40m")
os.system('cls')
from time import sleep

fájl_list = ["konnyu.txt", "kozepes.txt", "nehez.txt"]
választható = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# https://stackabuse.com/how-to-print-colored-text-in-python/


def adat_beolvasás(fájlnév):
    beolvasni_a = 'Forrasok/4_Sudoku/' + fájlnév
    forrásfájl = open(beolvasni_a)
    # print("forrásfájl:        ", forrásfájl)
    print("--------------------------------------")


    lista = forrásfájl.readlines()
    lista_végek_nélkül = []
    for elem in lista:
        lista_végek_nélkül.append(elem.strip())
    forrásfájl.close()
    # print(lista_végek_nélkül)
    return lista_végek_nélkül

def sudoku_tábla(lista_végek_nélkül):
    sudoku_tábla = []
    for  i in range( 0,9,1):
        belső_lista = []
        for elem in lista_végek_nélkül[i]:
            if elem != " ":
                belső_lista.append(elem)
        # print("belső_lista:", belső_lista )
        sudoku_tábla.append(belső_lista)
    print(sudoku_tábla)
    return sudoku_tábla

def sudoku_üres(sudoku):
    üres = []
    for s, sor in enumerate(sudoku):
        print(s, end = "\n")
        lista = []
        for o, elem in  enumerate(sor):
            logika = False
            if elem == "0":
                logika = True
            lista.append(logika)
        üres.append(lista)    
    return üres
            


def sudoku_megjelenít(sudoku, sor, oszlop, érték, üres):
    os.system('cls')
    print("\033[1;34;40m      1   2   3   4   5   6   7   8   9  ")
    print("\033[1;34;40m________________________________________")
    i, j = 0 , 0
    for sors in sudoku:
        i += 1
        j = 0
        print("\033[1;34;40m", i, "| ", end="")
        for elem in sors:
            j += 1
            oszlop_maradék = int(j)%3
            if oszlop_maradék == 0:
                elválasztó = "|"
            else:
                elválasztó = " "
            if üres[i-1][j-1] and elem == "0":
                print("\033[0;37;43m", elem, elválasztó, end ="")
            elif üres[i-1][j-1] and elem != "0":
                print("\033[0;37;42m", elem, elválasztó, end ="")
            else:
                print("\033[0;37;40m", elem, elválasztó, end ="")
        print("\033[0;37;40m")
        sor_maradék = int(i)%3
        if sor_maradék == 0:
            print("-----------------------------------------")
    print("\033[0;37;40m ")
    print("Táblázat lekérdezés          ", "Választható számok: ", választható )
    print("sor: ", sor, "        oszlop: ", oszlop, "       érték: ", érték)

def próbálkozások(lista_végek_nélkül):
    próbálkozások = []
    for  i in range( 9,len(lista_végek_nélkül),1):
        belső_lista = []
        for elem in lista_végek_nélkül[i]:
            if elem != " ":
                belső_lista.append(elem)
        # print("belső_lista:", belső_lista )
        próbálkozások.append(belső_lista)
    return próbálkozások

def adat_kérés(szöveg = "Nincs szöveg !!!"):
    választás = None
    megvan = False
    while megvan != True:
        választás = input(szöveg)
        # print(választás, type(választás))
        for elem in választható:
            if választás == elem:
                megvan = True
        if megvan == False:
            print('"', választás, '"  nem választható', end = "\r\r")
            sleep(1.2)
    sleep(0.7)
    return választás

def hely_ellenőr(sudoku, sor, oszlop):
    sor = int(sor)
    oszlop = int(oszlop)
    résztáblázat_érték = (int(sor / 3.3) * 3 )  + int(oszlop / 3.3) + 1  # balról jobbra és fentről lefelé növekvő
    print("Az adott helyen szereplő szám:", sudoku[sor-1][oszlop-1])
    print("A hely a(z) ", résztáblázat_érték, " résztáblázathoz tartozik.")

def üres_helyek(sudoku):
    üres = 0
    for sor in sudoku:
        for elem in sor:
            if elem == "0":
                üres += 1
    kitöltés = int(üres/81 *10000)/100
    print("Az üres helyek aránya: ", kitöltés, "%")

def beadott_adat_ellenőr(sudoku, sor, oszlop, szám):
    lehet = True
    sor = int(sor)
    oszlop = int(oszlop)
    adat = sudoku[sor-1][oszlop-1]
    print("A kiválasztott sor: ", sor, "oszlop: ", oszlop, "a szám: ", szám)
    if adat != "0":
        print("A helyet már kitöltötték." )
        lehet = False
    else:
        for o in range(1,10,1):
            elem = sudoku[sor-1][o-1]
            if elem == szám:
                print("Az adott sorban már szerepel a szám")
                lehet = False
        for s in range(1,10,1):
            elem = sudoku[s-1][oszlop-1]
            if elem == szám:
                print("Az adott oszlopban már szerepel a szám")
                lehet = False
        
        sor_kezdet = (int(sor / 3.3) * 3 )
        oszlop_kezdet = int(oszlop / 3.3) * 3
        # print(sor_kezdet , "sor ", sor_kezdet + 3,  "   |      ",    oszlop_kezdet      ,"oszlop", oszlop_kezdet + 3)
        for sr in range(sor_kezdet, sor_kezdet + 3, 1):
            for os in range(oszlop_kezdet, oszlop_kezdet + 3, 1):
                if sudoku[sr][os] == szám:
                    print("Az adott résztáblázatban már szerepel a szám")
                    lehet = False
    if lehet:
        print("A lépés megtehető")
    return lehet

def lépés_mentés(sudoku, sor, oszlop, szám):
    sudoku[int(sor)-1][int(oszlop)-1] = szám
    return sudoku



def játék_interface(fájlnév):
    forrás = adat_beolvasás(fájlnév = "konnyu.txt")
    sudoku = sudoku_tábla(forrás)
    üres = sudoku_üres(sudoku)
    for i in üres:
        print(i)
    ismétlés = False
    sor, oszlop, érték = None, None, None
    sudoku_megjelenít(sudoku, sor, oszlop, érték, üres)
    while ismétlés != True:
        választás = input(" [R] => Megadott adatok futtatása        [B] => visszalép a főmenübe:         [J] vagy [0] => játék ")
        if választás.capitalize() == "J" or választás.capitalize() == "0":
            sudoku_megjelenít(sudoku, sor, oszlop, érték, üres)
            sor = adat_kérés("Adja meg egy sor számát!  ")
            sudoku_megjelenít(sudoku, sor, oszlop, érték, üres)
            oszlop = adat_kérés("Adja meg egy oszlop számát!  ")
            sudoku_megjelenít(sudoku, sor, oszlop, érték, üres)
            print("3. feladat ")
            hely_ellenőr(sudoku, sor, oszlop)
            print("4. feladat ")
            üres_helyek(sudoku)
            szám = adat_kérés("Adja meg a számot beírandó!  ")
            lehet = beadott_adat_ellenőr(sudoku, sor, oszlop, szám)
            if lehet:
                mentsem = input(" [I] vagy [0] => menti:         [N] => nem menti ")
                if mentsem.capitalize() == "I" or mentsem == "0":
                    print("mentése:")
                    sudoku = lépés_mentés(sudoku, sor, oszlop, szám)
                    sudoku_megjelenít(sudoku, sor, oszlop, érték, üres)
            else:
                print("Nem menthető")
                sleep(2)
        if választás.capitalize() == "R":
            print("5. feladat ")
            próbák = próbálkozások(forrás)
            for adat in próbák:
                print(adat)
                szám_r = adat[0]
                sor_r = adat[1]
                oszlop_r = adat[2]
                beadott_adat_ellenőr(sudoku, sor_r, oszlop_r, szám_r)
        if választás.capitalize() == "B":
            ismétlés = True





# Main program call the functions
 # 1. choice
választott = True
while választott:
    os.system('cls')
    print("1. feladat ")
    print("Válassz neházségi szintet! \n [1] - könnyű, \n [2] - közepes \n [3] - nehéz \n [0] - kilépés a programból" )
    választás = input("Adja meg a bemeneti fájl nevét! (A számával)" )
    # print("választás:", választás, type(választás))
    sleep(0.5)
    if választás == "0":
        választott = False
    elif választás == "1" or választás == "2" or választás == "3":
        fájlnév = fájl_list[int(választás)-1]
        print(fájlnév)
        játék_interface(fájlnév)
        sleep(1)
        választott = True
    else:
        választott == True