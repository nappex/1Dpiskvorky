from random import randrange

symbol_hrac = "x"
symbol_pocitac = "o"


def vyhodnot(pole):
    if "xxx" in pole.lower():
        return "x"
    elif "ooo" in pole.lower():
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def tah(pole, pozice, symbol):
    pole = pole[:pozice]+symbol+pole[pozice+1:]
    return pole


def tah_hrace(pole):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    while True:
        pozice = int(input("Zadej pozici na kterou chces hrat ? (0-19)\n"))

        if 0 <= pozice <= 19 and pole[pozice] == "-":
            return tah(pole, pozice, symbol_hrac)
        elif pole[pozice] == symbol_hrac or pole[pozice] == symbol_pocitac:
            print("Na této pozici už byl zahrán tah dříve.")
        else:
            print("Pozice symbolu je mimo hraci pole !")


def tah_pocitace(pole):
    while True:
        pozice = randrange(0, 20)

        if "x-x" in pole:
            return tah(pole, pole.index("x-x")+1, symbol_pocitac)
        elif "-oo" in pole:
            return tah(pole, pole.index("-oo"), symbol_pocitac)
        elif "oo-" in pole:
            return tah(pole, pole.index("oo-")+2, symbol_pocitac)
        elif "o-o" in pole:
            return tah(pole, (pole.index("o-o")+1), symbol_pocitac)
        elif "-xx" in pole:
            return tah(pole, pole.index("-xx"), symbol_pocitac)
        elif "xx-" in pole:
            return tah(pole, pole.index("xx-")+2, symbol_pocitac)
        elif "-o-" in pole:
            return tah(pole, pole.index("-o-"), symbol_pocitac)
        elif "----" in pole:
            cislo = randrange(1, 4)
            return tah(pole, (pole.index("----")+cislo), symbol_pocitac)
        elif pole[pozice] == "-":
            return tah(pole, pozice, symbol_pocitac)


hraci_pole = "-"*20
stav = "-"
kolo = 0
print(kolo, ". kolo: ", hraci_pole, sep="")

while stav == "-":
    hraci_pole = tah_pocitace(hraci_pole)
    kolo += 1
    print("Tah pocitace:")
    print(kolo, ". kolo: ", hraci_pole, sep="")
    stav = vyhodnot(hraci_pole)
    if stav != "-":
        break
    hraci_pole = tah_hrace(hraci_pole)
    print("Tah hrace:")
    print(kolo, ". kolo: ", hraci_pole, sep="")
    stav = vyhodnot(hraci_pole)


if stav == "x":
    print("Vyhral hrac !")
    print(kolo, ". kolo: ", hraci_pole, sep="")
elif stav == "o":
    print("Vyhral pocitac !")
    print(kolo, ". kolo: ", hraci_pole, sep="")
else:
    print("Remiza !")
    print(kolo, ". kolo: ", hraci_pole, sep="")
