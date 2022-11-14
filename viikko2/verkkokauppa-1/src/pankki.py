from kirjanpito import the_kirjanpito_olio


class Pankki:
    def __init__(self, kirjanpito=the_kirjanpito_olio):
        self.kirjanpito = kirjanpito

    def tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        self.kirjanpito.lisaa_tapahtuma(
            f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        # täällä olisi koodi joka ottaa yhteyden pankin verkkorajapintaan
        return True

the_pankki_olio = Pankki()
