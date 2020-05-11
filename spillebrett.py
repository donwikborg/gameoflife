from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner): #oppretter konstruktoeren
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = [] #oppretter rutenett
        for i in range(self._rader):
            self._rutenett.append([]) #oppretter en tom liste per rad
            for j in range(self._kolonner):
                self._rutenett[i].append(Celle()) #legger en celle inn i hver rute som opprettes basert paa antall kolonner
        self._generasjonsnummer = 0
        self._generer() #kaller paa generer for aa tilordne hver celle ny status

    def _generer(self): #for aa gi hver celle i rutenettet 1/3 sjanse til aa starte som levende
        for rad in self._rutenett:
            for celle in rad: #gaar gjennom alle cellene i rutenettet
                if randint(0,2) == 1: #gir hver celle 1/3 sjanse til aa leve
                    celle.settLevende() #setter status paa cellen til levende

    def tegnBrett(self): #metode for aa tegne brett
        for rad in range(len(self._rutenett)): #gaar gjennom radene
            skrivUt = "" #lager en tom tekststreng
            for kolonne in range(len(self._rutenett[rad])): #sjekker hver celle
                skrivUt += self._rutenett[rad][kolonne].hentStatusTegn() + "  " #legger til i tekststrengen og legger paa mellomrom for aa skrive ut mer kvadratisk
            print(skrivUt) #skriver ut rad for rad

    def finnNabo(self, rad, kolonne): #hentet fra gruppetime med tobias, men har skjoent den
        naboer = [] #starter med tom naboliste
        for j in range(-1,2): #range med -1, 0 og 1 fordi det er naboradene
            for i in range(-1,2): #samme som med rad, men for kolonner
                naboRad = rad + j
                naboKol = kolonne + i
                gyldig = True #setter alle til aa vaere gyldige i starten
                if naboRad == rad and naboKol == kolonne:
                    gyldig = False #luker ut den cellen vi er i, for den er ikke nabo til seg selv
                if naboRad >= self._rader or naboRad < 0:
                    gyldig = False #luker ut rader som ikke er i rutenettet
                if naboKol >= self._kolonner or naboKol < 0:
                    gyldig = False #luker ut kolonner som ikke er i rutenettet
                if gyldig:
                    naboer.append(self._rutenett[naboRad][naboKol]) #legger de aatte gyldige cellene inn i nabolisten
        return naboer

    def oppdatering(self): #metode for aa oppdatere brettet og bestemme hvilke celler som lever eller doer etter oppdateringen
        skalLeve = [] #oppretter en tom liste for cellene som skal leve videre
        skalDoe = [] #gjoer det samme for de som skal doe
        for rad in range(len(self._rutenett)): #gaar gjennom rutenettet
            for kolonne in range(len(self._rutenett[rad])):
                naboliste = self.finnNabo(rad,kolonne) #oppretter en naboliste til hver celle
                nabolever = [] #oppretter en foreloepig tom liste over naboceller som lever
                for cellen in naboliste: #gaar gjennom cellens naboliste
                    if cellen.erLevende(): #hvis cellen i nabolisten lever
                        nabolever.append(cellen) #saa legger vi cellen til i nabolever-listen
                if self._rutenett[rad][kolonne].erLevende() and (len(nabolever) == 2 or len(nabolever) == 3): #sjekker om cellen lever og om lengden paa nabolisten er 2 eller 3, jf reglene
                    skalLeve.append(self._rutenett[rad][kolonne]) #da skal cellen leve videre
                elif self._rutenett[rad][kolonne].erLevende() == False and len(nabolever) == 3: #hvis cellen er doed, maa den ha tre levende naboceller for aa leve
                    skalLeve.append(self._rutenett[rad][kolonne]) #og da skal cellen leve
                else:
                    skalDoe.append(self._rutenett[rad][kolonne]) #hvis cellen ikke passer med noen av if-sjekkene over, saa skal den legges i doedlisten
        for hvercelle in skalLeve: #gaar gjennom skalLeve-listen
            hvercelle.settLevende() #setter alle cellene i den til aa leve
        for hvercelle in skalDoe: #gjoer det samme med doedlisten
            hvercelle.settDoed()
        self._generasjonsnummer += 1

    def finnAntallLevende(self): #metode for aa hente ut antall levende celler
        w00pw00pCelleAlive = 0 #setter teller til 0
        for rad in self._rutenett: #gaar gjennom rutenettet
            for celle in rad:
                if celle.erLevende(): #hvis cellen har status som levende
                    w00pw00pCelleAlive +=1 #pluss paa 1 i telleren
        return w00pw00pCelleAlive #returnerer totalt antall levende celler



    def skrivGen(self): #for aa skrive ut generasjonsnummer. kunne sikkert laget den under tegnBrett, men, men.
        return self._generasjonsnummer
