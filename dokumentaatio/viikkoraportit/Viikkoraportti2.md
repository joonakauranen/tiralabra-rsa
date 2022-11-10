# Viikko2

Ensimmäisen viikon nähdäkseni tärkein asia oli sopivan aiheen valinta ja sen yksityiskohdista keskustelu ohjaajan kanssa. Sopivan aiheen valinnan ja sen hyväksymisen jälkeen aloitin aiheeseen perehtymisen. Lisäksi tein GitHub-repositorion ja valmistelin ohjelmointiympäristön. Myös määrittelydokumentti on laadittu.

Ohjelma ei varsinaisen konkretian osalta ole edistynyt. Ainoastaan Poetry-projekti on luotu. Projektin luomisen ja tehdyn taustatyön myötä projektin koodaaminen voidaan aloittaa seuraavalla viikolla.

Opin yksityiskohtia kryptografiasta RSA-algoritmista tehdyn taustatyön myötä. Konseptitasolla uutta oli avainten luomisen prosessi ja esimerkiksi Miller-Rabin alkulukutesti. Mahdollisen SHA256-funktion toteutuksen tutkimisen yhteydessä opin, että RSA:ta ja SHA:ta voidaan käyttää yhdessä esim käyttötarkoituksiin, joissa tiedon muuttumattomuus halutaan todentaa pelkän tiivisteen perusteella.

Mielestäni tässä vaiheessa ei ole tullut vastaan epäselvyyksiä. Vaikeuksia tuotti gradle-projektin luominen ja pitkän tauon jälkeen tehty Gitin ja GitHubin synkronointi. Lopulta päädyin vielä viime hetkellä vaihtamaan ohjelmointikielen Pythoniin, koska sillä voidaan paremmin käsitellä hyvin suuria lukuja.

Projektin toteutuksen etenemistä olen koodauksen osalta hahmotellut seuraavalla tavalla:

1. Luodaan tekstikäyttöliittymä, joka ottaa syötteenä merkkijonon
2. Salaus ja purku jollain esimerkinomaisella tavalla
3. Salaus ja purku valmiiksi luoduilla avaimilla
4. Avaimien luonti etukäteen valituista alkuluvuista
5. Alkulukujen generointi, vahvistus ja niiden perusteella avaimien luominen
6. SHA256-funktion toteutus ja sen soveltaminen syötteenä olevaan merkkijonoon

Ensi viikon palautuksessa täytyy olla myös Javadocia, testausta, checkstyleä ja muuta, joten epäilen, että merkittävä osa ajasta kuluu myös näihin. Tavoite on, että koodi ja testaus kattavat ensi viikon jälkeen yllä mainituista kohdista kohdat 1-3.

Käytetty aika: 8h
