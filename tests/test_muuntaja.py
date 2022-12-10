import unittest
from tiralabra_rsa.str_int_str_muuntaja import Str_int_str_muuntaja

class test_avain_generoija(unittest.TestCase):
    def setUp(self):
        self.muuntaja = Str_int_str_muuntaja()
    
    def test_muunnon_jalkeen_merkkijono_on_sama(self):
        alkuperainen = "muutettava"
        kokonaisluku = self.muuntaja.merkkijono_kokonaisluvuksi(alkuperainen)
        merkkijono = self.muuntaja.kokonaisluku_merkkijonoksi(kokonaisluku)
        self.assertEqual(merkkijono, alkuperainen)