stevilo = int(input("Vpiši celo število: "))

def sodo_liho(n):
    if n <= 0:
        return print(f"Vpisano število mora biti večje od 0!")
    elif n % 2 == 0:
        return print(f"Število {n} je sodo.")
    return print(f"Število {n} je liho.")

def main():
    return sodo_liho(stevilo)

main()
input()