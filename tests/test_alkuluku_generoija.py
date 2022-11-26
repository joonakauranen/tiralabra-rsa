import unittest
from tiralabra_rsa.alkuluku_generoija import AlkulukuGeneroija

class test_avain_generoija(unittest.TestCase):
    def setUp(self):
        self.alkulukugeneroija = AlkulukuGeneroija()

    def tunnistaa_yhdistetyn_luvun(self):
        hyvaksyttiinko = self.alkulukugeneroija.apufunktio(2)
        self.assertEquals(hyvaksyttiinko, 0)
