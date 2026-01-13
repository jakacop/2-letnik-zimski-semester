def postevanka():
    stevilo = int(input("Vpiši pozitivno celo število: "))

    while stevilo <= 0:
        stevilo = int(input("Vpiši pozitivno celo število: "))
    
    for i in range(1, 11):
        postevanec = i * stevilo
        print(f"{i} x {stevilo} = {postevanec}")

    print()

    for i in range(1, stevilo + 1):
        inverzni_postevanec = i * stevilo
        print(f"{i} x {stevilo} = {inverzni_postevanec}")

def tezja_postevanka():
    stevilo = int(input("Vpiši pozitivno celo število: "))

    while stevilo <= 0:
        stevilo = int(input("Vpiši pozitivno celo število: "))

    stevec = 1
    zg_meja = 10
    while stevec <= zg_meja:
        postevanec = stevec * stevilo
        print(f"{stevec} x {stevilo} = {postevanec}")
        stevec += 1

    print()
    
    stevec2 = 1
    while stevec2 <= stevilo:
        inverzni_postevanec = stevec2 * stevilo
        print(f"{stevec2} x {stevilo} = {inverzni_postevanec}")
        stevec2 += 1

postevanka()
tezja_postevanka()
input()