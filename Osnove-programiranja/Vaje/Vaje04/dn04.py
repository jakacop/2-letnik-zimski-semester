letnica_rojstva = int(input("Vpiši letnico rojstva: "))
znesek = float(input("Vpiši skupen znesek nakupa (v EUR): "))
trenutno_leto = 2025

def desetodstotni_popust(n):
    return 0.9 * n

def cetrtinska_vrednost(n):
    return 0.25 * n

def glavni_program():
    print(f"Na nakup v vrednosti {znesek:.2f} EUR ste dobili 10 % popust, vaš račun znaša {desetodstotni_popust(znesek):.2f} EUR.")
    if trenutno_leto - letnica_rojstva >= 65:
        return print(f"Na varčevalni račun je bilo nakazano še {cetrtinska_vrednost(znesek):.2f} EUR."), print(f"Pri tem nakupu ste prihranili {(znesek - desetodstotni_popust(znesek) + cetrtinska_vrednost(znesek)):.2f}")
    elif (18 <= trenutno_leto - letnica_rojstva <= 27):
        return print(f"Na varčevalni račun je bilo nakazano še {cetrtinska_vrednost(znesek):.2f} EUR."), print(f"Pri tem nakupu ste prihranili {(znesek - desetodstotni_popust(znesek) + cetrtinska_vrednost(znesek)):.2f}")
    return print(f"Pri tem nakupu ste prihranili {znesek - desetodstotni_popust(znesek):.2f}")
    
glavni_program()