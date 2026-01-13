temperatura = int(input("Vpiši temperaturo (°C): "))
tlak = float(input("Vpiši tlak (bar): "))

def alarm():
    if not ((40 <= temperatura <= 90) and (1.2 <= tlak <= 3.0)):
        return print(f"ALARM! Temperatura je {temperatura} °C in tlak {tlak} bara!")
    return None
    
alarm()