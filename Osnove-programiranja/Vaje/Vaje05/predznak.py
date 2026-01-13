stevilo = float(input("Vnesi število: "))

def predznak_stevila(n):
    if n >= 0:
        return print(f"Število {n} je pozitivno število.")
    return print(f"Število {n} je negativno število.")

def main():
    return predznak_stevila(stevilo)

main()
input()