def razbijanje_besedila(n):
    besedilo = input("Vpiši besedilo: ")
    besedilo = besedilo.strip()

    """
    besedilo = besedilo.replace(".", "")
    besedilo = besedilo.replace(",", "")
    besedilo = besedilo.replace("!", "")
    besedilo = besedilo.replace("?", "")
    """

    for znak in ".,!?":
        besedilo = besedilo.replace(znak, "")

    besedilo = besedilo.split(" ")
    pomozni_seznam = [ime.lower() for ime in besedilo if len(ime) > n]
    
    print("Besede, daljše od treh znakov:", end=" ")
    for i in range(len(pomozni_seznam)):
        if len(pomozni_seznam[i]) > n:
            print(f"{pomozni_seznam[i]}", end=" ")

razbijanje_besedila(3)