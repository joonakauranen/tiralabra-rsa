# Viikko4

Neljännellä viikolla RSA-algoritmin toiminta on saatu valmiiksi. Ohjelma luo suuret alkuluvut, niistä edelleen avaimet ja avaimien avulla voi salata syötteen. 

Kuten aiempinakin viikkoina opin jälleen lisää yksityiskohtia kryptografiasta ja RSA-algoritmista. Oli hieman vaikeaa hahmottaa Miller-Rabin-algoritmin toimintaa, joten sen implementoiminen oli myös opettavaista. Rehellisyyden nimissä on syytä tuoda esiin, että kyseinen ja algoritmi ja muutama muu osa ohjelmasta on implementoitu jokseenkin mekaanisesti ja puutteellisella ymmärryksellä. Ajankäytön suunnittelu hieman epäonnistui tällä viikolla. Oppina tästä, että dokumentaatioon ja testien tekemiseen tulee varata riittävästi aikaa kun tehtävä asia on monimutkainen eikä ennestään tuttu.

Epäselvyyttä aiheuttaa edelleen koodin suorituskyky. Tähän en kerennyt tällä viikolla palata. Vaikuttaa siltä, että modulaarinen eksponentio on nykyisellä toteutuksella erittäin hidas. Pythonin pow-funktio voi olla ratkaisu. Muiden luokkien testit osittain sisältävät alkulukujen luomista koskevat testit. Miller-Rabin-algoritmin osalta on testattu, että se ei hyväksy yhdistettyjä lukuja. Eratostheneen seulassa käytin while-looppia ja algoritmi ei palauta kuin oikeita lukuja. Sen testaaminen on näin ollen haastavaa, täytyy refaktoroida koodia jos testaaminen on tarpeen. Miller-Rabin kyllä hylkää myös pienet yhdistetyt luvut. Seuraavaa viikkoa varten voisin kuitenkin kysyä asiasta, joka oli Labtool-palautteessakin mainittu, eli **miten alkulukujen luontia kannattaa testata? Lisäksi mikä yleisemmin tämän projektin ja kurssin tapauksessa voisi olla "suorituskyky- tai muuta aiheeseen sopivaa testausta"?**

Projekti on edennyt alkuperäisen suunnitelman mukaan. Suunnitelmasta kohdat 1,3, 4 ja 5 on toteutettu. Kohta 2 on osoittautunut tarpeettomaksi. Dokumentaation ja testauksen osalta projekti ei ole edennyt yhtä hyvin.

1. Luodaan tekstikäyttöliittymä, joka ottaa syötteenä merkkijonon                 (alustava versio tehty)
2. Salaus ja purku jollain esimerkinomaisella tavalla                             (ei tehdä, tarpeeton)
3. Salaus ja purku valmiiksi luoduilla avaimilla                                  (alustava versio tehty)
4. Avaimien luonti etukäteen valituista alkuluvuista                              (alustava versio tehty)
5. Alkulukujen generointi, vahvistus ja niiden perusteella avaimien luominen      (alustava versio tehty)
6. SHA256-funktion toteutus ja sen soveltaminen syötteenä olevaan merkkijonoon    (tehdään jos jää aikaa)

Ohjelman keskeinen toiminnallisuus on valmista. Ajatus on, että parannuksien tekeminen tai sovelluksen laajentaminen käyttämään SHA256:ta ei ole prioriteetti. Sen sijaan keskitytään dokumentaatioon, testaukseen ja tuleviin vertaisarviointeihin. Aikavaativuuden analysointiin kulunee myös mahdollisesti reilustikin aikaa.

Käytetty aika: 13h
