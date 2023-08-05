

import sys
import random

#definovanie japonskych cisel
JAPONSKE_CISLA = {1: "ICHI", 2: "NI", 3: "SAN", 4: "SHI", 5: "GO", 6: "ROKU"}

#pocet pociatocnych penazi
penazenka = 5000

print(""" Jedna sa o tracicnu japonsku hru s 2 kockami. Kocky sa hadzu v bambusovom pohari dealera. Hrac musi uhadnut ci celkova hodnota na kockach je parna(cho) alebo neparna(han).
      """)

#main game loop
while True:
    #Stavenie sa
    print("Mas ", penazenka, " penazi. Kolko chces vsadit? (alebo SKONCIT) ")
    
    while True:
        pot = input()
        if pot.upper() == "SKONCIT":
            print("Dakujem za hranie.")
            sys.exit()
        elif not pot.isdecimal():
            print("Vstup nie je cislo. Zadaj cislo.")
        elif int(pot) > penazenka:
            print("Nemas tolko aby si vstavil.")
        else:
            #ak je vklad vhodny
            pot = int(pot)
            break
        
    #hod kockami
    kocka1 = random.randint(1, 6)
    kocka2 = random.randint(1, 6)
    
    print("Dealer hodil kockami.")
    print(" CHO (parne) alebo HAN (neparne)")
    
    #volba hraca
    while True:
        bet = input().upper()
        
        if bet != "CHO" and bet != "HAN":
            print("Prosim zadaj bud: CHO alebo HAN")
            continue
        else:
            break
        
    #zobrazenie hodnot na kocke
    print("Dealer odhalil hodnotu na kockach: ")
    print("  ", JAPONSKE_CISLA[kocka1], " - ", JAPONSKE_CISLA[kocka2])
    print("     ", kocka1, " - ", kocka2)
    
    #urcenie ci hrac vyhral
    hodenieParne = (kocka1 + kocka2) % 2 == 0
    
    if hodenieParne:
        spravnaVolba = "CHO"
    else:
        spravnaVolba = "HAN"
    
    hracVyhral = bet == spravnaVolba
    
    #zobrazenie vysledku
    if hracVyhral:
        print("Vyhral si! Ziskavas ", pot, "penazi")
        penazenka = penazenka + pot
        print("House si zoberie poplatok ", pot // 10)
        penazenka = penazenka - (pot//10)
    else:
        penazenka = penazenka - pot
        print("Prehral si")
        
    #zistenie ci je hrac bez penazi
    if penazenka == 0:
        print("Nemaz peniaze")
        print("Dakujem za hranie")
        sys.exit()
    
