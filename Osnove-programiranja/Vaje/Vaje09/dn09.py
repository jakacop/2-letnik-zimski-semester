datumi = ['01.04.2025', '01.01.1955', '25.05.2000', '27.05.2025', '09.06.2025', '25.05.1968', '09.09.1999', '04.06.2025', '31.12.1999', '01.11.2011']

"""
def obracanje_datuma(datum):
    return ".".join(datum.split(".")[::-1])

def obracanje_datumov(seznam_datumov):
    return sorted([obracanje_datuma(datum) for datum in seznam_datumov])

def urejanje_datumov(seznam_datumov):
    print(sorted([".".join(datum.split(".")[::-1]) for datum in seznam_datumov]))
    print(sorted([".".join(datum.split(".")[::-1]) for datum in seznam_datumov])[1:-1])
"""

def urejanje_neobrnjenih_datumov(seznam_datumov):
    print(seznam_datumov)
    print([".".join(datum.split(".")[::-1]) for datum in sorted([".".join(datum.split(".")[::-1]) for datum in seznam_datumov])])
    print([".".join(datum.split(".")[::-1]) for datum in sorted([".".join(datum.split(".")[::-1]) for datum in seznam_datumov])][1:-1])

urejanje_neobrnjenih_datumov(['01.04.2025', '01.01.1955', '25.05.2000', '27.05.2025', '09.06.2025', '25.05.1968', '09.09.1999', '04.06.2025', '31.12.1999', '01.11.2011'])
input()