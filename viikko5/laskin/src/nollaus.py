class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        self.sovellus.edellinen = self.sovellus.tulos
        self.sovellus.tulos = 0

    def kumoa(self):
        tmp = self.sovellus.edellinen
        self.sovellus.edellinen = self.sovellus.tulos
        self.sovellus.tulos = tmp
