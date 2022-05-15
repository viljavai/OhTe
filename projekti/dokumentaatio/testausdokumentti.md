# Testausdokumentti
Ohjelman testaus rajoittuu matemaattiseen logiikkaan, sillä suuri osa ohjelmasta on vastuussa kuvaajan piirtämisestä. Vain Sovelluslogiikasta vastaavan Conjecture-luokan metodit testataan.
## Toiminnallisuudet
Ohjelmaan voi syöttää vain valideja numeroarvoja (positiivisia, ei merkkijonoja tai tyhjiä syötteitä). Syötettä on testattu manuaalisesti virheellisillä syötteillä. 
## Testauskattavuus
Käyttöliittymästä ja visualisoinnista vastaavia luokkia lukuunottamatta haarautumakattavuus on 79%.<br>
![testikattavuus](/projekti/dokumentaatio/kuvat/testikattavuus.png)<br>
## Asennus
Asennus ja toiminta on testattu kahdella eri linux-järjestelmällä. 
## Ongelmat
- Kun kuvaajan luo ensimmäistä kertaa, kuva piirtyy osittain ruudun ulkopuolelle, vasempaan reunaan. Bugi on helposti kierrettävissä painamalla "Create graph" nappia kahdesti.
