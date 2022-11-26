from tuote import Tuote
from ostos import Ostos

""" Ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote. """
class Ostoskori:
    def __init__(self):
        self.ostoslista = []

    """ Kertoo korissa olevien tavaroiden lukumäärän. """
    """ Eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2. """
    """ Samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2. """
    def tavaroita_korissa(self):
        tavaroita = 0

        for ostos in self.ostoslista:
            tavaroita = tavaroita + ostos.lukumaara()

        return tavaroita

    """ Kertoo korissa olevien ostosten yhteenlasketun hinnan. """
    def hinta(self):
        hinta = 0

        for ostos in self.ostoslista:
            hinta = hinta + ostos.hinta()

        return hinta

    """ Lisää tuotteen. """
    def lisaa_tuote(self, lisattava: Tuote):

        indeksi = -1
        for i in range(0, len(self.ostoslista)):
            if self.ostoslista[i].tuotteen_nimi() is lisattava.nimi():
                indeksi = i

        if indeksi == -1:
            self.ostoslista.append(Ostos(lisattava))
        else:
            self.ostoslista[indeksi].muuta_lukumaaraa(1)

    """ Poistaa tuotteen. """
    def poista_tuote(self, poistettava: Tuote):
        pass

    """ Tyhjentää ostoskorin. """
    def tyhjenna(self):
        pass

    """ Palauttaa listan jossa on korissa olevat ostos-oliot. """
    """ Kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on. """
    def ostokset(self):
        return self.ostoslista
