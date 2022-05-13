## Käyttöohje
Lataa viimeisin [release](https://github.com/viljavai/OhTe/releases)
# Käynnistys
1. Asenna riippuvuudet
`poetry install`
2. Käynnistä sovellus
`poetry run invoke start`
# Sovelluksen käyttäminen
1. Syötä luku kenttään "Give integer". Tämä luku määrittää mistä luvusta asti kuvaaja luodaan. Huomioi, 
että suurilla syötteillä (>5000) kuvaajan generointiin kuluu useampi sekunti. Yli 10 000 syötteillä aikaa kuluu yli minuutti. 
Jos annat epäpätevän syötteen, virheilmoitus näkyy komentorivillä.
2. Syötä kääntymisaste kenttään "Give angle of rotation". Tämä määrittää kuvaajan normitetun käännöskulman. 
Hyväksi havaittu vakiosyöte on 10 astetta. Suurilla kulmasyötteillä kuvaaja saattaa käpristyä kasaan. 
3. valitse haluatko luvut näkyväksi kuvaajaan. Suurilla lukuarvoilla kuvaaja saattaa näyttää sotkuiselta, 
mutta numeroilla pystyy havainnollistamaan erkanevien haarojen arvoja.
4. Kuvaaja piirtyy ruudulle ja komentoriville tulostuu generoitu lukusarja käyttäjäsyötteelle.
Jos kuvaaja ei näy ruudulla, koeta syöttää arvot uudelleen tai muuta kulmaparametrin arvoa. 
6. Kun kuvaaja on valmis, voit tallentaa sen kotihakemistoosi .eps-vektorigrafiikkana painamalla "Save graph" painiketta. 
Kuva tallentuu nimimuodossa "my_collatz-kk.pp.vvvv-tt:mm:ss". Huomioi, että suurilla syötteillä kuvan lataamisessa saattaa kulua hetki.
