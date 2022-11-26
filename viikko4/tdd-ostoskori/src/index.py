from tuote import Tuote
from ostos import Ostos
from ostoskori import Ostoskori

def main():
    kori = Ostoskori()
    maito = Tuote("Maito", 3)

    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(maito)

    ostokset = kori.ostokset()

    for ostos in ostokset:
        print(ostos.tuotteen_nimi())
    




if __name__ == "__main__":
    main()
