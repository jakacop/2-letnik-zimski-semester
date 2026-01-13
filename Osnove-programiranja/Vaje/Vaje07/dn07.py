imena = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fani", "Greta", "Hilda", "Iva", "Jana", "Kaja"]

tocke = [98, 56, 89, 68, 40, 50, 86, 100, 29, 93, 83]

def najdaljsi_el(sez):
    max_dolz = 0
    for el in sez:
        dolzina = len(str(el))
        if dolzina > max_dolz:
            max_dolz = dolzina
    return max_dolz # Verjetno bi bilo veliko bolj enostavno s funkcijo max...!

najdaljse_ime = najdaljsi_el(imena)
najdaljse_tocke = najdaljsi_el(tocke)

def je_opravljen(n):
    return tocke[n] >= 50

def izpis():
    for i in range(len(imena)):
        if je_opravljen(i):
            print(f"{imena[i]:{najdaljse_ime}} ima {tocke[i]:{najdaljse_tocke}}, izpit opravljen.")
        else:
            print(f"{imena[i]:{najdaljse_ime}} ima {tocke[i]:{najdaljse_tocke}}, izpit ni opravljen.")

def povprecje():
    print()
    return print(f"Povprečno število doseženih točk je: {(sum(tocke) / len(tocke)):.2f}")

izpis()
povprecje()