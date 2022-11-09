import AvainGeneroija as avaingeneroija


class Kayttoliittyma:
    def __init__(self):
        self.avain_generoija = avaingeneroija.AvainGeneroija()

    def kaynnista(self):       
        print("***RSA-salaus***")
        salattava_merkkijono = input("Syötä salattava merkkijono:")
        print(self.avain_generoija.alkulukujen_tulo)
