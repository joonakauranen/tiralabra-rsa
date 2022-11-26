# Viikko4

Neljännellä viikolla RSA-algoritmin toiminta on saatu valmiiksi. Ohjelma luo suuret alkuluvut, niistä edelleen avaimet ja avaimien avulla voi salata syötteen. 

Kuten aiempinakin viikkoina opin jälleen lisää yksityiskohtia kryptografiasta ja RSA-algoritmista. Oli hieman vaikeaa hahmottaa Miller-Rabin-algoritmin toimintaa, joten sen implementoiminen oli myös opettavaista. Rehellisyyden nimissä on syytä tuoda esiin, että kyseinen ja algoritmi ja muutama muu osa ohjelmasta on implementoitu jokseenkin mekaanisesti ja puutteellisella ymmärryksellä. Ajankäytön suunnittelu hieman epäonnistui tällä viikolla. Oppina tästä, että dokumentaatioon ja testien tekemiseen tulee varata riittävästi aikaa kun tehtävä asia on monimutkainen eikä ennestään tuttu.

Epäselvyyttä aiheuttaa edelleen koodin suorituskyky. Tähän en kerennyt tällä viikolla palata. Vaikuttaa siltä, että modulaarinen eksponentio on nykyisellä toteutuksella erittäin hidas. Pythonin pow-funktio voi olla ratkaisu. Alkuluvut luovan luokan yksilöllisempi testaus vaikuttaa myös haasteelta. Ohjelma kuitenkin vaikuttaa toimivan oikein ja alkuluvut luova luokka on integroitu muuhun ohjelmaan. Muiden luokkien testit siis tavallaan sisältävät alkulukujen luomista koskevat testit. Testikattavuusraportti näyttää lähes 100%, mutta testauksen voi silti sanoa olevan puutteellista. Seuraavaa viikkoa varten voisinkin kysyä apua asiaan, joka oli Labtool-palautteessakin mainittu, eli **miten alkulukujen luontia kannattaa testata? Lisäksi mikä yleisemmin tämän projektin ja kurssin tapauksessa voisi olla "suorituskyky- tai muuta aiheeseen sopivaa testausta"?**

Projekti on edennyt alkuperäisen suunnitelman mukaan. Suunnitelmasta kohdat 1,3, 4 ja 5 on toteutettu. Kohta 2 on osoittautunut tarpeettomaksi. Dokumentaation ja testauksen osalta projekti ei ole edennyt yhtä hyvin.

1. Luodaan tekstikäyttöliittymä, joka ottaa syötteenä merkkijonon                 (alustava versio tehty)
2. Salaus ja purku jollain esimerkinomaisella tavalla                             (ei tehdä, tarpeeton)
3. Salaus ja purku valmiiksi luoduilla avaimilla                                  (alustava versio tehty)
4. Avaimien luonti etukäteen valituista alkuluvuista                              (alustava versio tehty)
5. Alkulukujen generointi, vahvistus ja niiden perusteella avaimien luominen      (alustava versio tehty)
6. SHA256-funktion toteutus ja sen soveltaminen syötteenä olevaan merkkijonoon    (tehdään jos jää aikaa)

Ohjelman toiminnallisuus alkaa olla valmis tällaisenaan. Ajatus on, että parannuksien tekeminen keskeiseen toiminnallisuuteen tai sovelluksen laajennetaminen käyttämään SHA256:ta ei ole prioriteetti. Sen sijaan keskitytään dokumentaatioon, testaukseen ja tuleviin vertaisarviointeihin.

Käytetty aika: 13h
