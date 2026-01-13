import math

def obseg_kroga(r):
    return 2 * math.pi * r

def ploscina_kroga(r):
    return math.pi * (r ** 2)

radij = float(input("Vnesi radij kroga (v cm): "))

print("Obseg kroga je:", obseg_kroga(radij), "cm", "ploščina pa:", ploscina_kroga(radij), "cm^2.")

input("Za konec pritisni 'Enter'!")