import random

st_metov = int(input("Vnesi število metov: "))

def kocka(n):
    sez = [0 for i in range(6)]
    for i in range(n + 1):
        kocka = random.randrange(1, 7)
        sez[kocka - 1] += 1
    return sez

povprecje = st_metov / 6
rezultat = kocka(st_metov)
najmanj_pik = rezultat.index(min(rezultat)) + 1
najvec_pik = rezultat.index(max(rezultat)) + 1
odstop_od_povpr_minus = ((rezultat[najmanj_pik] - povprecje) / povprecje) * 100
odstop_od_povpr_plus = ((rezultat[najvec_pik] - povprecje) / povprecje) * 100
razlika = rezultat[najvec_pik] - rezultat[najmanj_pik]

print(f"Po {st_metov} metih smo dobili naslednje rezultate: \n Pike 1: {rezultat[0]} \n Pike 2: {rezultat[1]} \n Pike 3: {rezultat[2]} \n Pike 4: {rezultat[3]} \n Pike 5: {rezultat[4]} \n Pike 6: {rezultat[5]}")
print(f"V povprečju je vsako število pik padlo {povprecje:.2f}")
print(f"Najmanjkrat je padlo {najmanj_pik} pik ({rezultat[najmanj_pik]}, {odstop_od_povpr_minus:.2f} povprečja).")
print(f"Največkrat je padlo {najvec_pik} pik ({rezultat[najvec_pik]}, {odstop_od_povpr_plus:.2f} povprečja).")
print(f"Razlika med največ in najmanj je {razlika} ({(razlika / povprecje):.2f} povprečja).")