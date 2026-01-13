def vracanje(datoteka):
    dat = open(datoteka, "r", encoding="utf-8")
    vsebina = dat.readlines()
    stevec = 1
    for vrstica in vsebina:
        print(f"{stevec:2}. {vrstica.strip():^30}")
        stevec += 1

vracanje("zabe.txt")