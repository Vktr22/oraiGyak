import random

"""
Kérj be 1 páratlan számot a felhasználótól. (1 pont)
Amennyiben nem páratlan  számot ad meg a felhasználó,
akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)
"""
def feladat1():
    beker:int=int(input("Adj meg egy páratlan számot: "))
    while(beker%2==0):
        beker=int(input("Nem jó, kérlek, páratlan számot adj meg: "))

"""
Írass ki a konzolra 7 db  [5, 100] zárt intervallumba eső véletlen számot.
Hány 5-tel osztható van közöttük? A kiírás formátuma: „A számok között X db 5-mal osztható van!” 
"""
def feladat2():
    i:int=0
    oszthato5el:int=0
    while(i<7):
        random:int=random.random()*96+5
        print(random)
        if(random%5==0):
            oszthato5el+=1
        i+=1
    print(f"A számok között {oszthato5el} db 5-el osztható van.")

"""
Írj eljárást, mely paraméterként kap egy text szöveget, és egy betu betűt.
Számoljuk meg hány betu betű van a kapott szövegben?  
"""
def feladat3(text, betu):
    i:int=0
    while(i<len(text)):
        db:int=0
        if (text[i]==betu):
            db+=1
        i+=1
    print(f"A szövegben {db} db '{betu}' betű van.")

"""
Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja. 
Hány nevet adott meg a felhasználó?  
A kiírás formája: „A felhasználó 12 nevet adott meg.” 
"""
def feladat4():
    nevek=[]
    db:int=0
    nev=input("Diktálj nekem neveket, amennyiben végeztél, @+enter: ")
    while(nev!="@"):
        nevek.append(nev)
        db+=1
    print(f"A felhasználó {db} nevet adott meg.")

"""
Szimuláljuk a kő-papír-olló játékot.  
Írj eljárást, amiben:  
A felhasználótól bekérjük a tippjét, ami kő/papír/olló lehet.
Alakítsd át csupa kisbetűssé a szöveget, majd tárold el a felhasznalo_tippje változóban.  

Ezután a gép generál egy egész számot [1,3] között.
1- kő, 2- papír – 3 olló. Tárold el a gep_tippje változóban 

Ezután írd ki, hogy ki nyert! 
Ha a két szó ugyanaz, írja ki, hogy Döntetlen.  
Egyéb esetben azt írja ki, aki győzött! 

++ Ha valami más szót ad meg a felhasznló  a kő, papír, ollón kívül, akkor kérje be újra!
"""
def feladat5():
    felhaszntipp:str=input("Játszunk kő, papír, ollót!\nAddmeg a tipped(írj kő, papír, vagy ollót): ")
    felhaszntipp.lower()
    geptipp:str=""
    geptippSzama:int=random.random()*3+1
    if (geptippSzama==1):
        geptipp="kő"
        if(felhaszntipp=="kő"):
            print("Döntetlen")
        elif(felhaszntipp=="papír"):
            print("A felhasználó nyert!")
        else:
            print("A gép nyert!")
    elif (geptippSzama==2):
        geptipp="papír"
        if (felhaszntipp == "papír"):
            print("Döntetlen")
        elif (felhaszntipp == "olló"):
            print("A felhasználó nyert!")
        else:
            print("A gép nyert!")
    else:
        geptipp="olló"
        if (felhaszntipp == "olló"):
            print("Döntetlen")
        elif (felhaszntipp == "kő"):
            print("A felhasználó nyert!")
        else:
            print("A gép nyert!")
