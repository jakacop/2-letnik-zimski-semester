import random

dnevi_v_tednu = ["ponedeljek", "torek", "sreda", "četrtek", "petek", "sobota", "nedelja"]

def izbrani_dan():
    return dnevi_v_tednu[random.randrange(0,7)]

print(f"Izbrani dan v tednu je {izbrani_dan()}.")