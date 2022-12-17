from tiralabra_rsa.avain_generoija import AvainGeneroija

class RSA:
    def __init__(self):
        self.avain_generoija = AvainGeneroija()
        self.julkinen_avain = self.avain_generoija.hae_julkinen_avain()
        self.salattu_avain = self.avain_generoija.hae_salattu_avain()

    def salaa_merkkijono(self, merkkijono):

        """
        Metodi salaa annetun merkkijonon käyttäen RSA-algoritmia

        Argumentit:
            merkkijono: merkkijono, joka salataan (testivaiheessa kokonaisluku)

        Palauttaa:
            Merkkijonon (str), joka on salattu käyttäen RSA-algortimia
        """

        julkinen_eksponentti, modulo = self.julkinen_avain

        #jätin oman ratkaisun näkyviin vaikka pythonin oma on nopeampi
        #salattu_merkkijono = (merkkijono ** julkinen_eksponentti) % modulo

        salattu_merkkijono = pow(merkkijono, julkinen_eksponentti, modulo)

        return salattu_merkkijono

    def pura_merkkijono(self, merkkijono):

        """
        Metodi purkaa aiemmin salatun merkkijonon käyttäen RSA-algoritmia

        Argumentit:
            merkkijono: merkkijono, joka puretaan (testivaiheessa kokonaisluku)

        Palauttaa:
            Merkkijonon (str), joka on purettu käyttäen RSA-algortimia
        """

        salattu_eksponentti, modulo = self.salattu_avain

        #jätin oman ratkaisun näkyviin vaikka pythonin oma on nopeampi
        #purettu_merkkijono = (merkkijono ** salattu_eksponentti) % modulo

        purettu_merkkijono = pow(merkkijono, salattu_eksponentti, modulo)

        return purettu_merkkijono
