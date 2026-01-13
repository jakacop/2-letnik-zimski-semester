import random

def generiraj_st(n):
    return random.randrange(1, n + 1)

def preverba(n):
    return n.isdigit()

def igra(m, n):
    izmisljeno_st = generiraj_st(m)
    stevec = 0

    while stevec < n:
        poskus = input(f"{stevec + 1}/n Katero število sem si zamislil? ")

        if not preverba(poskus):
            print("Vpiši celo število med 1 in 100!")
            continue

        poskus = int(poskus)

        if poskus == izmisljeno_st:
            print(f"Bravo! Moje število je res {poskus}.")
            return
        elif poskus > izmisljeno_st:
            print(f"Moje število je manjše od {poskus}.")
        else:
            print(f"Moje število je večje od {poskus}.")

        stevec += 1

    print(f"Žal ti ni uspelo. Iskano število je {izmisljeno_st}.")

igra(100, 7)