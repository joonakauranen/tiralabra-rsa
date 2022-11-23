import random

class AlkulukuGeneroija():

    """
    Generoi RSA-algoritmin tarvitsemat alkuluvut

    Tämä luokka luo tarvittavat alkuvut avaimen RSA-algoritimin käyttöön.
    """

    def __init__(self):
        alkuluku1 = 0
        alkuluku2 = 0
        self.pienet_alkuluvut = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541



    def luo_alkuluku(self):
        suuri_alkuluku = self.eratostheneen_seula()

    def eratostheneen_seula(self):

        while True:
            testattava_luku = random.getrandbits(10)

            if testattava_luku < 3 or testattava_luku % 2 == 0:
                break

            for luku in self.pienet_alkuluvut:
                if testattava_luku % luku == 0 and luku ** 2 <= testattava_luku:
                    break
        
            return testattava_luku

    def miller_rabin_algoritmi(self, suuri_alkuluku):

        if suuri_alkuluku < 3 or suuri_alkuluku % 2 == 0:
            self.eratostheneen_seula()

        

            

    
            
