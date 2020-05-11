from spillebrett import Spillebrett

def main():
    print("Hei, og velkommen til Game of Life!")
    rader = int(input("Hvor mange rader vil du aa starte med?\n"))
    kolonner = int(input("Og hvor mange kolonner vil du ha?\n"))
    skrrt = Spillebrett(rader, kolonner)
    skrrt.tegnBrett()
    print("Generasjon: " + str(skrrt.skrivGen()) + " - Antall levende celler: " + str(skrrt.finnAntallLevende()))
    svar = input("For aa see neste generasjon, trykk enter. For aa avslutte, trykk q: ")
    while svar != "q":
        skrrt.oppdatering()
        skrrt.tegnBrett()
        print("Generasjon: " + str(skrrt.skrivGen()) + " - Antall levende celler: " + str(skrrt.finnAntallLevende()))
        svar = input("For aa see neste generasjon, trykk enter. For aa avslutte, trykk q:\n")

main()
