import binascii

class StrIntStrMuuntaja():

    """
    Luokka toteuttaa metodit joilla voi muuttaa str -> int -> str
    """

    def merkkijono_kokonaisluvuksi(self, merkkijono):
        merkkijono = str(merkkijono)
        utf8 = merkkijono.encode(encoding = 'UTF-8')
        hexa = binascii.hexlify(utf8)
        kokonaisluku = int(hexa, 16)

        return kokonaisluku

    def kokonaisluku_merkkijonoksi(self, kokonaisluku):
        hexa = hex(kokonaisluku)
        hex_ilman_etuliitetta = hexa[2:]
        tavuina = bytes.fromhex(hex_ilman_etuliitetta)
        merkkijono = tavuina.decode('utf-8')

        return merkkijono
