class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.lukujono = []

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukujono.append(n)
            return True
        else:
            return False

    def poista(self, n):
        if n in self.lukujono:
            self.lukujono.remove(n)
            return True
        else:
            return False

    def kopioi_taulukko(self, a, b):
        b = a.copy()

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return self.lukujono

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()

        for i in a.to_int_list():
            x.lisaa(i)
        for i in b.to_int_list():
            x.lisaa(i)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()

        for i in [value for value in a.to_int_list() if value in b.to_int_list()]:
            y.lisaa(i)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()

        for i in [value for value in a.to_int_list() if value not in b.to_int_list()]:
            z.lisaa(i)

        return z

    def __str__(self):
        return f"{{{str(self.lukujono)[1:-1]}}}"
