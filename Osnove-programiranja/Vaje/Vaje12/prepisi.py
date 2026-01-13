def kopija(vhod, izhod):
    dat1 = open(vhod, "r", encoding="utf-8")
    dat2 = open(izhod, "w", encoding="utf-8")
    vsebina = dat1.read()
    dat2.write(vsebina)
    dat2.close()

kopija("test.txt", "test-kopija.txt")