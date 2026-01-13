def sestevanje_in_povprecje():
    vsota = 0
    stevec = 0
    stevilo = float(input("Vnesi število: "))
    while stevilo != 0:
        vsota += stevilo
        stevilo = float(input("Vnesi število: "))
        stevec += 1
    if stevec == 0:
        return print("Ni vpisanih števil.")
    else:
        povprecje = vsota / stevec
        return print(f"Vsota {stevec} števil je {vsota:.2f}, povprečje pa je {povprecje:.2f}.")

sestevanje_in_povprecje()
input()