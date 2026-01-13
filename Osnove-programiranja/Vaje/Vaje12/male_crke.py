def pomanjsaj(vhod, izhod):
    dat1 = open(vhod, "r", encoding="utf-8")
    dat2 = open(izhod, "w", encoding="utf-8")
    vsebina = dat1.readlines()
    stevec = 1
    for vrstica in vsebina:
        vrstica = vrstica.lower()
        dat2.write(f"{stevec:3}: {vrstica}")
        stevec += 1
        
pomanjsaj("test.txt", "test-kopija-ostevilcena-pomanjsana.txt")