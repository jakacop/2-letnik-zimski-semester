def sestavljalec():
    n = int(input("Vpiši n: "))
    sez = [i for i in range(n + 1)]
    print(sez)
    seznam_sodih = sez[::2]
    print(seznam_sodih)
    seznam_veckratnikov_3 = sez[::3]
    print(seznam_veckratnikov_3)
    zadnji_in_prvih_5 = sez[:6] + sez[-5:]
    print(zadnji_in_prvih_5)
    zaporednih_lihih = sez[5:16:2]
    print(zaporednih_lihih)

sestavljalec()