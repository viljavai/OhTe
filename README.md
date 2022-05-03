# Collatzin konjektuuri -visualisaattori
Sovelluksella käyttäjä voi tehdä visualisoinnin [Collatzin konjektuurista](https://fi.wikipedia.org/wiki/Collatzin_konjektuuri). Käyttäjä antaa luvun n ja kuvauksen parametrit kuten värit, sekä parametrit kuvaajan liikkeille. Ohjelma tekee kuvauksen luvuille (n,1) jolloin muodostuu puumainen rakenne. Kun luku n on pariton, kuvaaja kääntyy parametrien ilmaiseman astemäärän vasemmalle ja kun n on parillinen, kuvaaja kääntyy oikealle.

TEHTY<br>
- visualisointi luvuille (n,..1).HUOM Kuvan generointi alkaa olemaan hyvin hidasta syötteillä (>10 000). Esimerkiksi syötteellä 11877 aikaa kului 2-3min, kun taas syötteellä 50 000 aikaa kului liki 30min. 
- Kuvan voi tallentaa kotihakemistoon painamalla nappia "save graph". Kuva tallentuu .eps muodossa nimellä "my_collatz-(%m.%d.%Y-%H:%M:%S)".
- UIn kautta voi nyt antaa syötteen luvulle.
- *_HUOM!_*<br>
Tällä hetkellä UI on aika pahasti rikki, eikä kuvan tallennuskaan toimi. UI on työn alla.

## Dokumentaatio
- [Työaikakirjanpito](projekti/dokumentaatio/tyoaika.md)
- [changelog](projekti/dokumentaatio/changelog.md)

## Asennus
1. Asenna riippuvuudet
`poetry install`
2. Käynnistä sovellus
`poetry run invoke start`

## Testaus
Testien suoritus
`poetry run invoke test`\
Testikattavuus
`poetry run invoke coverage`\
Pylint
`poetry run invoke lint`
