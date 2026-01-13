def vracanje(datoteka):
    dat = open(datoteka, "r", encoding="utf-8")
    vsebina = dat.readlines()
    for vrstica in vsebina:
        print(vrstica.strip())

vracanje("zabe.txt")