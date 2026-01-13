def sestevanje_n_stevil(n):
    return (n * (n + 1) // 2)

def main():
    stevilo = int(input("Vpiši celo število: "))
    if stevilo <= 0:
        return print("Vpisano število mora biti večje od 0!")
    return print(sestevanje_n_stevil(stevilo))

main()
input()