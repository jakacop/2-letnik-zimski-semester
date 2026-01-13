pin = int(input("Vpiši PIN: "))

def glavni_program():
    if (pin % 2 == 0) and (999 < pin < 2000):
        return print(f"{pin} (Ana)")
    elif (pin % 5 == 0) and (1999 < pin < 2999):
        return print(f"{pin} (Ana)")
    return print(f"{pin}")

glavni_program()