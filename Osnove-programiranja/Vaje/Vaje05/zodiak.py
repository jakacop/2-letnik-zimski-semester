dan = int(input("Vpiši dan: "))
mesec = int(input("Vpiši mesec: "))

def zodiak(m, n):
    if (m >= 21 and n == 3) or (m <= 19 and n == 4):
        return print(f"Datum {m}. {n}. je v znamenju Ovna.")
    elif (m >= 20 and n == 4) or (m <= 20 and n == 5):
        return print(f"Datum {m}. {n}. je v znamenju Bika.")
    elif (m >= 21 and n == 5) or (m <= 20 and n == 6):
        return print(f"Datum {m}. {n}. je v znamenju Dvojčka.")
    elif (m >= 21 and n == 6) or (m <= 22 and n == 7):
        return print(f"Datum {m}. {n}. je v znamenju Raka.")
    elif (m >= 23 and n == 7) or (m <= 22 and n == 8):
        return print(f"Datum {m}. {n}. je v znamenju Leva.")
    elif (m >= 23 and n == 8) or (m <= 22 and n == 9):
        return print(f"Datum {m}. {n}. je v znamenju Device.")
    elif (m >= 23 and n == 9) or (m <= 23 and n == 10):
        return print(f"Datum {m}. {n}. je v znamenju Tehtnice.")
    elif (m >= 24 and n == 10) or (m <= 21 and n == 11):
        return print(f"Datum {m}. {n}. je v znamenju Škorpijona.")
    elif (m >= 22 and n == 11) or (m <= 21 and n == 12):
        return print(f"Datum {m}. {n}. je v znamenju Strelca.")
    elif (m >= 22 and n == 12) or (m <= 20 and n == 1):
        return print(f"Datum {m}. {n}. je v znamenju Kozoroga.")
    elif (m >= 21 and n == 1) or (m <= 18 and n == 2):
        return print(f"Datum {m}. {n}. je v znamenju Vodnarja.")
    elif (m >= 19 and n == 2) or (m <= 20 and n == 3):
        return print(f"Datum {m}. {n}. je v znamenju Ribe.")
    
def main():
    return zodiak(dan, mesec)

main()
input()