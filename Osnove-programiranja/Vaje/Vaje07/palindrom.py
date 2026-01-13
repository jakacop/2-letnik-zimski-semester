palindromcic = input("Vnesi besedo ali frazo (za fraze glej samo tretjo vrstico)): ")

def palindrom():
    for i in range(len(palindromcic) // 2):
        if palindromcic[i] != palindromcic[-i - 1]:
            return False
    return True

def palindrom2():
    if palindromcic == palindromcic[::-1]:
        return True
    return False

def palindrom3():
    PALINDROMCIC = palindromcic.upper()
    sez = []
    for i in range(len(PALINDROMCIC)):
        if PALINDROMCIC[i] != " ":
            sez.append(PALINDROMCIC[i])

    for i in range(len(sez) // 2):
        if sez[i] != sez[-i - 1]:
            return False
    return True
    
print(palindrom())
print(palindrom2())
print(palindrom3()) #Kaj pa "perica reže raci rep" in velike začetnice ;) !?
input()