import unittest
from tiralabra_rsa.AvainGeneroija import AvainGeneroija

class test_avain_generoija(unittest.TestCase):
    def setUp(self):
        self.avaingeneroija = AvainGeneroija()
        self.avaingeneroija.eka_alkuluku = 7
        self.avaingeneroija.toka_alkuluku = 11
        self.avaingeneroija.alkulukujen_tulo = 77
        self.avaingeneroija.euler = 60
    
    def test_eulerin_pii_funktio_toimii(self):
        eulerin_pii = self.avaingeneroija.eulerin_pii_funktio(self.avaingeneroija.eka_alkuluku, self.avaingeneroija.toka_alkuluku)
        self.assertEqual(eulerin_pii, 60)

    def test_suurin_yhteinen_tekija_toimii(self):
        suurin_yhteinen_tekija = self.avaingeneroija.etsi_suurin_yhteinen_tekija(13, 17)
        self.assertEqual(suurin_yhteinen_tekija, 1)

    #testataan määrittyykö julkinen eksponentti siten, että sen ja eulerin pii-funktion suurin yhteinen tekijä on 1
    def test_julkinen_eksponentti_yhteinen_tekija_oikein(self):
        julkinen_eksponentti = self.avaingeneroija.maarita_julkinen_eksponentti()
        print(julkinen_eksponentti)
        suurin_yhteinen_tekija = self.avaingeneroija.etsi_suurin_yhteinen_tekija(julkinen_eksponentti, 72)
        self.assertEqual(suurin_yhteinen_tekija, 1)

    #yksi mahdollinen julkinen eksponentti on 13, käytetään sitä, jotta saadaan testitapaus pysymään muuttumattomana
    #tiedämme bezout'n lemman perusteella, että 61 on kelvollinen salattu eksponentti
    def test_salainen_eksponentti_oikein(self):
        julkinen_eksponentti = 7
        print(julkinen_eksponentti)
        salattu_eksponentti = self.avaingeneroija.maarita_salattu_eksponentti(julkinen_eksponentti, self.avaingeneroija.euler)
        self.assertEqual(salattu_eksponentti, 43)

    