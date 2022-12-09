import random
import unittest
import miller_rabin

from tiralabra_rsa.alkuluku_generoija import AlkulukuGeneroija

class test_avain_generoija(unittest.TestCase):
    def setUp(self):
        self.alkulukugeneroija = AlkulukuGeneroija()

    def test_miller_rabin_ei_hyvaksy_pienta_yhdistettya_lukua(self):
        hyvaksyttiinko = self.alkulukugeneroija.apufunktio(12)
        self.assertEqual(hyvaksyttiinko, 0)

    def test_miller_rabin_ei_hyvaksy_suurta_yhdistettya_lukua(self):
        hyvaksyttiinko = self.alkulukugeneroija.apufunktio(1200000000000000000000000000000)
        self.assertEqual(hyvaksyttiinko, 0)

    def test_miller_rabin_hyväksyy_oikeat(self):

        # Verrataan omaa toteutusta kirjaston toteutukseen

        for i in range(10):
            testattava_luku = random.getrandbits(512)
            
            if self.alkulukugeneroija.apufunktio(testattava_luku) == 0:
                oma_tulos = False
            else:
                oma_tulos = True

            miller_rabin_kirjaston_tulos = miller_rabin.miller_rabin(testattava_luku, 40)

            if oma_tulos != miller_rabin_kirjaston_tulos:
                tulos = False
                break
            else:
                tulos = True

        self.assertEqual(tulos, True)

    def miller_rabin_ei_hyvaksy_mersennen_luvun_neliota(self):
        # Mersennen luvut otettu täältä: https://www.mersenne.org/primes/

        mersennen_luku = 68647976601306097149819007990813932172694353001433054093944634591
        85543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151
        
        nelio = mersennen_luku * mersennen_luku

        tulos = self.alkulukugeneroija.apufunktio(nelio)

        self.assertEqual(tulos, 0)

        mersennen_luku = 531137992816767098689588206552468627329593117727031923199444138200403559860
        852242739162502265229285668889329486246501015346579337652707239409519978766587351943831270835393219031728127
        
        nelio = mersennen_luku * mersennen_luku

        tulos = self.alkulukugeneroija.apufunktio(nelio)

        self.assertEqual(tulos, 0)