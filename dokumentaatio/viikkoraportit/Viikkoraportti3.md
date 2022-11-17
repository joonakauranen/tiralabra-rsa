# Viikko3

Projektin pääasiallinen rakenne on muodostunut ja tarvittavat luokat luotu. Avaimet luova luokka on edistynyt toiminnallisuudeltaan eniten ja on lähes valmis. Luokka luo kahden alkuluvun perusteella julkisen ja salatun avaimen ja niiden tarvittavat eksponenttiosat. Suurin osa tämän viikon ajasta kului tämän toiminnallisuuden luomiseen. Pyrin ymmärtämään avainten luonnissa käytettävän matematiikkan ja sen jälkeen muuttamaan sen Python-koodin muotoon. Laajennetun Euklideen algoritmin ja modulaariaritmetiikan käänteisluvun osalta mallia on paljolti otettu netistä löytyneistä implementaatioista ja kirjastojen valmiista koodista. Tämäkin luokka on vielä rakenteeltaan sekava ja tarkoitus on selkeyttää sitä samalla kun muita luokkia koodataan ja luokkia aletaan integroida yhteen. Eriyisesti init- ja luo_avaimet -metodit ovat keskeneräisiä, koska ei ole vielä selkeää miten ne toteutetaan suhteessa muihin luokkiin. Koin, että niiden korjaaminen siistiin, mutta väliaikaiseen muotoon ei ole täysin tarpeellista. Luokalle on kirjoitettu testit, testikattavuus 100%. Hieman sattumalta päädyin toteuttamaan 'test driven developmentia' kun sain testien ennaltamäärättyjä syötteitä tutkimalla luotua toimivat Bezout'n luvut tuottavan koodin. Testit paljastivat myös randomness-metodin tuottaman virheen, jonka myötä testit hajoavat välillä. Tätä ei ole vielä korjattu, mutta se on tiedossa.

Tarkemmin ottaen avainten luonnin osalta on toteutettu Eulerin pii-funktio, Euklideen algoritmi, laajennettu Euklideen algoritmi ja modulaariaritmetiikan käänteisluvun tuottava algoritmi. Muut luokat ovat alkutekijöissään. GitHub actions on konfiguroitu ja se tuottaa codecov-raportin. Docstrings-dokumentointi on aloitettu ja koodin laadun seuraamiseen käytän paikallisesti Pylancea. Pylance/Pyright lisätään GitHub actionsiin.

Tällä viikolla opin lisää yksityiskohtia kryptografiasta ja RSA-algoritmista. Opin käytettävää matematiikkaa ja ymmärsin miten julkinen avain ja salainen avain liittyvät toisiinsa matemaattisesti. Lisäksi yleisellä tasolla hieman tarkemmin miten salaus, purku ja allekirjoittaminen toimivat RSA:n tapauksessa. Matemaattikan muuttaminen koodiksi selkeytyi ideana. Kertaus pytestin, pylancen, codecovin, GitHub actionsin jne käytöstä oli tervetullutta.

Hieman epäselvyyttä on dokumentaation osalta. Nyt dokumentaatio on hyvin yleisluontoista eikä sisällä tietoa esim parametreistä tai siitä mitä metodit palauttavat. Tarkoitus on kuitenkin jatkossa alkaa käyttää jotain olemassaolevaa formaattia, esim [Googlen formaattia](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings)

Projekti eteni hieman eri tavalla kuin olin suunnitellut. Ensimmäisen viikon suunnitelmasta kohdat 1 ja 4 on toteutettu. Kohta 2 on osoittautumassa tarpeettomaksi, joten seuraavaksi on tarkoitus toteuttaa kohdat 3 ja 5. Kohta kolme kuitenkin siten, että algoritmi käyttää valituista alkuluvuista luotuja oikeita avaimia valmiiksi luotujen sijaan. Alkuperäinen suunnitelma toisen viikon jälkeen:

1. Luodaan tekstikäyttöliittymä, joka ottaa syötteenä merkkijonon                 (alustava versio tehty)
2. Salaus ja purku jollain esimerkinomaisella tavalla                             (ei tehdä, tarpeeton)
3. Salaus ja purku valmiiksi luoduilla avaimilla                                  (toteutetaan kohdassa 4 luotuja avaimia käyttäen)
4. Avaimien luonti etukäteen valituista alkuluvuista                              (alustava versio tehty)
5. Alkulukujen generointi, vahvistus ja niiden perusteella avaimien luominen
6. SHA256-funktion toteutus ja sen soveltaminen syötteenä olevaan merkkijonoon

Koodauksen lisäksi aikaa täytyy varata myös testausdokumentin ja Docstringsin tekoon. Lisäksi Pylance/Pyright konfikoroida GitHub actionsiin. Koodauksen osalta tavoite on, että salaus- ja purkutoiminnallisuudet on tehty ja testattu. Mahdollisesti myös alkulukujen generointi ja vahvistus ainakin aloitettu.

Käytetty aika: 14h
