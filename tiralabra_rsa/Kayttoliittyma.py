import AvainGeneroija as avaingeneroija

class Kayttoliittyma:

    """"
    RSA-algoritmia käyttävä tekstikäyttöliittymä

    Toimii käyttöliittymänä ohjelmaan, jolla voi salata merkkijonon ja purkaa aiemmin salatun merkkijonon,
    sekä luoda tähän tarvittavat salausavaimet
    """
    
    def __init__(self):
        self.avain_generoija = avaingeneroija.AvainGeneroija()

    def kaynnista(self):       
        print("***RSA-salaus***")
        salattava_merkkijono = input("Syötä salattava merkkijono:")
