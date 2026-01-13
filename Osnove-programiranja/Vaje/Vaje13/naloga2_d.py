import csv

def branje_datotek(datoteka, zalozba):
    dat = open(datoteka, "r", encoding="utf-8")
    bralnik = csv.reader(dat, delimiter=";")
    sez = []
    for vrstica in bralnik:
        if zalozba in vrstica:
            sez.append(vrstica)

    return sez

print(branje_datotek("knjige.csv", "Cankarjeva založba"))