from varasto import the_varasto_olio
from pankki import the_pankki_olio
from viitegeneraattori import the_viitegeneraattori_olio
from ostoskori import Ostoskori


class Kauppa:
    def __init__(self, varasto=the_varasto_olio, pankki=the_pankki_olio, viitegeneraattori=the_viitegeneraattori_olio):
        self.varasto = varasto
        self.pankki = pankki
        self.viitegeneraattori = viitegeneraattori
        self._kaupan_tili = "33333-44455"

    def aloita_asiointi(self):
        self._ostoskori = Ostoskori()

    def poista_korista(self, id):
        tuote = self.varasto.hae_tuote(id)
        self._ostoskori.poista(tuote)
        self.varasto.palauta_varastoon(tuote)

    def lisaa_koriin(self, id):
        if self.varasto.saldo(id) > 0:
            tuote = self.varasto.hae_tuote(id)
            self._ostoskori.lisaa(tuote)
            self.varasto.ota_varastosta(tuote)

    def tilimaksu(self, nimi, tili_numero):
        viite = self.viitegeneraattori.uusi()
        summa = self._ostoskori.hinta()

        return self.pankki.tilisiirto(nimi, viite, tili_numero, self._kaupan_tili, summa)
