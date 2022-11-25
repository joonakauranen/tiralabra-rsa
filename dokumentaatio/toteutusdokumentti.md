# Toteutusdokumentti

RSA-algoritmi perustuu suuriin alkulukuihin ja niiden matemaattisiin ominaisuuksiin. Tätä myötä tämän projektin yleisrakennetta on mielekästä hahmotella toteutettujen matemaattisten algoritmien ja niiden Python-kielisten implementaatioiden näkökulmasta.

RSA-algoritmin käyttöön täytyy siis ensimmäisenä luoda kaksi suurta alkulukua. Näistä alkuluvuista taas luodaan julkinen ja salattu avain. Nämä kaksi ensimmäistä vaihetta voidaan toteuttaa seuraavalla tavalla:

### Alkulukujen luominen

Ohjelmaan on tallennettu 100 ensimmäistä alkulukua. Näitä käyttäen voidaan selvittää onko luku yhdistetty luku. Yhdistetty luku on luku, joka on jaollinen myös muilla luvuilla kuin 1 ja itsellään. Toisin sanoen tällainen ei ole alkuluku. Tämä tarkastus voidaan suorittaa käyttäen Eratostheneen seulaa. Tähän ensimmäisen seulan syötteeksi luodaan sattumanvaraisia lukuja.

Jos sattumanvarainen luku läpäisee seulan on se potentiaalisesti tarvittava suuri alkuluku. Saatua potentiaalista lukua testataan edelleen Miller-Rabin-primaalisuustestillä. Toisin sanoen jälleen testataan onko luku yhdistetty luku. Yksi Miller-Rabin algoritmin iteraatio karsii yhdistetyt luvut pois 3/4 (täytyy vielä varmistaa tämä) todennäköisyydellä. Näin ollen yksi iteraatio ei riitä. Vakiintunut iteraatioiden määrä näyttää olevan 40. Mikäli luku läpäisee Miller-Rabin-testin iteraatiot oletamme, että se on alkuluku. 

### Avainten luominen

1. Valitaan yllä kuvatulla tavalla kaksi suurta erisuurta alkulukua satunnaisesti ja toisistaan riippumatta.
2. Lasketaan valittujen alkulukujen tulo. Tämä luku on algoritmin tarvitsema modulus tai vakio.
3. Valitaan kokonaisluku e, jolle toteutuu 1 < e < N jolle (p-1)(q-1) on suhteellinen alkuluku, kun N on kohdan 2. modulus ja p ja q kohdassa 1. valitut alkuluvut. Näin valittu e on RSA-algoritmin julkinen eksponentti
4. Valitaan kokonaisluku d siten, että d * e ≡ 1 (mod (p-1)(q-1)). Valittu e on RSA-algoritmin salainen eksponentti.

### Salaus ja purku

### Aikavaativuus

