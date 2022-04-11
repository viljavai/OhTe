# Collatzin konjektuuri -visualisaattori
Sovelluksella käyttäjä voi tehdä visualisoinnin [Collatzin konjektuurista](https://fi.wikipedia.org/wiki/Collatzin_konjektuuri). Käyttäjä antaa luvun n ja kuvauksen parametrit kuten värit, sekä parametrit kuvaajan liikkeille. Ohjelma tekee kuvauksen luvuille (n,1) jolloin muodostuu puumainen rakenne. Kun luku n on pariton, kuvaaja kääntyy parametrien ilmaiseman astemäärän vasemmalle ja kun n on parillinen, kuvaaja kääntyy oikealle.
TEHTY visualisointi luvuille (n,..1).HUOM Kuvan generointi alkaa olemaan hyvin hidasta syötteillä (>10 000). Esimerkiksi syötteellä 11877 aikaa kului 2-3min, kun taas syötteellä 50 000 aikaa kului liki 30min.

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
`poetry run invoke coverage`
