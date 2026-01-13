def je_prestopno(leto):
    if (leto % 400 == 0) or (leto % 4 == 0 and leto % 100 != 0):
        return True
    return False

prva_letnica = int(input("Vnesi prvo letnico: "))
druga_letnica = int(input("Vnesi drugo letnico: "))

def izpis_prestopnih_let():
    zacetek = prva_letnica
    konec = druga_letnica
    stevec = 0

    if prva_letnica > druga_letnica:
        zacetek = druga_letnica
        konec = prva_letnica

    for i in range(zacetek, konec + 1):
        if je_prestopno(i):
            stevec += 1
            print(i)
    return print(f"Med letoma {zacetek} in {konec} je {stevec} prestopnih let.")

izpis_prestopnih_let()
input()