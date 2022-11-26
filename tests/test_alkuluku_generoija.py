import unittest
from tiralabra_rsa.alkuluku_generoija import AlkulukuGeneroija

class test_avain_generoija(unittest.TestCase):
    def setUp(self):
        self.alkulukugeneroija = AlkulukuGeneroija()

    def test_ei_hyvaksy_pienta_yhdistettya_lukua(self):
        hyvaksyttiinko = self.alkulukugeneroija.apufunktio(12)
        self.assertEqual(hyvaksyttiinko, 0)

    def test_ei_hyvaksy_suurta_yhdistettya_lukua(self):
        hyvaksyttiinko = self.alkulukugeneroija.apufunktio(1200000000000000000000000000000)
        self.assertEqual(hyvaksyttiinko, 0)
