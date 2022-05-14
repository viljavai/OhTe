# Arkkitehtuurikuvaus
## Pakkausrakenne
Ohjelma on jaettu kolmeen tiedostoon. Tiedosto UI vastaa käyttöliittymästä, visualisazion vastaa kuvaajan piirtoon liittyvästä koodista ja tiedostossa logic on matemaattisesta logiikasta vastaava koodi.<br>
![pakkausrakenne](/projekti/dokumentaatio/kuvat/pakkausrakenne.png)<br>
## Sovelluslogiikka
Sovelluksen luokkarakenne on melko yksinkertainen. Luokkien välillä käsitellään listaa, joka sisältää piirrettävät lukujonot.
Ensin luokassa Conjecture luodaan lukujono. Tämän jälkeen luotu jono syötetään luokalle Plotting. Luokka Ui kutsuu luokkaa
Conjecture, kun käyttäjä luo uuden kuvaajan.
![luokkakaavio](/projekti/dokumentaatio/kuvat/luokkakaavio.png)
## Pysyväistallennus
Sovellus tallentaa luodun turtle-canvasin käyttäjän kotihakemistoon uniikilla nimellä. Nimi määritellään luokan Plotting save_image -metodissa.
## Sovelluksen toiminnallisuudet
Havainnollistetaan sovelluksen toimintaa sekvenssikaaviolla:
![sekvenssikaavio](/projekti/dokumentaatio/kuvat/sekvenssikaavio.png)
