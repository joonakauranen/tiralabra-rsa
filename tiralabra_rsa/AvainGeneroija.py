import random

class AvainGeneroija(object):

    def __init__(self):
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
        self.eka_alkuluku = 17055899557196527525682810191339089909014331959812898993437334555169285087976951946809555356817674844913188193949144165887100694620944167618997411049745043243260854998720061941490491091205087788373487296637817044103762239946752241631032791287021875863785226376406279424552454153388492970310795447866569138481
        self.toka_alkuluku = 171994050316145327367864378293770397343246561147593187377005295591120640129800725892235968688434055779668692095961697434700708550594137135605048681344218643671046905252163983827396726536078773766353616572531688390937410451433665914394068509329532352022301339189851111636176939179510955519440490431177444857017
        self.alkulukujen_tulo = self.eka_alkuluku * self.toka_alkuluku
        
        
    def eulerin_pii_funktio(self, luku_a, luku_b):
        return (luku_a - 1) * (luku_b - 1)

    def etsi_suurin_yhteinen_tekija(self, luku_a, luku_b):
        while(luku_b):
            luku_a, luku_b = luku_b, luku_a % luku_b
        
        return luku_a

    def maarita_julkinen_eksponentti(self):
        suhteellinen_luku = self.euler

        julkinen_eksponentti = random.randint(2, suhteellinen_luku - 1)
        
        while self.etsi_suurin_yhteinen_tekija(suhteellinen_luku, julkinen_eksponentti) != 1:
            julkinen_eksponentti = random.randint(2, julkinen_eksponentti - 1)

        return julkinen_eksponentti

    def maarita_salattu_eksponentti(self, luku_a, luku_b):
 
        salattu_eksponentti = self.modul_kaanteisluku(luku_a, luku_b)

        return salattu_eksponentti

    def laajennettu_eukleideen_algoritmi(self, luku_a, luku_b):
        
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
  
        g, x, y = self.laajennettu_eukleideen_algoritmi(e, m)
        assert g == 1

        if x < 0:
            x += m
        
        return x