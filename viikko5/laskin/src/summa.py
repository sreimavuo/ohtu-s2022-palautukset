class Summa:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.syote = lue_syote()

    def suorita(self):
        print(self.syote)
        self.sovellus.tulos = self.sovellus.tulos + self.syote
