import string
import random

def generator(n):
    abeceda = string.ascii_lowercase
    stevke = [i for i in range(10)]
    posebni = [".", ",", "!", "?", "*", "@", "$", ":"]
    geslo = ""
    for i in range(n // 5):
        nakljucna = random.randint(0, n)
        geslo += abeceda[nakljucna]
    return geslo

print(generator(20))