def pravo_geslo():
    geslo = "moje skrivno geslo"
    vneseno_geslo = input("Vpiši geslo: ")
    while geslo != vneseno_geslo:
        if vneseno_geslo == "":
            return
        vneseno_geslo = input("Vpiši geslo: ")
    return print("Dostop omogočen ...")

pravo_geslo()
input()

#Kako bi tu lahko uporabil break?? Uporabiš lahko while-else!!! Else se šteje kot del zanke!!