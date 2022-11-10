import random

class AvainGeneroija(object):

    """
    Generoi RSA-algoritmin tarvitsemat avaimet

    Tämä luokka luo julkisen ja salaisen avaimen RSA-algoritimin käyttöön.
    Avainten generointi perustuu suuriin alkulukuihin liittyvään matematiikkaan.
    """

    def __init__(self):

        #init-metodi on epäselvä ja keskeneräinen, selkeentyy kun integroidaan alkuluvut luovaan luokkaan ja RSA-luokkaan

        self.luo_avain()
        self.julkinen_avain = ''
        self.salattu_avain = ''
        self.alkulukujen_tulo
        self.euler = self.eulerin_pii_funktio(self.eka_alkuluku, self.toka_alkuluku)
        self.eka_alkuluku
        self.toka_alkuluku
        self.julkinen_eksponentti = self.maarita_julkinen_eksponentti()
        self.salattu_eksponentti = self.maarita_salattu_eksponentti(self.julkinen_eksponentti, self.euler)

    def luo_avain(self):
        #luo_avain-metodi on epäselvä ja keskeneräinen, selkeentyy kun integroidaan alkuluvut luovaan luokkaan ja RSA-luokkaan


        """
        Tätä metodia kutsumalla luodaan avaimet.

        Metodi kutsuu muita tarvittavia metodeita ja palauttaa avaimet.
        Tässä vaiheessa luokan metodit ovat erillisiä ja tässä asetataan ennalta määrätyt alkuluvut
        """

        self.eka_alkuluku = 17055899557196527525682810191339089909014331959812898993437334555169285087976951946809555356817674844913188193949144165887100694620944167618997411049745043243260854998720061941490491091205087788373487296637817044103762239946752241631032791287021875863785226376406279424552454153388492970310795447866569138481
        self.toka_alkuluku = 171994050316145327367864378293770397343246561147593187377005295591120640129800725892235968688434055779668692095961697434700708550594137135605048681344218643671046905252163983827396726536078773766353616572531688390937410451433665914394068509329532352022301339189851111636176939179510955519440490431177444857017
        self.alkulukujen_tulo = self.eka_alkuluku * self.toka_alkuluku
        
        
    def eulerin_pii_funktio(self, luku_a, luku_b):
        """
        Eulerin pii-funktio

        Laskee ja palauttaa Eulerin pii-funktion tuloksen
        """ 
        return (luku_a - 1) * (luku_b - 1)

    def etsi_suurin_yhteinen_tekija(self, luku_a, luku_b):
        """
        Metodi etsii suurimman yhteisen tekijän annetuille luvuille
        """

        while(luku_b):
            luku_a, luku_b = luku_b, luku_a % luku_b
        
        return luku_a

    def maarita_julkinen_eksponentti(self):
        """
        Metodi luo julkisen eksponentin RSA-algoritmin käyttöön

        Metodi tuottaa julkisen eksponentin, joka on kokonaisluku e,
        kun 1 < e < N jolle Eulerin luku on suhteellinen alkuluku.
        """
        suhteellinen_luku = self.euler

        julkinen_eksponentti = random.randint(2, suhteellinen_luku - 1)
        
        while self.etsi_suurin_yhteinen_tekija(suhteellinen_luku, julkinen_eksponentti) != 1:
            julkinen_eksponentti = random.randint(2, julkinen_eksponentti - 1)

        return julkinen_eksponentti

    def maarita_salattu_eksponentti(self, luku_a, luku_b):
        """
        Metodi luo salatun eksponentin RSA-algoritmin käyttöön

        Metodi valitsee salatan eksponentin d, siten, että d e ≡ 1 (mod Eulerin luku)
        """
 
        salattu_eksponentti = self.modul_kaanteisluku(luku_a, luku_b)

        return salattu_eksponentti

    def laajennettu_eukleideen_algoritmi(self, luku_a, luku_b):
        """
        Metodi toteuttaa laajennetun Eukleideen algoritmin

        Algoritmi laskee ja palauttaa suurimman yhteisen tekijän ja luvut, jotka yhdessä
        muuttujien luku_a ja luku_b kanssa toteuttavat Bezout'n yhtälön
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
        """
  
        g, x, y = self.laajennettu_eukleideen_algoritmi(e, m)
        assert g == 1

        if x < 0:
            x += m
        
        return x