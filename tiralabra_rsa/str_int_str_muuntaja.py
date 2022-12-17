import binascii
import codecs

class StrIntStrMuuntaja():

    """
    Luokka toteuttaa metodit joilla voi muuttaa str -> int -> str
    """

    def merkkijono_kokonaisluvuksi(self, merkkijono):
        """
        Metodi muuttaa merkkijonon kokonaisluvuksi, joka voidaan muuttaa
        takaisin merkkijonoksi

        Argumentit:
            merkkijono: merkkijono, joka muutetaan kokonaisluvuksi

        Palauttaa:
            Kokonaisluvun
        """
        merkkijono = str(merkkijono)
        utf8 = merkkijono.encode(encoding = 'UTF-8')
        hexa = binascii.hexlify(utf8)
        kokonaisluku = int(hexa, 16)

        return kokonaisluku

    def kokonaisluku_merkkijonoksi(self, kokonaisluku):
        """
        Metodi muuttaa kokonaisluvun merkkijonoksi

        Argumentit:
            kokonaisluku: kokonaisluku, joka on muutetaan takaisin alkuperäiseksi
            merkkijonoksi

        Palauttaa:
            Merkkijonon, joka on alkuperäinen merkkijono
        """
        hexa = hex(kokonaisluku)
        hex_ilman_etuliitetta = hexa[2:]
        print(hex_ilman_etuliitetta)
        hex_ilman_etuliitetta = hex_ilman_etuliitetta.strip()
        byt = codecs.decode(hex_ilman_etuliitetta,"hex")
        merkkijono = byt.decode('utf-8')

        return merkkijono
