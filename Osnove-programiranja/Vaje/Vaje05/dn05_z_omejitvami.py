uporabnik1 = "admin"
uporabnik2 = "Jaka"
geslo1 = "1234"
geslo2 = "moje geslo"

def preverjanje_uporabnika():
    stevec_prijav = 0
    uporabnisko_ime = input("Vpiši uporabniško ime: ")

    if (uporabnisko_ime != uporabnik1) and (uporabnisko_ime != uporabnik2):
        return print("Uporabnik ne obstaja!")

    while stevec_prijav < 3:
        vpisano_geslo = input("Vpiši geslo: ")

        if (uporabnisko_ime == uporabnik1) and (vpisano_geslo == geslo1):
            return print("Prijava uspešna!")
        elif (uporabnisko_ime == uporabnik2) and (vpisano_geslo == geslo2):
            return print("Prijava uspešna!")
        else:
            stevec_prijav += 1
            if stevec_prijav < 3:
                print("Napačno geslo. Poskusi ponovno!")
            else:
                print("Napačno geslo, računalnik je zaklenjen. Več sreče prihodnjič!")

preverjanje_uporabnika()
input()