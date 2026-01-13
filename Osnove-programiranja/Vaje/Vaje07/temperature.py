temperature_najvisje = [15, 14, 15, 8, 6, 9, 8]

def velikost_temperature():
    najnizja = temperature_najvisje[0]
    najvisja = temperature_najvisje[0]
    for element in temperature_najvisje:
        if element < najnizja:
            najnizja = element
        elif element > najvisja:
            najvisja = element
    return print(f"V prihodnjem tednu bo najnižja temperatura {najnizja} °C in najvišja {najvisja} °C.")

velikost_temperature()

dnevi_tedna = ["ponedeljek", "torek", "sreda", "četrtek", "petek", "sobota", "nedelja"]

def napoved():
    for i in range(len(dnevi_tedna)):
        print(f"{dnevi_tedna[i]}: {temperature_najvisje[i]}")
        
napoved()

temperature_najnizje = [4, 2, 6, -3, -5, 2, -1]

def temperaturne_razlike():
    indeks = 0
    najvisja_razlika = temperature_najvisje[0] - temperature_najnizje[0]
    for i in range(len(temperature_najnizje)):
        if temperature_najvisje[i] - temperature_najnizje[i] > najvisja_razlika:
            najvisja_razlika = temperature_najvisje[i] - temperature_najnizje[i]
            indeks += 1
    return print(f"Največja temperaturna razlika bo {najvisja_razlika} °C v {dnevi_tedna[indeks]}.")

temperaturne_razlike()

def zmrzal():
    sez = []
    for i in range(len(temperature_najnizje)):
        if temperature_najnizje[i] < 0:
            sez.append(i)

    print("Dnevi s temperaturo pod ničlo: ", end=" ")
    for i in sez:
        print(f"{dnevi_tedna[i]}", end=" ")

zmrzal()

input()