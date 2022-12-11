# tiralabra-rsa

[Määrittelydokumentti](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/maarittelydokumentti.md)

[Testausdokumentti](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/testausdokumentti.md)

[Toteutusdokumentti](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/toteutusdokumentti.md)

## Viikkoraportit

[Viikko1](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/viikkoraportit/Viikkoraportti1.md)

[Viikko2](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/viikkoraportit/Viikkoraportti2.md)

[Viikko3](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/viikkoraportit/Viikkoraportti3.md)

[Viikko4](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/viikkoraportit/Viikkoraportti4.md)

[Viikko5](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/viikkoraportit/Viikkoraportti5.md)

[Viikko6](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/viikkoraportit/Viikkoraportti6.md)

## Käyttöohje

1. Kloona projekti
2. Asenna Poetry paikallisesti: ```pip install poetry```
3. Asenna riippuvuudet: ```poetry install```
4. Aja ohjelma: ```poetry run python3 tiralabra_rsa/```
  - syötteenä voi käyttää mitä tahansa merkkijonoja (tai numeroita, mutta ne käsitellään merkkijonoina)
  - syötteen kokoa rajoittaa luotavien avaimien ja moduluksen koko (syötteen tulee olla pienempi kuin modulus)
  - jos halutaan käsitellä suurempia syötteitä voidaan luoda suurempia avaimia
    - muuta ```alkuluku_generoija.eratostheneen_seula```-metodin kohta ```testattava_luku = random.getrandbits(10)``` 10 -> esim 512
5. Aja testit: ```poetry run pytest```
6. Aja Pylint ```poetry run pylint tiralabra_rsa```

Testikattavuusraportti myös alla.

## codecov

Alla olevaa codecov-merkkiä klikkaamalla uusimpaan testikattavuusraporttiin:

[![codecov](https://codecov.io/gh/joonakauranen/tiralabra-rsa/branch/main/graph/badge.svg?token=0Z1448E5ED)](https://codecov.io/gh/joonakauranen/tiralabra-rsa)
