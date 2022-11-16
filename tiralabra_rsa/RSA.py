from tiralabra_rsa.AvainGeneroija import AvainGeneroija

class RSA:
    def __init__(self):
        self.avain_generoija = AvainGeneroija()
        self.julkinen_avain = self.avain_generoija.hae_julkinen_avain()
        self.salattu_avain = self.avain_generoija.hae_salattu_avain()

    def salaa_merkkijono(self, merkkijono):
        julkinen_eksponentti, n = self.julkinen_avain

        salattu_merkkijono = (merkkijono ** julkinen_eksponentti) % n

        return salattu_merkkijono

    def pura_merkkijono(self, merkkijono):
        salattu_eksponentti, n = self.salattu_avain

        purettu_merkkijono = (merkkijono ** salattu_eksponentti) % n

        return purettu_merkkijono


