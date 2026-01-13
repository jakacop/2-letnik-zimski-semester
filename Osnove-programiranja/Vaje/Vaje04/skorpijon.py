dan = int(input("Vpiši dan: "))
mesec = int(input("Vpiši mesec: "))

def glavni_program():
    if dan >= 23 and mesec == 10:
        return print(f"Tvoj rojstni dan je {dan}. {mesec}., to je v znamenju škorpijona.")
    elif dan <=21 and mesec == 11:
        return print(f"Tvoj rojstni dan je {dan}. {mesec}., to je v znamenju škorpijona.")
    return print(f"Tvoj rojstni dan je {dan}. {mesec}.")

glavni_program()