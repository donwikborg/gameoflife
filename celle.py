class Celle:
    def __init__(self): #oppretter konstruktoeren
        self._status = "doed" #cellen starter som doed

    def settDoed(self):
        self._status = "doed" #metode for aa "drepe" cellen

    def settLevende(self):
        self._status = "levende" #metode for aa gjore cellen levende

    def erLevende(self):
        if self._status == "levende": #hvis cellen lever
            return True #returner gyldig
        return False #hvis ikke returner ugyldig

    def hentStatusTegn(self):
        if self.erLevende(): #hvis cellen lever
            return "O" #returner bokstaven o
        return "." #returner punktum
