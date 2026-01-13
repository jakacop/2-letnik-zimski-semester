import math

def obseg_kvadrata(a):
    return 4 * a

def ploscina_kvadrata(a):
    return a ** 2

def obseg_vcrtanega_kroga(a):
    return 2 * math.pi * (a / 2)

def obseg_ocrtanega_kroga(a):
    return 2 * math.pi * ((a * math.sqrt(2)) / 2)

def ploscina_vcrtanega_kroga(a):
    return math.pi * ((a/2) ** 2)

def ploscina_ocrtanega_kroga(a):
    return math.pi * (((a * math.sqrt(2)) / 2) ** 2)

stranica_kvadrata = float(input("Vpiši velikost stranice kvadrata: "))

def glavni_program():
    print(f'Obseg kvadrata s stranico {stranica_kvadrata:.2f}: {obseg_kvadrata(stranica_kvadrata):.2f}')
    print(f'Ploščina kvadrata s stranico {stranica_kvadrata:.2f}: {ploscina_kvadrata(stranica_kvadrata):.2f}')
    print(f'Obseg kvadratu včrtanega kroga: {obseg_vcrtanega_kroga(stranica_kvadrata):.2f}')
    print(f'Ploščina kvadratu včrtanega kroga: {ploscina_vcrtanega_kroga(stranica_kvadrata):.2f}')
    print(f'Obseg kvadratu očrtanega kroga: {obseg_ocrtanega_kroga(stranica_kvadrata):.2f}')
    print(f'Ploščina kvadratu očrtanega kroga: {ploscina_ocrtanega_kroga(stranica_kvadrata):.2f}')

glavni_program()
input("Za konec pritisni 'Enter'!")