imena = ["admin", "alenka", "fanči", "lojze", "borut"]
gesla = ["12345", "moje komplicirano geslo", "fanči", "", "12%fdš #12?90*lkjSEF%&"]

def prijava():
    stevilo_napak = 0
    while stevilo_napak <= 5:
        upor_ime = input("Uporabniško ime: ")
        if upor_ime not in imena:
            stevilo_napak += 1
            print("Napačen uporabnik ali geslo!")
        elif upor_ime in imena:
            indeks = imena.index(upor_ime)
            geslo = input("Geslo: ")
            if geslo not in gesla:
                stevilo_napak += 1
                print("Napačen uporabnik ali geslo!")
            elif geslo == gesla[indeks]:
                return print("Prijava uspešna!")
    return print("Dostop zavrnjen, računalnik zaklenjen.")
            
prijava()