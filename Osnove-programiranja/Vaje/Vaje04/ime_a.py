ime = input("Vpiši ime: ")

def glavni_program():
    print(f"{ime}")
    if ("a" in ime) and ("e" or "i" in ime):
        return print(f"Ime {ime} vsebuje črko a in vsaj eno od črk e ali i.")
    
glavni_program()