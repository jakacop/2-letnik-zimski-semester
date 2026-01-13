def kopija(vhod, izhod):
    dat1 = open(vhod, "r", encoding="utf-8")
    dat2 = open(izhod, "w", encoding="utf-8")
    vsebina = dat1.readlines()
    stevec = 1
    for vrstica in vsebina:
        dat2.write(f"{stevec:3}: {vrstica}")
        stevec += 1
        
kopija("test.txt", "test-kopija-ostevilcena.txt")