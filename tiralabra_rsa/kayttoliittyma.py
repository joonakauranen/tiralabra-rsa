from tiralabra_rsa import rsa
from tiralabra_rsa import str_int_str_muuntaja

class Kayttoliittyma:

    """"
    RSA-algoritmia käyttävä tekstikäyttöliittymä

    Toimii käyttöliittymänä ohjelmaan, jolla voi salata merkkijonon ja purkaa aiemmin
    salatun merkkijonon, sekä luoda tähän tarvittavat salausavaimet
    """

    def __init__(self):
        self.rsa = rsa.RSA()
        self.muuntaja = str_int_str_muuntaja.StrIntStrMuuntaja()

    def kaynnista(self):
        print("***RSA-salaus***")
        while True:
            komento = input("Paina 'x' jos haluat lopettaa, mitä tahansa muuta jatkaaksesi")

            if komento == "x":
                break

            salattava_merkkijono = input("Syötä salattava merkkijono: ")
            merkkijono_koklukuna = self.muuntaja.merkkijono_kokonaisluvuksi(salattava_merkkijono)
            salattu_merkkijono = self.rsa.salaa_merkkijono(merkkijono_koklukuna)
            print("")
            print("Syöte salattuna:")
            print(salattu_merkkijono)
            print("")
            print("Syöte purettuna:")
            purettu_merkkijono = self.rsa.pura_merkkijono(salattu_merkkijono)
            purettu_merkkijono = self.muuntaja.kokonaisluku_merkkijonoksi(purettu_merkkijono)
            print(purettu_merkkijono)
            print("")
