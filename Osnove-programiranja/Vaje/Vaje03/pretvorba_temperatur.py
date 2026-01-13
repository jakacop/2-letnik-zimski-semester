def pretvorba_v_fahrenheite(T):
    return T * (9/5) + 32

def pretvorba_v_celzije(T):
    return (T - 32) * (5/9)

def glavni_program():
    print("Izberi smer pretvorbe:")
    print("1. Celsius ---> Fahrenheit")
    print("2. Fahrenheit ---> Celsius")

    izbira = input("Vnesi 1 ali 2: ")

    if izbira == "1":
        temp_cels = float(input("Vnesi temperaturo v °C: "))
        fahrenheit = pretvorba_v_fahrenheite(temp_cels)
        print(f'{temp_cels:.2f} °C je {fahrenheit:.2f}, °F.')
        print(f'{temp_cels:.2f} °C je {(temp_cels - 273.15):.2f} °K.')
    
    elif izbira == "2":
        temp_fahr = float(input("Vnesi temperaturo v °F: "))
        celsius = pretvorba_v_celzije(temp_fahr)
        print(str(temp_fahr) + " °F je " + str(celsius) + " °C.")
        print(str(temp_fahr), "°F je " + str(celsius - 273.15) + " °K.")

    else:
        print("Neveljaven vnos.")

glavni_program()
input("Za konec pritisni 'Enter'!")