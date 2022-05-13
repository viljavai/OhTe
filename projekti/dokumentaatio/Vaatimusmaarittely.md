# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi luoda visualisoinnin Collatzin konjektuurista ja tallentaa saadun kuvan.
## Toiminnallisuus
- Käyttäjä voi syöttää sovellukseen luvun, mistä asti generoidaan kuvaaja luvuille n,n-1..1 noudattaen kaavaa n/2, jos n on parillinen ja 3n+1 jos n on pariton.
- Käyttäjä voi syöttää kääntymiskulman, jolloin kuvaaja kääntyy parillisen luvun kohdalla oikealle käyttäjäsyötteen verran. Parittomalla luvulla kulma on normitettu kääntymään 1,8*(syöte). Näin kuvaaja pysyy tasaisen muotoisena.
- Lopputuloksena piirretään puurakenne, jossa näkyy kaikkien lukujen (1,..,n) kuvaaja yhdessä kuvassa. 
- Käyttäjä voi valita kunkin lukujonon ensimmäiset luvut näkyväksi kuvaajaan.
- Kun kuvaaja on luotu, käyttäjä voi tallentaa kuvaajan .eps-formaatissa kotihakemistoon.
## Jatkokehitys
Sovellusta voisi kehittää vielä seuraavilla osa-alueilla:
- Graafisen käyttöliittymän kehittäminen kuten sliderit parametreille
- Reaaliaikainen kuvan luonti, jolloin parametreja muuttaessa näkisi välittömästi kuvan muutoksen. Tämänhetkisellä toteutuksella sovellus vaatii kuitenkin niin paljon laskentatehoa, että reaaliaikaiset parametrit vaatisivat ohjelman huomattavaa optimointia.
