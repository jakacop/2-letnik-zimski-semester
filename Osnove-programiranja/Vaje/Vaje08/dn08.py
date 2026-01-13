imena = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fani", "Greta", "Hilda", "Iva", "Jana", "Kaja"]

tocke = [100, 56, 29, 68, 40, 50, 86, 100, 29, 100, 83]

najboljsi_dosezek = max(tocke)
najslabsi_dosezek = min(tocke)

def najboljsi(sez):
    dosezek = 0
    for i in range(len(sez)):
        if sez[i] > dosezek:
            dosezek = sez[i]
    return dosezek

def najslabsi(sez):
    dosezek = 100
    for i in range(len(sez)):
        if sez[i] < dosezek:
            dosezek = sez[i]
    return dosezek

def najboljse(sez):
    najvec_tock = []
    for i in range(len(sez)):
        if najboljsi(tocke) == tocke[i]:
            najvec_tock.append(sez[i])
    return najvec_tock

def najslabse(sez):
    najmanj_tock = []
    for i in range(len(sez)):
        if najslabsi(tocke) == tocke[i]:
            najmanj_tock.append(sez[i])
    return najmanj_tock

def st_negativnih(sez):
    stevec = 0
    for i in range(len(sez)):
        if sez[i] < 50:
            stevec += 1
    return stevec

def tocno_pol(sez, n):
    stevec = 0
    for i in range(len(sez)):
        if sez[i] == n:
            stevec += 1
    return stevec

def povprecje_pozitivnih(sez):
    pomozni_seznamcic = []
    for i in range(len(sez)):
        if sez[i] >= 50:
            pomozni_seznamcic.append(sez[i])
    return sum(pomozni_seznamcic) / len(pomozni_seznamcic)

def main(sez1, sez2):
    print(f"Največ točk, to je {najboljsi_dosezek} točk, so dosegle naslednje študentke:", end=" ")
    for ime in najboljse(imena):
        print(ime, end=" ")

    print()

    print(f"Najmanj točk, to je {najslabsi_dosezek} točk, so dosegle naslednje študentke:", end=" ")
    for ime in najslabse(imena):
        print(ime, end=" ")

    print()

    print(f"Izpit je pisalo {len(sez1)}, od tega {len(sez1) - st_negativnih(sez2)} pozitivno in {st_negativnih(sez2)} negativno.")

    print(f"Točno 50 točk je pisalo {tocno_pol(sez2, 50)} študentk.")

    print(f"Povprečje pozitivnih na izpitu {povprecje_pozitivnih(sez2):.2f}")

main(["Ana", "Berta", "Cilka", "Dani", "Ema", "Fani", "Greta", "Hilda", "Iva", "Jana", "Kaja"], [100, 56, 29, 68, 40, 50, 86, 100, 29, 100, 83])