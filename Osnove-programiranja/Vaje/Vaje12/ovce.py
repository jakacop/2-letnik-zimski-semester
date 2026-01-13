def ovce(vhod):
    dat = open(vhod, "r", encoding="utf-8")
    vsebina = dat.readlines()

    for vrstica in vsebina:
        print(vrstica.replace("rega", "rega, beee"), end="")

ovce("zabe.txt")