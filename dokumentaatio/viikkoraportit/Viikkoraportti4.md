# Viikko3

Neljännellä viikolla RSA-algoritmin toiminta on saatu valmiiksi. Ohjelma luo suuret alkuluvut, niistä edelleen avaimet ja avaimien avulla voi salata syötteen. 

Kuten aiempinakin viikkoina opin jälleen lisää yksityiskohtia kryptografiasta ja RSA-algoritmista. Oli opettavaista implementoida vaiheiltaan melko

Epäselvyyttä aiheuttaa koodin suorituskyky. Vaikuttaa siltä, että modulaarinen eksponentio on nykyisellä toteutuksella erittäin hidas. Funktio on sinänsä hyvin yksinkertainen, mutta se voi olla laskennallisesti raskas. Täytyy tarkastaa onko Pythonissa tähän valmista metodia tai yrittää löytää tehokkaampi tapa muuten. Toki voi olla, että erittäin suurilla luvuilla kyseinen operaatio vain on niin raskas. Suorituskykytestejä taas pohdin siitä näkökulmasta, että RSA-algoritmin tapauksessa yksittäisten syötteiden koko ei välttämättä vaikuta aikavaativuuteen vaan se käsittääkseni perustuu alkulukujen summien kokoon bitteinä. Epävarma perusteluni tälle on se, että algoritmin vaativin osa on modulaarinen eksponentio, jonka vaativuus on suhteellinen alkulukujen tuloon nähden. Tarkemmin ottaen alkulukujen ja niiden tulon kokoon biteissä. **Onko niin, että koska alkulukujen koko biteissä on ennalta määrätty on myös algoritmin aikavaativuus/suoritusaika laskennallisesti vakio?** Jos näin on pohdin suorituskykytestien luomisen mielekkyyttä.

Projekti eteni viime viikon lopuksi tehdyn suunnitelman mukaan. Suunnitelmasta kohdat 1,3 ja 4 on toteutettu. Kohta 2 on osoittautunut tarpeettomaksi. Seuraavaksi siirrytään siis kohtaan 5.

1. Luodaan tekstikäyttöliittymä, joka ottaa syötteenä merkkijonon                 (alustava versio tehty)
2. Salaus ja purku jollain esimerkinomaisella tavalla                             (ei tehdä, tarpeeton)
3. Salaus ja purku valmiiksi luoduilla avaimilla                                  (alustava versio tehty)
4. Avaimien luonti etukäteen valituista alkuluvuista                              (alustava versio tehty)
5. Alkulukujen generointi, vahvistus ja niiden perusteella avaimien luominen
6. SHA256-funktion toteutus ja sen soveltaminen syötteenä olevaan merkkijonoon

Ensi viikolla on tarkoitus saada ohjelman ydintoiminta valmiiksi, eli koodataan, integroidaan ja testataan alkuluvut luova luokka. Viikon vaatimusten mukaisesti toteutusraportti aloitetaan ja testausdokumenttia laajennetaan. 

Käytetty aika: 9h
