# Testausdokumentti

### Yleistä

Tässä vaiheessa testaus koostuu yksikkötesteistä. Pohdin suorituskykytestien mielekkyyttä RSA-algoritmin tapauksessa. Algoritmin vaativin osa on modulaarinen eksponentio, jonka vaativuus on suhteellinen alkulukujen tuloon nähden. Tarkemmin ottaen alkulukujen ja niiden tulon kokoon biteissä. Alkulukujen koko taas on ennalta määrätty luku.

### Yksikkotestaus

Yksikkötestit suoritetaan osittain ennaltamäärättyjen lukujen perusteella. Testit on toteutettu osittain valmiita lukuja käyttäen, koska todelliseen toteutukseen liittyy sattumanvaraisuutta.

Yksikkötestit suoritetaan ohjelmallisesti käyttäen Pytest-testauskehystä, ja niiden kattavuus raportoidaan automaattisesti Codecov analyysityökalun avulla.



Kehitysympäristössä yksikkötestit suoritetaan GitHub Actionsin avulla. Muutoin testit voidaan toistaa seuraavasti:
- kloonaa projektin repositorio ```git clone https://github.com/joonakauranen/tiralabra-rsa.git```
- tarvittaessa asenna poetry ```pip install poetry```
- lisää projektin riippuvuudet ```poetry install```
- aja testit ```poetry run pytest```

### Testikattavuusraportti

![Alt text](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/kuvat/coverage-raportti.png)

### Integraatiotestaus

Integraatiotestausta on tehty vähäisissä määrin tekstikäyttöliittymän avulla. Salaus ja purku toimivat hyvin. On kuitenkin syytä huomioida, että syötteen tulee olla pienempi kuin alkulukujen tulon.
