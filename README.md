# Collatzin konjektuuri -visualisaattori
Sovelluksella käyttäjä voi tehdä visualisoinnin [Collatzin konjektuurista](https://fi.wikipedia.org/wiki/Collatzin_konjektuuri). Käyttäjä antaa luvun n ja kääntymiskulman. Kun luku n on parillinen, kuvaaja kääntyy parametrien ilmaiseman astemäärän oikealle ja kun n on pariton, kuvaaja kääntyy vasemmalle. Ohjelma tekee operaatiot ja kuvauksen luvuille (n,..,1) jolloin muodostuu puumainen rakenne. 
<br>
![esimerkki](/projekti/dokumentaatio/kuvat/esimerkki.png)

## Dokumentaatio
- [Vaatimusmäärittely](projekti/dokumentaatio/Vaatimusmaarittely.md)
- [Käyttöohje](projekti/dokumentaatio/kayttoohje.md)
- [Arkkitehtuuri](projekti/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](projekti/dokumentaatio/testausdokumentti.md)
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
`poetry run invoke coverage-report`\
Pylint
`poetry run invoke lint`
