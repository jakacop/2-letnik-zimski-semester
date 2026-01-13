def sestevanje_dveh_stevil(m, n):
    if (m + n) % 1 == 0:
        return int(m + n)
    return m + n

prvo_stevilo = float(input("Vnesi prvo število: "))
drugo_stevilo = float(input("Vnesi drugo število: "))

print(sestevanje_dveh_stevil(prvo_stevilo, drugo_stevilo))

input("Za konec pritisni 'Enter'!")