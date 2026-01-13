ime = input("Vpiši ime: ")

def glavni_program():
    print(f"{ime}")
    if (("a" in ime or "A" in ime) and (("e" in ime or "E" in ime) or ("i" in ime or "I" in ime))):
        return print(f"Ime {ime} vsebuje črko a in vsaj eno od črk e ali i.")
    
glavni_program()