from tiralabra_rsa.AvainGeneroija import AvainGeneroija

class RSA:
    def __init__(self):
        self.avain_generoija = AvainGeneroija()
        self.julkinen_avain = self.avain_generoija.julkinen_avain
        self.salattu_avain = self.avain_generoija.salattu_avain
        self.julkinen_eksponentti = self.avain_generoija.julkinen_eksponentti
        self.salattu_eksponentti = self.avain_generoija.salattu_eksponentti


    