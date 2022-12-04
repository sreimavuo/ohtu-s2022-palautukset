class Erotus:
    def __init__(self, sovellus, lue_syote=0):
        self.sovellus = sovellus
        self.syote = lue_syote()

    def suorita(self):
        self.sovellus.tulos = self.sovellus.tulos - self.syote
