#importovanie modulu
from collections import Counter

#ulozenie vstupu do premennej
vstup = input("Zadaj vetu:")

#zadeklarovanie premennej a zoznamov
male = vstup.lower()
kod = []
kod_int = []

#trieda na priradenie hodnot
priradovanie = {" ":0,"a":1,"b":11,"c":111,"d":2,"e":22,"f":222,"g":3,"h":33,"i":333,
                "j":4,"k":44,"l":444,"m":5,"n":55,"o":555,"p":6,"q":66,"r":666,
                "s":7,"t":77,"u":777,"v":8,"w":88,"x":888,"y":9,"z":99}

for i in male: #cyklus pre priradovanie hodnot vstupu do zoznamu
    kod.append(str(priradovanie[i]))

#spojenie hodnot v zozname do stringu + pomocna premenna    
zakodovane = " ".join(kod)
zakodovane_1 = "".join(kod)

for ii in zakodovane_1: #cyklus pre konvertovanie hodnot do int
    kod_int.append(int(ii))

#zistenie najviac pouziteho cisla/cisel
pocitadlo = Counter(kod_int)
naj = pocitadlo.most_common(1)[0][1]
vystup = [hodnota for hodnota, cislo in pocitadlo.most_common() if cislo == naj]

#vypisanie pozadovanych hodnot
print(zakodovane)
print("Najčastejšie používané:",*vystup)

