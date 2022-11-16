import unittest
from tiralabra_rsa.RSA import RSA

class test_avain_generoija(unittest.TestCase):
    def setUp(self):
        self.rsa = RSA()
        self.rsa.julkinen_avain = (13, 91)
        self.rsa.salattu_avain = (61 ,91)
        self.testi_luku = 2
    
    def test_salaus_ja_purku_toimii(self):
        salattu = self.rsa.salaa_merkkijono(2)
        print(salattu + 1)
        purettu = self.rsa.pura_merkkijono(salattu)
        self.assertEqual(purettu, 2)