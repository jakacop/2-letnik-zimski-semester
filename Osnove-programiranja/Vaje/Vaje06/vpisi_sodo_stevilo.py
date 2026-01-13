def je_sodo(n):
    if n % 2 == 0:
        return True
    return False

def vpisi_sodo_stevilo():
    vpisano_stevilo = int(input("Vnesi sodo število: "))
    while not je_sodo(vpisano_stevilo):
        print("Vpisano število ni sodo!")
        vpisano_stevilo = int(input("Vnesi sodo število: "))
    return print(f"Vpisano število je {vpisano_stevilo}.")

vpisi_sodo_stevilo()
input()