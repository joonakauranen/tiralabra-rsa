import AvainGeneroija as avaingeneroija

#testi

class Kayttoliittyma:
    def __init__(self):
        self.avain_generoija = avaingeneroija.AvainGeneroija()

    def kaynnista(self):       
        print("***RSA-salaus***")
        salattava_merkkijono = input("Syötä salattava merkkijono:")
