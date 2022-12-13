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
