import random

dobri_mozje = ["božiček", "dedek mraz", "miklavž"]

def nakljucni_moz(sez):
    return sez[random.randint(0,2)]

def zamenjaj_dobre_moze(datoteka):
    dat1 = open(datoteka, "r", encoding="utf-8")

    nakljucni_dobri_moz = nakljucni_moz(dobri_mozje)
    
    ime_datoteke = datoteka.split(".")[0]

    izhodna_datoteka = f"{ime_datoteke} - {nakljucni_dobri_moz}.txt"

    dat2 = open(izhodna_datoteka, "w", encoding="utf-8")
    
    for vrstica in dat1:
        nova_vrstica = vrstica.lower()
        for moz in dobri_mozje:
            nova_vrstica = nova_vrstica.replace(moz, nakljucni_dobri_moz)
        dat2.write(nova_vrstica.upper())

    dat1.close()
    dat2.close()

ime_datoteke = input("Vnesi ime datoteke: ")
zamenjaj_dobre_moze(ime_datoteke)