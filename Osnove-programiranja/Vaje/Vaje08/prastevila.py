def je_prastevilo(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                 return False
        return True

def prastevila_na_intervalu():
    spodnja_meja = int(input("Vnesi spodnjo mejo intervala (večjo od 1): "))
    zgornja_meja = int(input("Vnesi zgornjo mejo intervala (večjo od 1): "))
    sez = []

    while spodnja_meja <= 1 or zgornja_meja <= 1:
        spodnja_meja = int(input("Vnesi spodnjo mejo intervala (večjo od 1): "))
        zgornja_meja = int(input("Vnesi zgornjo mejo intervala (večjo od 1): "))

    for i in range(spodnja_meja, zgornja_meja + 1):
        if je_prastevilo(i):
            sez.append(i)

    print(f"Praštevila na intervalu [{spodnja_meja}, {zgornja_meja}] so:", end=" ")

    for j in range(len(sez)):
        print(sez[j], end=" ")


prastevila_na_intervalu()