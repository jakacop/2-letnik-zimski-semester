def iso_datum(datum):
    return "".join(datum.split(".")[::-1])

def primerjaj(datum1, datum2):
    if iso_datum(datum1) == iso_datum(datum2):
        return 0
    elif iso_datum(datum1) < iso_datum(datum2):
        return -1
    return 1

def izpis_najvecjega(seznam_datumov):
    najmlajsi_datum = [".".join(datum.split(".")[::-1]) for datum in sorted([".".join(datum.split(".")[::-1]) for datum in seznam_datumov])][-1]
    print(f"Najnovejši datum je {najmlajsi_datum}.")

print(primerjaj("12.09.2025", "12.09.2024"))
izpis_najvecjega(['01.04.2025', '01.01.1955', '25.05.2000', '27.05.2025', '09.06.2025', '25.05.1968', '09.09.1999', '04.06.2025', '31.12.1999', '01.11.2011'])