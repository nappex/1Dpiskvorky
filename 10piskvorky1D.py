from random import randrange


def vyhodnot(pole):
    if "xxx" in pole.lower():
        return "x"
    elif "ooo" in pole.lower():
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def tah_hrace(pole):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    while True:
        pozice = int(input("Zadej pozici na kterou chces hrat ? (0-19)\n"))

        if 0 <= pozice <= 19 and pole[pozice] == "-":
            pole = pole[:pozice]+"x"+pole[pozice+1:]
            return pole
        elif pole[pozice] == ("x" or "o"):
            print("Na této pozici už byl zahrán tah dříve.")
        else:
            print("Pozice symbolu je mimo hraci pole ! Znak pro hrani je x/o.")


def tah_pocitace(pole):
    while True:
        pozice = randrange(0, 20)

        if "x-x" in pole:
            pole = pole[:pole.index("x-x")+1]+"o"+pole[pole.index("x-x")+2:]
            return pole
        elif "-o" in pole:
            pole = pole[:pole.index("-o")]+"o"+pole[pole.index("-o")+1:]
            return pole
        elif "o-" in pole:
            pole = pole[:pole.index("o-")+1]+"o"+pole[pole.index("o-")+2:]
            return pole
        else:
            if pole[pozice] == "-":
                pole = pole[:pozice]+"o"+pole[pozice+1:]
                return pole


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
