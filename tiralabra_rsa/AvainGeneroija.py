import random

class AvainGeneroija(object):

    """
    Generoi RSA-algoritmin tarvitsemat avaimet

    Tämä luokka luo julkisen ja salaisen avaimen RSA-algoritimin käyttöön.
    Sekä julkinen että salattu avain koostuu kahdesta osasta, alkulukujen tulosta ja eksponenttiosasta
    """

    def __init__(self):

        #init-metodi on epäselvä ja keskeneräinen, selkeentyy kun integroidaan alkuluvut luovaan luokkaan ja RSA-luokkaan

        self.luo_avain()
        self.julkinen_avain
        self.salattu_avain
        self.alkulukujen_tulo
        self.euler
        self.eka_alkuluku
        self.toka_alkuluku
        self.julkinen_eksponentti
        self.salattu_eksponentti

    def luo_avain(self):

        """
        Tätä metodia kutsumalla luodaan avaimet.

        Metodi kutsuu muita tarvittavia metodeita ja määrittää avaimia kuvaavat luokkamuuttujat
        """

        self.eka_alkuluku = 7
        self.toka_alkuluku = 11
        self.alkulukujen_tulo = self.eka_alkuluku * self.toka_alkuluku

        self.euler = self.eulerin_pii_funktio(self.eka_alkuluku, self.toka_alkuluku)
        self.julkinen_eksponentti = self.maarita_julkinen_eksponentti()
        self.salattu_eksponentti = self.maarita_salattu_eksponentti(self.julkinen_eksponentti, self.euler)
        self.julkinen_avain = (self.julkinen_eksponentti, self.alkulukujen_tulo)
        self.salattu_avain = (self.salattu_eksponentti, self.alkulukujen_tulo)
        
    def eulerin_pii_funktio(self, luku_a, luku_b):
        """
        Eulerin pii-funktio

        Laskee ja palauttaa Eulerin pii-funktion tuloksen

        Argumentit:
            luku_a: ensimmäinen alkuluku
            luku_b: toinen alkuluku

        Palauttaa:
            Kokonaisluvun (int), joka on Eulerin pii-funktion tulos

        """ 
        return (luku_a - 1) * (luku_b - 1)

    def etsi_suurin_yhteinen_tekija(self, luku_a, luku_b):
        """
        Metodi etsii suurimman yhteisen tekijän annetuille luvuille

        Argumentit:
            luku_a: mikä tahansa kokonaisluku
            luku_b: mikä tahansa kokonaisluku

        Palauttaa:
            Kokonaisluvun (int), joka on kahden argumenttina annetun luvun suurin yhteinen tekijä
        """

        while(luku_b):
            luku_a, luku_b = luku_b, luku_a % luku_b
        
        return luku_a

    def maarita_julkinen_eksponentti(self):
        """
        Metodi luo julkisen eksponentin RSA-algoritmin käyttöön

        Metodi tuottaa julkisen eksponentin, joka on kokonaisluku e,
        kun 1 < e < N jolle Eulerin luku on suhteellinen alkuluku.

        Palauttaa:
            Kokonaisluvun (int), joka on julkisen avaimen eksponenttiosa
        """
        suhteellinen_luku = self.euler

        julkinen_eksponentti = random.randint(2, suhteellinen_luku - 1)
        
        while self.etsi_suurin_yhteinen_tekija(suhteellinen_luku, julkinen_eksponentti) != 1:
            julkinen_eksponentti = random.randint(2, julkinen_eksponentti - 1)

        return julkinen_eksponentti

    def maarita_salattu_eksponentti(self, luku_a, luku_b):
        """
        Metodi luo salatun eksponentin RSA-algoritmin käyttöön

        Metodi valitsee salatun eksponentin d, siten, että d e ≡ 1 (mod Eulerin luku)

        Argumentit:
            luku_a: kokonaisluku
            luku_b: kokonaisluku
        
        Palauttaa:
            Kokonaisluvun (int), joka on salatun avaimen eksponenttiosa
        """
 
        salattu_eksponentti = self.modul_kaanteisluku(luku_a, luku_b)

        return salattu_eksponentti

    def laajennettu_eukleideen_algoritmi(self, luku_a, luku_b):
        """
        Metodi toteuttaa laajennetun Eukleideen algoritmin

        Algoritmi laskee ja palauttaa suurimman yhteisen tekijän ja luvut, jotka yhdessä
        muuttujien luku_a ja luku_b kanssa toteuttavat Bezout'n yhtälön

        Argumentit:
            luku_a: kokonaisluku
            luku_b: kokonaisluku
        
        Palauttaa:
            Kokonaisluvun (int), joka on salatun avaimen eksponenttiosa
        """
        
        a = luku_a
        b = luku_b

        old_s, s = 1, 0
        old_t, t = 0, 1
        
        while b:
            q = a // b
            s, old_s = old_s - q * s, s
            t, old_t = old_t - q * t, t
            a, b = b, a % b
        
        return a, old_s, old_t

    def modul_kaanteisluku(self, e, m):
        """
        Metodi tuottaa modulaariaritmetiikan käänteisluvun

        Argumentit:
            luku_a: kokonaisluku
            luku_b: kokonaisluku
        
        Palauttaa:
            Kokonaisluvun (int), joka on modulaariartimetiikan käänteisluku
        """
  
        g, x, y = self.laajennettu_eukleideen_algoritmi(e, m)
        assert g == 1

        if x < 0:
            x += m
        
        return x

    def hae_julkinen_avain(self):
        return self.julkinen_avain
    
    def hae_salattu_avain(self):
        return self.salattu_avain