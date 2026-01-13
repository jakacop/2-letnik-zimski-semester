def stetje_samoglasnikov(niz):
    stevec = 0
    samoglasniki = ["a", "e", "i", "o", "u"]
    for znak in niz:
        if znak in samoglasniki:
            stevec += 1
    return stevec

print(stetje_samoglasnikov(input("Vnesi besedo: ")))