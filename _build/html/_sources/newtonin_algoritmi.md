# Yhtälöiden ratkaisu numeerisesti

Numeeristen menetelmien avulla on mahdollista selvittää likimääräisiä ratkaisuja yhtälöille, joita on mahdotonta tai vaikeaa ratkaista muuten. Esimerkiksi kolmannen ja neljännen asteen polynomien nollakohtien ratkaisukaavat ovat hyvin monimutkaisia, ja viidennen ja korkeamman asteen polynomeille sellaisia ei ole olemassakaan. Tietokoneetkin ratkaisevat tällaisia ongelmia numeerisesti eli etsimällä luvun, joka toteuttaa ratkaistavan yhtälön riittävän hyvin. Tässä luvussa tarkastellaan erityisesti sitä, miten derivaattaa voi hyödyntää yhtälöiden ratkaisussa.

## Bolzanon lause

Lähtökohtana tämän luvun menetelmille on Bolzanon lause: jos jatkuvan funktion $f(x)$ arvo pisteessä $a$ on eri merkkinen kuin funktion $f(x)$ arvo pisteessä $b$, niin lukujen $a$ ja $b$ välissä on olemassa jokin piste $c$, jossa funktion arvo on $f(c)=0$. Toisin sanoen funktion arvot eivät voi muuttua positiivisista negatiivisiksi tai negatiivisista positiivisiksi ilman, että funktion arvo on välissä ainakin kerran nolla.

Bolzanon lauseesta on huomioitava seuraavaa:

- Funktiolla voi olla nollakohtia pisteiden $a$ ja $b$ välissä, vaikka funktion arvot olisivat saman merkkiset pisteissä $a$ ja $b$; esimerkiksi funktio $f(x)=x^2-9x+18$ saa saman merkkiset arvot pisteissä 2 ja 7 (sillä $f(2)=2^2-9\cdot 2+18=4 > 0$ ja $f(7)=7^2-9\cdot 7+18 = 4 > 0$), mutta funktiolla on kuitenkin tällä välillä kaksikin nollakohtaa $x=3$ ja $x=6$.

