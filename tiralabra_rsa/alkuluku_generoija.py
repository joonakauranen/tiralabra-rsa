import random

class AlkulukuGeneroija():

    """
    Generoi RSA-algoritmin tarvitsemat alkuluvut

    Tämä luokka luo tarvittavat alkuvut avaimen RSA-algoritimin käyttöön.
    """

    def __init__(self):
        self.alkuluku1 = 0
        self.alkuluku2 = 0
        self.pienet_alkuluvut = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
        139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
        229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
        317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509,
        521, 523, 541)
        self.luo_alkuluvut()

    def luo_alkuluvut(self):
        alkuluku1 = self.luo_alkuluku()
        alkuluku2 = self.luo_alkuluku()

        while alkuluku2 == alkuluku1:
            alkuluku2 = self.luo_alkuluku()

        self.alkuluku1 = alkuluku1
        self.alkuluku2 = alkuluku2

    def luo_alkuluku(self):

        while True:
            testattava_luku = self.eratostheneen_seula()
            testattava_luku = self.miller_rabin_algoritmi(testattava_luku)
            if testattava_luku != 0:
                return testattava_luku

    def eratostheneen_seula(self):

        while True:

            testattava_luku = random.getrandbits(1000)

            if testattava_luku < 3 or testattava_luku % 2 == 0:
                continue

            for luku in self.pienet_alkuluvut:
                if testattava_luku % luku == 0 and luku ** 2 <= testattava_luku:
                    continue

            return testattava_luku

    def miller_rabin_algoritmi(self, suuri_alkuluku):

        if suuri_alkuluku < 3 or suuri_alkuluku % 2 == 0:
            return 0
        suuri_alkuluku = self.apufunktio(suuri_alkuluku)

        if suuri_alkuluku == 0:
            return 0

        return suuri_alkuluku

    def apufunktio(self, mahdollinen_alkuluku):
        _s = 0
        _d = mahdollinen_alkuluku-1

        while _d%2==0:
            _d>>=1
            _s+=1

            assert 2**_s * _d == mahdollinen_alkuluku-1

        return self.onko_yhdistetty_luku(mahdollinen_alkuluku, _d, _s)

    def onko_yhdistetty_luku(self, testattava_luku, _d, _s):
        for _ in range(10):
            ylaraja = testattava_luku - 1
            _a = random.randrange(2, ylaraja)
            _x = pow(_a, _d, testattava_luku)

            if _x == 1 or _x == testattava_luku - 1:
                continue

        for _ in range(_s):
            _x = pow(_x, 2, testattava_luku)
            if _x == testattava_luku - 1:
                break
        else:
            return 0

        return testattava_luku

    def hae_alkuluku1(self):
        return self.alkuluku1

    def hae_alkuluku2(self):
        return self.alkuluku2
