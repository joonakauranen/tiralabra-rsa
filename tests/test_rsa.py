import unittest
from tiralabra_rsa.RSA import RSA

class test_avain_generoija(unittest.TestCase):
    def setUp(self):
        self.rsa = RSA()
        self.rsa.julkinen_avain = (7, 77)
        self.rsa.salattu_avain = (43 ,77)
    
    def test_salaus_ja_purku_toimii(self):
        salattu = self.rsa.salaa_merkkijono(2)
        purettu = self.rsa.pura_merkkijono(salattu)
        self.assertEqual(purettu, 2)

    def test_salaus_toimii(self):
        salattu = self.rsa.salaa_merkkijono(2)
        self.assertAlmostEqual(salattu, 51)

    def test_purku_toimii(self):
        purettu = self.rsa.pura_merkkijono(51)
        self.assertAlmostEqual(purettu, 2)