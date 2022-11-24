# Toteutusdokumentti

RSA-algoritmi perustuu suuriin alkulukuihin ja niiden ominaisuuksiin. Tätä myötä tämän projektin yleisrakennetta on mielekästä hahmotella toteutettujen matemaattisten algoritmien ja niiden Python-kielisten implementaatioiden näkökulmasta.

### Avainten luominen

1. Valitaan kaksi suurta erisuurta alkulukua satunnaisesti ja toisistaan riippumatta.
2. Lasketaan valittujen alkulukujen tulo. Tämä luku on algoritmin tarvitsema modulus tai vakio.
3. Valitaan kokonaisluku e, jolle toteutuu 1 < e < N jolle (p-1)(q-1) on suhteellinen alkuluku, kun N on kohdan 2. modulus ja p ja q kohdassa 1. valitut alkuluvut.
