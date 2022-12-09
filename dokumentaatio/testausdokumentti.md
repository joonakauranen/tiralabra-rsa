# Testausdokumentti

### Yleistä

Tässä vaiheessa testaus koostuu yksikkötesteistä.

### Yksikkotestaus

Yksikkötestit suoritetaan osittain ennaltamäärättyjen lukujen perusteella. Testit on toteutettu osittain valmiita lukuja käyttäen, koska todelliseen toteutukseen liittyy sattumanvaraisuutta.

Alkuluvut vahvistava testaus perustuu siihen, että käytettävät algoritmit pyrkivät tunnistamaan yhdistetyt luvut. Testatessa siis annetaan algoritmille yhdistettyjä lukuja ja oletetaan, että algoritmi ei niitä hyväksy. Näin myös tapahtuu luotujen testien tapauksessa.

Yksikkötestit suoritetaan ohjelmallisesti käyttäen Pytest-testauskehystä, ja niiden kattavuus raportoidaan automaattisesti Codecov analyysityökalun avulla.



Kehitysympäristössä yksikkötestit suoritetaan GitHub Actionsin avulla. Muutoin testit voidaan toistaa seuraavasti:
- kloonaa projektin repositorio ```git clone https://github.com/joonakauranen/tiralabra-rsa.git```
- tarvittaessa asenna poetry ```pip install poetry```
- lisää projektin riippuvuudet ```poetry install```
- aja testit ```poetry run pytest```

### Testikattavuusraportti

![Alt text](https://github.com/joonakauranen/tiralabra-rsa/blob/main/dokumentaatio/kuvat/coverage-raportti.png)

### Integraatiotestaus

Integraatiotestausta on tehty tekstikäyttöliittymän avulla. Salaus, purku sekä avainten että alkulukujen luominen toimivat hyvin.

### Miller-Rabinin testauksesta

Miller-Rabinin-algoritmia on testattu tuomalla testien käyttöön toinen [implementaatio](https://pypi.org/project/miller-rabin/). Testissä luodaan kymmenen satunnaista lukua ja tarkistetaan, että tämän projektin implementaation tulokset ovat yhteneväiset kirjaston algoritmin kanssa.

Tämän lisäksi testataan, että algoritmi hylkää suurten alkulukujen neliöt. Tähän on käytetty suuria [Mersennen lukuja](https://www.mersenne.org/primes/).

Yksinkertaisempia yksikkötestejä käytetään muun alkulukujen luomiseen liittyvän toiminnallisuuden testaamiseen.
