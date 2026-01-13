def vsota_stevk(stevilo):
    return sum([int(znak) for znak in str(stevilo)])

def preverba():
    stevilka = input("Vnesi število: ")
    while not stevilka.isdigit():
        stevilka = input("Vnesi število: ")
    return vsota_stevk(stevilka)

preverba()