import RSA as rsa

class Kayttoliittyma:

    """"
    RSA-algoritmia käyttävä tekstikäyttöliittymä

    Toimii käyttöliittymänä ohjelmaan, jolla voi salata merkkijonon ja purkaa aiemmin salatun merkkijonon,
    sekä luoda tähän tarvittavat salausavaimet
    """
    
    def __init__(self):
        self.rsa = rsa.RSA()

    def kaynnista(self):       
        print("***RSA-salaus***")
        salattava_merkkijono = int(input("Syötä salattava merkkijono:"))
        salattu_merkkijono = self.rsa.salaa_merkkijono(salattava_merkkijono)
        print(salattu_merkkijono)
        print("____________________")
        purettu_merkkijono = self.rsa.pura_merkkijono(salattu_merkkijono)
        print(purettu_merkkijono)
