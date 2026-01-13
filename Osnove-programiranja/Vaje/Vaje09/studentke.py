#imena = ["Ana", "Berta", "Cilka", "Dani", "Ema", "Fani", "Greta", "Hilda"]

def izpis_zacetnic(sez):
    pomozni_seznam = []
    pomozni_seznam_2 = []
    for ime in sez:
        zacetnica = ime[:1]
        zacetnica_2 = ime[:2]
        pomozni_seznam.append(zacetnica)
        pomozni_seznam_2.append(zacetnica_2)
    return print(pomozni_seznam), print(pomozni_seznam_2)

def tezji_izpis_zacetnic(sez):
    pomozni_seznam = []
    pomozni_seznam_2 = []
    for i in range(len(sez)):
        zacetnica = sez[i][:1]
        zacetnica_2 = sez[i][:2]
        pomozni_seznam.append(zacetnica)
        pomozni_seznam_2.append(zacetnica_2)
    return print(pomozni_seznam), print(pomozni_seznam_2)

izpis_zacetnic(["Ana", "Berta", "Cilka", "Dani", "Ema", "Fani", "Greta", "Hilda"])
tezji_izpis_zacetnic(["Ana", "Berta", "Cilka", "Dani", "Ema", "Fani", "Greta", "Hilda"])