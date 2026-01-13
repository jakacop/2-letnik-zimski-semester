import csv

def branje_datotek(datoteka):
    dat = open(datoteka, "r", encoding="utf-8")
    bralnik = csv.reader(dat, delimiter=";")
    sez = []
    for vrstica in bralnik:
        sez.append(vrstica)
    return sez

print(branje_datotek("knjige.csv"))