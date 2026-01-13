vneseno_stevilo = int(input("Vpiši sodo število med 10 in 50: "))

def posebno_stevilo():
    if (10 < vneseno_stevilo < 50) and (vneseno_stevilo % 2 == 0):
        return print(f"{vneseno_stevilo}")
    return print(f"Število {vneseno_stevilo} ni ustrezno!")

posebno_stevilo()