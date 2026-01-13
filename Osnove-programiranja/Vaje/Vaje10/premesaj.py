import random

def zamenjaj_elementa(m, n, sez):
    temp = sez[m]
    sez[m] = sez[n]
    sez[n] = temp
    return sez

def premesaj_seznam():
    prvih_petdeset = [i for i in range(1, 51)]
    stevilo_premesanj = random.randrange(5, 101)
    stevec = 0
    while stevec <= stevilo_premesanj:
        zamenjaj_elementa(random.randrange(len(prvih_petdeset)), random.randrange(len(prvih_petdeset)), prvih_petdeset)
        stevec += 1
    return prvih_petdeset

print(premesaj_seznam())