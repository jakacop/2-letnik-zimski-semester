sez = [10, 8, 5, 9, 6, 0, 10, 9, 5, 8, -3, 18, -11, -5, 20]

def izpis_s_presledki():
    print("Elementi seznama: ", end=" ")
    for element in sez:
        print(element, end=" ") #priveto skoči v novo vrstico! -- "\n"

def najmanjsi():
    print()
    najmanjsi = sez[0]
    for element in sez:
        if element < najmanjsi:
            najmanjsi = element
    return print(f"Najmanjši element seznama je: {najmanjsi}")

izpis_s_presledki()
najmanjsi()