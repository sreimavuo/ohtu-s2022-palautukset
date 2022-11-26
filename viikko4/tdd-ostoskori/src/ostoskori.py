from tuote import Tuote
from ostos import Ostos

""" Ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote. """
class Ostoskori:
    def __init__(self):
        self.ostokset = []

    """ Kertoo korissa olevien tavaroiden lukumäärän. """
    """ Eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2. """
    """ Samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2. """
    def tavaroita_korissa(self):
        tavaroita = 0

        for ostos in self.ostokset:
            tavaroita = tavaroita + ostos.lukumaara()

        return tavaroita

    """ Kertoo korissa olevien ostosten yhteenlasketun hinnan. """
    def hinta(self):
        hinta = 0

        for ostos in self.ostokset:
            hinta = hinta + ostos.hinta()

        return hinta

    """ Lisää tuotteen. """
    def lisaa_tuote(self, lisattava: Tuote):
        self.ostokset.append(Ostos(lisattava))

    """ Poistaa tuotteen. """
    def poista_tuote(self, poistettava: Tuote):
        pass

    """ Tyhjentää ostoskorin. """
    def tyhjenna(self):
        pass

    """ Palauttaa listan jossa on korissa olevat ostos-oliot. """
    """ Kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on. """
    def ostokset(self):
        pass
