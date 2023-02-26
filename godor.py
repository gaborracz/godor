melysegAdatok = list()

with open("melyseg.txt", "r") as file:
    for line in file:
        line = int(line.rstrip())
        melysegAdatok.append(line)

def elsoFeladat(melysegAdatok):
    print("1. feladat")
    print(f"A fájl adatainak száma: {len(melysegAdatok)}\n")

def harmadikFeladat(melysegAdatok):
    erintett = 0
    erintetlen = 0
    
    for i in melysegAdatok:
        if i == 0:
            erintetlen = erintetlen + 1
        else:
            erintett = erintett + 1
    
    arany = (erintetlen / len(melysegAdatok)) * 100
    print(f"Az érintetlen területek aránya {round(arany, 2)}%.\n")

def negyedikFeladat(melysegAdatok):
    godrok = list()
    godor = list()
    
    for i in melysegAdatok:
        if i == 0 and len(godor) == 0: continue
        elif i == 0 and len(godor) !=0:
            godrok.append(godor)
            godor = list()
        else:
            godor.append(i)
    
    with open("godrok.txt", "w") as file:
        for i in godrok:
            for j in i:    
                file.write(f"{j} ")
            file.write(f"\n")

    godrokSzama = len(godrok)
    return godrokSzama
            


elsoFeladat(melysegAdatok)

# 2. feladat
print("2, feladat")
tavolsagErtek = int(input("Adjon meg egy távolságértéket! "))
print(f"Ezen a helyen a felszín {melysegAdatok[tavolsagErtek - 1]} méter mélyen van.\n")

# 3. feladat
print("3. feladat")
harmadikFeladat(melysegAdatok)

# 4. feladat
negyedikFeladat(melysegAdatok)

# 5. feladat:
print("5. feladat")
print(f"A gödrök száma: {negyedikFeladat(melysegAdatok)}\n")

# 6. feladat a:
print("6. feladat")

if melysegAdatok[tavolsagErtek - 1] == 0:
    print("a)")   
    print("Az adott helyen nincs gödör.\n")
    
else:
    godorKezdete = tavolsagErtek - 1
    godorVege = tavolsagErtek - 1
    kezdet = True
    veg = True
    
    while kezdet or veg == True:
        
        if melysegAdatok[godorKezdete] != 0 and melysegAdatok[godorKezdete -1] != 0 : 
            godorKezdete -= 1
        else:
            kezdet = False
            
        if melysegAdatok[godorVege] != 0 and melysegAdatok[godorVege + 1] != 0: 
            godorVege += 1
        else:
            veg = False
            
    print("a)")     
    print(f"A gödör kezdete: {godorKezdete + 1} méter, a gödör vége: {godorVege + 1} méter.")

vizsgaltGodor = melysegAdatok[godorKezdete:godorVege + 1]

# 6. feladat b:

for i in vizsgaltGodor:
    elejetol 

# 6. feladat c:
print("c)")
print(f"A legnagyobb mélysége {max(vizsgaltGodor)} méter.")

# 6. feladat d:
terfogat = 0
for i in vizsgaltGodor:
    terfogat = (i * 1 *10) + terfogat
    
print("d)")
print(f"A térfogata {terfogat} m^3.")

# 6. feladat e:

vizmennyiseg = 0
for i in vizsgaltGodor:
    vizmennyiseg = ((i -1 ) * 1 *10) + vizmennyiseg

print(f"A vízmennyiség {vizmennyiseg} m^3.")
    
    
    



