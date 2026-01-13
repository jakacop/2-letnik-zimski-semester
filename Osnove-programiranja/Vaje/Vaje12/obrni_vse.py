def obrni_datoteko(vhod, izhod):
    dat1 = open(vhod, "r", encoding="utf-8")
    dat2 = open(izhod, "w", encoding="utf-8")
    sez = []

    for vrstica in dat1:
        nova_vrstica = vrstica.strip()
        sez.append(nova_vrstica + "\n")

    sez[-1] = sez[-1].strip()

    for element in sez[::-1]:
        dat2.write(element[::-1])
    
    dat1.close()
    dat2.close()

obrni_datoteko("zabe.txt", "obrnjene_zabe_vse.txt")