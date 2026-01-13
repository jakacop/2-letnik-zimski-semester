def tip_knjige():
    knjiga = input("Vpiši ime datoteke: ")
    if knjiga[-3:] == "mp3":
        print(f"Naslov: {knjiga[:-4]}.")
        print(f"Format: {knjiga[-3:]}.")
        print("Knjiga je zvočna.")
    else:
        print(f"Naslov: {knjiga[:-4]}.")
        print(f"Format: {knjiga[-3:]}.")
        print("Knjiga je tekstovna.")

tip_knjige()