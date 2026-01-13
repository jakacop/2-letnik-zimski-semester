import csv

def branje_datotek(datoteka):
    dat = open(datoteka, "r", encoding="utf-8")
    bralnik = csv.reader(dat, delimiter=";")
    sez = []
    for vrstica in bralnik:
        zalozba = vrstica[2]
        if zalozba not in sez:
            sez.append(zalozba)
    sez.sort()

    return sez

print(branje_datotek("knjige.csv"))