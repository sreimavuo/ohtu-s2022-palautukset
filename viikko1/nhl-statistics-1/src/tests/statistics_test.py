import unittest
from statistics import Statistics
from statistics import SortBy
from player_reader import PlayerReaderStub


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_hae_pelaaja_loytyy(self):
        self.assertEqual(str(self.statistics.search("Kurri")), "Kurri EDM 37 + 53 = 90")

    def test_hae_pelaaja_ei_loydy(self):
        self.assertEqual(str(self.statistics.search("Pingu")), "None")

    def test_hae_tiimilla(self):
        self.assertEqual(str(self.statistics.team("PIT")[0]), "Lemieux PIT 45 + 54 = 99")

    def test_hae_parhaat(self):
        self.assertEqual(str(self.statistics.top(1)[0]), "Gretzky EDM 35 + 89 = 124")

    def test_hae_parhaat_maalit(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.GOALS)[0]), "Lemieux PIT 45 + 54 = 99")

    def test_hae_parhaat_syotot(self):
        self.assertEqual(str(self.statistics.top(1, SortBy.ASSISTS)[0]), "Gretzky EDM 35 + 89 = 124")
