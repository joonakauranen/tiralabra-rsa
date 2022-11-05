# Määrittelydokumentti

Toteutetaan RSA-algoritmi. Mahdollisesti laajennetaan käyttämään SHA256-tiivistefunktiota. Projekti käyttää tekstikäyttöliittymää ja se ottaa syötteenä merkkijonon. Merkkijono voidaan salata ja purkaa RSA-algoritmia käyttäen. Mikäli aikaa riittää luodaan merkkijonosta ennen salausta tiiviste.

Käytän projektin toteutukseen Javaa. Hallitsen Pythonia riittävän hyvin, jotta voin vertaisarvioida kyseiselle kielellä toteutettuja projekteja.

Totetutan RSA-algoritmin ja Miller-Rabin algoritmin tarvittavien alkulukujen generointiin ja vahvistamiseen.

Valitsin RSA-algoritmin, koska olen kiinnostunut lohkoketjuista. Epäsymmetrinen salaus ratkaisee julkisiin lohkoketjuihin liittyvän salaukseen liittyvän ongelman. Ilman epäsymmetristä salausta ei voitaisi luoda julkisia kaikille näkyviä lompakoita. Toteutettava RSA-algoritmi havainnollistaa tätä toiminnallisuutta pienemmässä mittakaavassa.

Ohjelma saa syötteenä merkkijonon. Merkkijono salataan julkisella avaimella ja sen voi purkaa salatulla avaimella. Jos tiivistefunktio toteutetaan käytetään sitä merkkijonoon ennen salausta.

Aikavaativuuden osalta lähtökohta on, että julkisen avaimen operaatiot vievät O(n^2), salatun avaimen operaatiot O(n^3) ja alkulukujen ja avainten luonti O(n^4). Tämä tavoite on vain etukäteisarvio.

Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)

Dokumentaatiossa käytetty kieli: Suomi

Lähteet:

https://fi.wikipedia.org/wiki/RSA

https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

https://fi.wikipedia.org/wiki/Julkisen_avaimen_salaus

https://web.archive.org/web/20071112103441/http://www.rsa.com/rsalabs/node.asp?id=2215
