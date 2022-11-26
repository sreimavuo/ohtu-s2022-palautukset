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
        if self.__onko_tuote_jo_korissa(lisattava):
            self.ostoslista[self.__tuotteen_indeksi(lisattava)].muuta_lukumaaraa(1)
        else:
            self.ostoslista.append(Ostos(lisattava))

    """ Poistaa tuotteen. """
    def poista_tuote(self, poistettava: Tuote):
        if self.__onko_viimeinen_tuote_korissa(poistettava):
            self.ostoslista.pop(self.__tuotteen_indeksi(poistettava))
        else:
            self.ostoslista[self.__tuotteen_indeksi(poistettava)].muuta_lukumaaraa(-1)

    """ Tyhjentää ostoskorin. """
    def tyhjenna(self):
        pass

    """ Palauttaa listan jossa on korissa olevat ostos-oliot. """
    """ Kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on. """
    def ostokset(self):
        return self.ostoslista

    """ Jos ostos löytyy ostoskorista, palauttaa indeksin, muuten palauttaa -1. """
    def __tuotteen_indeksi(self, lisattava: Tuote):
        indeksi = -1
        for i in range(0, len(self.ostoslista)):
            if self.ostoslista[i].tuotteen_nimi() is lisattava.nimi():
                indeksi = i

        return indeksi

    """ Tarkistaa löytyykö tuote jo ostoskorista. """
    def __onko_tuote_jo_korissa(self, lisattava: Tuote):
        for ostos in self.ostoslista:
            if ostos.tuotteen_nimi() is lisattava.nimi():
                return True
        
        return False

    """ Tarkistaa onko tuotetta vain 1kpl ostoskorissa. """
    def __onko_viimeinen_tuote_korissa(self, poistettava: Tuote):
        return False
