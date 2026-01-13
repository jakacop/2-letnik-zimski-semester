import random

def odstrani_duplikate(sez):
    pomozni_seznam = []
    for znak in sez:
        if znak not in pomozni_seznam:
            pomozni_seznam.append(znak)
    return pomozni_seznam

def nakljucni_seznam(m, n, a, b):
    return [random.randint(a, b) for i in range(random.randint(m, n))]

print(odstrani_duplikate(nakljucni_seznam(10, 50, 1, 15)))