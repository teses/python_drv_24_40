

class Tier():

    def __init__(self):
        pass

    # abstrakte methode simuliert
    def laut_machen(self):
        raise TypeError("laut_machen() muss überschrieben werden")



class Hund(Tier):

    def laut_machen(self):
        print("Wau Wau")


class Katze(Tier):

    def laut_machen(self):
        print("Miau")


class Maus(Tier):
    pass


# normalerweise würde eine Klasse auch abstrakt sein müssen
# daher ist folgendes eigentlich nicht möglich
t = Tier()
#t.laut_machen()

####################################################

meine_katze = Katze()
meine_katze.laut_machen()

mein_hund = Hund()
mein_hund.laut_machen()

meine_maus = Maus()
meine_maus.laut_machen()
