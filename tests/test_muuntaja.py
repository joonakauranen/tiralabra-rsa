import unittest
from tiralabra_rsa.str_int_str_muuntaja import StrIntStrMuuntaja

class test_avain_generoija(unittest.TestCase):
    def setUp(self):
        self.muuntaja = StrIntStrMuuntaja()
    
    def test_muunnon_jalkeen_merkkijono_on_sama(self):
        alkuperainen = "muutettava"
        kokonaisluku = self.muuntaja.merkkijono_kokonaisluvuksi(alkuperainen)
        merkkijono = self.muuntaja.kokonaisluku_merkkijonoksi(kokonaisluku)
        self.assertEqual(merkkijono, alkuperainen)

    def test_muunnon_jalkeen_merkkijono_on_sama_erikoismerkkeja(self):
        alkuperainen = "gjoewjg904650981=)#Q(%#&)öäå"
        kokonaisluku = self.muuntaja.merkkijono_kokonaisluvuksi(alkuperainen)
        merkkijono = self.muuntaja.kokonaisluku_merkkijonoksi(kokonaisluku)
        self.assertEqual(merkkijono, alkuperainen)