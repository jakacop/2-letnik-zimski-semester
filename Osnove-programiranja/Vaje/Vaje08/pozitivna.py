def je_pozitivno_ali_nic(n):
    return n >= 0

def vpis_stevil():
    sez = []
    abs_seznam = []
    cel_seznam = []
    vneseno_stevilo = input("Vpiši število ali * za konec: ")
    while vneseno_stevilo != "*":
        vneseno_stevilo = float(vneseno_stevilo)
        sez.append(vneseno_stevilo)
        cel_seznam.append(round(vneseno_stevilo))
        if je_pozitivno_ali_nic(vneseno_stevilo):
            abs_seznam.append(vneseno_stevilo)
        else:
            abs_seznam.append(-vneseno_stevilo)
        vneseno_stevilo = input("Vpiši število ali * za konec: ")

    seznam_brez_nicel = [i for i in sez if i != 0]

    print(f"Seznam vpisanih števil: {sez}. Povprečje števil v seznamu je {sum(sez) / len(sez):.3f}")
    print(f"Seznam absolutnih vrednosti vpisanih števil: {abs_seznam}. Povprečje števil v seznamu je {sum(abs_seznam) / len(abs_seznam):.3f}")
    print(f"Seznam vpisanih števil, zaokrožen na cele vrednosti: {cel_seznam}. Povprečje števil v seznamu je {sum(cel_seznam) / len(cel_seznam):.3f}")
    print(f"Seznam vpisanih števil, razen ničel: {seznam_brez_nicel}. Povprečje števil v seznamu je {sum(seznam_brez_nicel) / len(seznam_brez_nicel):.3f}")

vpis_stevil()