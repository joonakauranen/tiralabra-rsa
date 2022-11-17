import random

class AvainGeneroija():

    """
    Generoi RSA-algoritmin tarvitsemat avaimet

    Tämä luokka luo julkisen ja salaisen avaimen RSA-algoritimin käyttöön.
    Sekä julkinen että salattu avain koostuu kahdesta osasta,
    alkulukujen tulosta ja eksponenttiosasta
    """

    def __init__(self):

        self.luo_avain()
        self.julkinen_avain = 0
        self.salattu_avain = 0
        self.alkulukujen_tulo = 0
        self.euler = 0
        self.eka_alkuluku = 0
        self.toka_alkuluku = 0
        self.julkinen_eksponentti = 0
        self.salattu_eksponentti = 0

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
        self.salattu_eksponentti = self.maarita_salattu_eksponentti(self.julkinen_eksponentti,
                                                                    self.euler)
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

        while luku_b:
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

        ylaraja = suhteellinen_luku - 1
        julkinen_eksponentti = random.randint(2, ylaraja)

        while self.etsi_suurin_yhteinen_tekija(suhteellinen_luku, julkinen_eksponentti) != 1:
            julkinen_eksponentti = random.randint(2, ylaraja)

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

        _a = luku_a
        _b = luku_b

        old_s, _s = 1, 0
        old_t, _t = 0, 1

        while _b:
            _q = _a // _b
            _s, old_s = old_s - _q * _s, _s
            _t, old_t = old_t - _q * _t, _t
            _a, _b = _b, _a % _b

        return _a, old_s, old_t

    def modul_kaanteisluku(self, _e, _m):
        """
        Metodi tuottaa modulaariaritmetiikan käänteisluvun

        Argumentit:
            luku_a: kokonaisluku
            luku_b: kokonaisluku

        Palauttaa:
            Kokonaisluvun (int), joka on modulaariartimetiikan käänteisluku
        """

        _g, _x, _y = self.laajennettu_eukleideen_algoritmi(_e, _m)
        assert _g == 1

        if _x < 0:
            _x += _m

        return _x

    def hae_julkinen_avain(self):

        return self.julkinen_avain

    def hae_salattu_avain(self):

        return self.salattu_avain
