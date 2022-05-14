# Arkkitehtuurikuvaus
## Pakkausrakenne
Ohjelma on jaettu kolmeen tiedostoon. Tiedosto UI vastaa käyttöliittymästä, visualisazion vastaa kuvaajan piirtoon liittyvästä koodista ja tiedostossa logic on matemaattisesta logiikasta vastaava koodi.<br>
![pakkausrakenne](/projekti/dokumentaatio/kuvat/pakkausrakenne.png)<br>
## Sovelluslogiikka
Sovelluksen luokkarakenne on melko yksinkertainen. Luokkien välillä käsitellään listaa, joka sisältää piirrettävät lukujonot.
Ensin luokassa Conjecture luodaan lukujono. Tämän jälkeen luotu jono syötetään luokalle Plotting. Luokka Ui kutsuu luokkaa
Conjecture, kun käyttäjä luo uuden kuvaajan.<br>
![luokkakaavio](/projekti/dokumentaatio/kuvat/luokkakaavio.png)
## Pysyväistallennus
Sovellus tallentaa luodun turtle-canvasin käyttäjän kotihakemistoon uniikilla nimellä. Nimi määritellään luokan Plotting save_image -metodissa.
## Sovelluksen toiminnallisuudet
Havainnollistetaan sovelluksen toimintaa sekvenssikaaviolla:<br>
![sekvenssikaavio](/projekti/dokumentaatio/kuvat/sekvenssikaavio.png)<br>
Lukujonojen luominen tapahtuu kolmen metodin kautta. Ensin Ui-luokan press-metodi antaa käyttäjäsyötteen Conjecture-luokan tree-metodille. Tree-metodi kutsuu metodia traverse luvuille (syöte,..,1). Traverse kutsuu metodia oper, joka antaa seuraavan luvun lukusarjassa konjektuurin sääntöjen mukaan. Saatu luku integer lisätään traverse-metodissa jonoon ja lopuksi jono lisätään superlistiin. Näin saadaan kaikki lista lukujonoista.<br>
![collatzkaavio](/projekti/dokumentaatio/kuvat/collatzkaavio.png)<br>
## Heikkoudet
Tällä hetkellä luokkarakenne ei ole tarpeeksi hajautettu. Sovelluksen rakenne pysyy yksinkertaisena, mutta luokkamuuttujia kertyy hyvin paljon. Tämän takia sovelluksen jatkokehitys nykyisessä muodossaan voi olla vaikeaa.
