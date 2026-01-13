leto = int(input("Vpiši letnico: "))

def prestopno_leto(n):
    if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
        return print(f"Leto {n} je prestopno.")
    return print (f"Leto {n} ni prestopno.")

def main():
    return prestopno_leto(leto)

main()
input()