- Funktiolla, jonka arvot pisteissä $a$ ja $b$ ovat eri merkkiset, voi olla välillä $]a,b[$ useampi kuin yksi nollakohta. Esimerkiksi funktion $f(x)=x^3-6x^2+11x-6$ arvo pisteessä $x=0$ on $f(0)=-6 < 0 $ ja pisteessä $x=4$ arvo on $f(4)= 6 > 0$. Funktion nollakohdiksi voidaan ratkaista $x=1$, $x=2$ ja $x=3$.

Jos kuitenkin luvut $a$ ja $b$ ovat lähellä toisiaan ja funktion arvot $f(a)$ ja $f(b)$ ovat eri merkkiset, niin lukujen $a$ ja $b$ välistä löytyy varmasti eräs nollakohta funktiolle $f(x)$. Bolzanon lausetta voi yksinkertaisimmin käyttää nollakohdan etsimiseen haarukoimalla, eli laskemalla funktion arvot ensin pisteissä $a$ ja $b$ ja sitten pienentämällä lukujen väliä, kunnes saadaan riittävän tarkat rajat sille, minkä lukujen välissä funktion merkki vaihtuu.

::::{admonition} Esimerkki

Ratkaise yhtälö $3x^2-4x=5$ haarukoimalla lukujen -1 ja 0 välistä.

:::{admonition} Ratkaisu
:class: tip, dropdown

Muutetaan ensin yhtälö muotoon, jossa kyse on funktion nollakohdan ratkaisusta. Yhtälön voi kirjoittaa muodossa $3x^2-4x-5=0$, joten nollakohtaa etsitään funktiolle $f(x)=3x^2-4x-5$. Polynomifunktiona funktio $f(x)$ on jatkuva, joten Bolzanon lausetta voi käyttää.

Lasketaan ensin funktion arvot välin päätepisteissä: $f(-1)=2 > 0 $ ja $f(0)=-5 <0$. Arvot ovat eri merkkiset, joten ratkaisu löytyy annetulta väliltä.

Lasketaan funktion arvo välin päätepisteiden puolivälissä: $f(-0.5) = -2.25 < 0$. Arvo on eri merkkinen kuin pisteessä -1, joten voidaan päätellä, että nollakohta on lukujen -1 ja -0.5 välissä.

Lasketaan funktion arvo näiden lukujen puolivälissä: $f(-0.75) = -0.3125 < 0$. Funktion arvo on eri merkkinen kuin pisteessä -1, joten etsitään nollakohtaa pisteiden -1 ja -0.75 puolivälistä: $f(-0.875) \approx 0.797 > 0$.

Funktion arvot ovat pisteissä -1 ja -0.875 positiivisia, mutta pisteessä -0.75 arvo on negatiivinen, joten merkki vaihtuu pisteiden -0.875 ja -0.75 välissä. 

Lasketaan funktion arvo näiden pisteiden puolivälissä: $f(-0.8125) \approx 0.234 > 0$. Merkin muuttuminen tapahtuu siis pisteiden -0.8125 ja -0.75 välissä. 

Lasketaan jälleen funktion arvo pisteiden puolivälissä: $f(-0.78125) \approx -0.044 < 0$. Tästä seuraa, että nollakohdan sijainti tarkentuu välille $]-0.8125,-0.78125[$.

Välin puolivälissä funktion arvo on $f(-0.796875) \approx 0.093 >0 $; toisin sanoen nollakohdan tiedetään nyt sijaitsevan lukujen -0.78125 ja -0.796825 välissä.

Laskua voidaan jatkaa samaan tapaan niin pitkälle kuin halutaan. Laskimella nollakohdaksi saadaan noin -0.78630.
:::

::::

## Sekanttimenetelmä

Haarukointimenetelmää voidaan hieman jalostaa seuraavasti: muodostetaan pisteiden $f(a)$ ja $f(b)$ välille suora, ja ratkaistaan tämän suoran nollakohta. Tätä tapaa kutsutaan sekanttimenetelmäksi.

Suora muodostetaan pisteiden $(a,f(a))$ ja $(b,f(b))$ avulla, joten suoran kulmakerroin on

$k=\frac{f(b)-f(a)}{b-a}$

ja leikkausvakio on $v=f(b)-kb$

jolloin suoran yhtälöksi saadaan $y=kx+f(b)-kb$.

Oletetaan, että suora saa arvon 0 pisteessä $c$. Kun suoran yhtälöön asetetaan $y=0$ ja $x=c$, saadaan $c=\frac{kb-f(b)}{k}$ eli $c=b-\frac{f(b)}{k}$.

Sijoittamalla edelliseen yhtälöön $k=\frac{f(b)-f(a)}{b-a}$ saadaan lopulta nollakohdalle arvio

$c=b-\frac{b-a}{f(b)-f(a)} f(b)$.

Seuraava vaihe on laskea funktion arvo pisteessä $c$ja tarkastella sen merkkiä. Jos merkki on sama kuin pisteessä $a$, niin lähemmäs nollakohtaa päästään muodostamalla uusi suora pisteestä $(c,f(c))$ pisteeseen $(b,f(b))$. Jos taas merkki on vastakkainen kuin pisteessä $a$, niin uusi suora muodostetaan pisteiden $(a,f(a))$ ja $(c,f(c))$ välille.

## Newtonin menetelmä

Newtonin menetelmä perustuu edellä esitettyyn sekanttimenetelmään. Sekanttimenetelmällä pisteiden välillä piirretyn suoran kulmakerroin oli
$k=\frac{f(b)-f(a)}{b-a}$. Jos pisteet $a$ ja $b$ ovat hyvin lähellä toisiaan, niin kyseinen erotusosamäärä on melkein sama kuin funktion derivaatta $f'(b)$. Nyt suoran kulmakertoimeksi valitaankin siis funktion derivaatta pisteessä $b$:

$k=f'(b)$

ja edelleen leikkausvakio on $v=f(b)-f'(b)b$,

joten suoran yhtälöksi muodostuu $y=f'(b)x+f(b)-f'(b)b$.

Suoran nollakohta on $(c,0)$, joten $0=f'(b)c+f(b)-f'(b)b$, josta ratkaa

$c=b-\frac{f(b)}{f'(b)}$.

Newtonin menetelmässä valitaan luvulle $c$ jokin alkuarvaus $x_0$. Seuraava arvio nollakohdalle, $x_1$, saadaan laskemalla $x_1=x_0 - \frac{f(x_0)}{f'(x_0)}$. Yleisesti $n+1$:s arvio luvulle $c$ eli x_{n+1} saadaan edellisen arvion $x_n$ perusteella:

$x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$.

Laskua jatketaan, kunnes jonon $x_1, x_2, ...$ luvut alkavat pysyä riittävällä tarkkuudella samoina. 

Menetelmän heikkouksia ovat seuraavat:
- ratkaisun löytyminen riippuu siitä, mikä valitaan alkuarvaukseksi $x_0$
- lasku katkeaa, jos $f'(x_n)=0$

::::{admonition} Esimerkki

Etsi Newtonin menetelmällä yhtälölle $3x^2-4x-8=0$ ratkaisu käyttäen alkuarvausta $x_0=-1$.

:::{admonition} Ratkaisu
:class: tip, dropdown

Funktion derivaatta on $f'(x)=6x-4$. Lasketaan arvioita nollakohdille:

$x_1=-1-\frac{3\cdot (-1)^2-4\cdot(-1)-8}{6\cdot (-1)-4} = 0.1$

$x_1=0.1-\frac{3\cdot 0.1^2-4\cdot0.1-8}{6\cdot 0.1-4} \approx -2.36176$

$x_2=-2.36176-\frac{3\cdot (-2.36176)^2-4\cdot(-2.36176)-8}{6\cdot (-2.36176)-4} \approx -1.3612$

$x_3=-1.3612-\frac{3\cdot (-1.3612)^2-4\cdot(-1.3612)-8}{6\cdot (-1.3612)-4} \approx -1.11436$

$x_4=-1.11436-\frac{3\cdot (-1.11436)^2-4\cdot(-1.11436)-8}{6\cdot (-1.11436)-4} \approx -1.09725$

$x_5=-1.09725-\frac{3\cdot (-1.09725)^2-4\cdot(-1.09725)-8}{6\cdot (-1.09725)-4} \approx -1.09717$

$x_6=-1.09717-\frac{3\cdot (-1.09717)^2-4\cdot(-1.09717)-8}{6\cdot (-1.09717)-4} \approx -1.09717$

Tulos näyttää vakiintuvan arvoon $-1.09717$, joten tämä sopii yhtälön likimääräiseksi ratkaisuksi.

Tässä käytetyllä alkuarvauksella $x_0=-1$ ei löydetä yhtälön toista ratkaisua $x\approx 2.4305$.

:::

::::