# Funktion ääriarvot

Funktion $f(x)$ derivaatan $f'(x)$ merkki kertoo, onko funktio kasvava vai vähenevä. Derivaatan merkki voi vaihdella eri muuttujan arvoilla. Niillä muuttujan $x$ arvoilla, joilla funktion $f(x)$ derivaatta $f'(x)$ on positiivinen, funktio on kasvava. Vastaavasti niillä muuttujan arvoilla, joilla derivaatta on negatiivinen, funktio on vähenevä.

Sellaisissa kohdissa, joissa funktio muuttuu kasvavasta väheneväksi tai vähenevästä kasvavaksi, funktion derivaatta on nolla. Tällaista kohdista löytyy funktion ääriarvoja. Ne ovat ikään kuin "mäen huippuja" ja "kuopan pohjia". Huippukohtia kutsutaan nimellä maksimi ja pohjakohtia nimellä minimi. Funktiolla voi olla useita tällaisia lokaaleja eli paikallisia ääriarvoja, aivan kuten työmatkan varrella voi olla useita mäkiä ja kuoppia. Jokin näistä lokaaleista ääriarvoista voi olla myös globaali ääriarvo eli suurin tai pienin mahdollinen funktion saama arvo. 

Funktion lokaaleja ääriarvoja etsitään käytännössä siten, että lasketaan funktion derivaatta ja ratkaistaan sitten yhtälö $f'(x)=0$. Derivaatan lausekkeesta riippuen näitä nollakohtia voi olla useitakin. Muuttujan arvoja, jotka toteuttavat yhtälön $f'(x)=0$, sanotaan funktion ääriarvokohdiksi. Ääriarvot ovat funktion arvoja siten, että funktion lausekkeeseen sijoitetaan muuttujan paikalle ääriarvokohdat.

Derivaatan nollakohdat selvittämällä löytää jotkin ääriarvokohdat. Ei kuitenkaan suoraan voi päätellä, onko kyseessä minimi- vai maksimikohta. Tällöin voi avuksi tarkastella derivaatan merkkiä ääriarvokohdan molemmin puolin. Jos derivaatan merkki on ennen nollakohtaa positiivinen ja nollakohdan jälkeen negatiivinen, niin funktio muuttuu ääriarvokohdassa kasvavasta väheneväksi ja tällöin kyseessä on lokaali maksimi. Jos taas derivaatan merkki muuttuu negatiivisesta positiiviseksi, niin funktio muuttuu vähenevästä kasvavaksi, ja kyseessä on lokaali minimi.

::::{admonition} Esimerkki

Selvitä funktion $f(x)=x^3-\frac{3}{2}x^2-18x$ ääriarvokohdat ja ääriarvot.

:::{admonition} Ratkaisu
:class: tip, dropdown

Funktion derivaatta on $f'(x)=3x^2+3x-18$. Derivaatan nollakohdat saadaan ratkaisemalla yhtälö $3x^2+3x-18=0$, josta saadaan ratkaisut $x=-3$ tai $x=2$. 

Valitaan muuttujalle arvoja: jokin lukua -3 pienempi arvo, jokin lukujen -3 ja 2 välissä oleva arvo, ja jokin luku 2 suurempi luku. Mitkä tahansa luvut, jotka toteuttavat nämä ehdot, kelpaavat laskuun. Lasketaan derivaatan arvoja näillä muuttujan arvoilla. Kirjataan tulokset taulukkoon:

| Muuttujan arvo | $x=-5$| $x=0$ | $x=5$|
|----------------|-------|-------|-------|
|Derivaatan arvo |$42$ |$-18$|$ 72$|
|Derivaatan merkki| $+$ | $-$ | $+$ |
|Funktion suunta | kasvava | vähenevä |kasvava|

Taulukosta voidaan päätellä:

- Pisteessä $x=-3$ funktio muuttuu kasvavasta väheneväksi, joten $x=-3$ on funktion lokaali maksimikohta. Tässä kohdassa funktion arvo, eli lokaali maksimiarvo, on $f(-3)=(-3)^3+\frac{3}{2}\cdot (-3)^2 -18\cdot (-3) = \frac{81}{2}$.

- Pisteessä $x=2$ funktio muuttuu vähenevästä kasvavaksi, joten $x=2$ on funktion lokaali minimikohta. Tässä kohdassa funktion arvo, eli lokaali minimiarvo, on $f(2)=2^3+\frac{3}{2}\cdot 2^2 -18\cdot 2 = -22$.

Funktion kuvaajaa tarkastelemalla nähdään, että funktion arvot pienenevät rajattomasti, kun $x \to -\infty$, ja kasvavat rajattomasti, kun $x \to \infty$. Niinpä edellä lasketut ääriarvot eivät ole funktion suurimmat tai pienimmät mahdolliset arvot.

:::

::::

Edellisessä esimerkissä funktiolle löytyi yksi lokaali minimi ja yksi lokaali maksimi. Ääriarvokohtien määrä riippuu funktiosta, esimerkiksi jatkuvasti aaltoilevalla sini- tai kosinifunktiolla on äärettömän monta lokaalia minimi- ja maksimikohtaa. Joillakin funktioilla taas ei ole ääriarvokohtia ollenkaan. Esimerkiksi funktion $f(x)=3x+1$ derivaatta on $f'(x)=3$, joka ei riipu muuttujasta $x$, jolloin ei myöskään ole mahdollista löytää sellaista muuttujan arvoa $x$, joka toteuttaisi yhtälön $f'(x)=0$. Yleisesti asteen $n$ polynomifunktiolla voi olla $n-1$ lokaalia äärikohtaa.

::::{admonition} Esimerkki

Määritä funktion $f(x)=4x^2+3x+5$ ääriarvot.

:::{admonition} Ratkaisu
:class: tip, dropdown

Funktion derivaatta on $f'(x)=8x+3$. 

Derivaatan nollakohdat saadaan yhtälöstä $8x+3=0$, jolle on vain yksi ratkaisu $x=-\frac{3}{8}$. 

Derivaatan arvo jollakin tätä pienemmällä luvulla on negatiivinen, esimerkiksi $f'(-2)=8\cdot(-2)+3=-16+3=-13 < 0 $, ja vastaavasti derivaatan arvo jollakin suuremmalla luvulla on positiivinen, esimerkiksi $f'(0)=8\cdot 0 +3 = 3 > 0$. 

Näin ollen funktio muuttuu pisteessä $x=-\frac{3}{8}$ vähenevästä kasvavaksi, ja kyseessä on funktion lokaali minimi.

:::

::::

Ääriarvokohdan laadun - siis sen, onko ääriarvokohta lokaali minimi vai lokaali maksimi - voi selvittää myös tarkastelemalla funktion $f(x)$ toista derivaattaa $f''(x)$ ääriarvokohdassa. Toinen derivaatta tarkoittaa derivaattafunktion $f'(x)$ derivaattaa. Jos toinen derivaatta $f''(x)$ on ääriarvokohdassa positiivinen, tarkoittaa se sitä, että funktion derivaatta $f'(x)$ on kasvava, ja edelleen funktion $f(x)$ kuvaaja on kääntymässä ylöspäin. Siis jos $f''(x) > 0$, kun $f'(x)=0$, niin ääriarvokohta on lokaali minimi. Vastaavasti jos $f''(x) < 0$, kun $f'(x)=0$, niin ääriarvokohta on lokaali maksimi.

::::{admonition} Esimerkki

Määritä funktion $f(x)=x^3-15x^2+48x+7$ ääriarvokohdat ensimmäisen ja toisen derivaatan avulla.

:::{admonition} Ratkaisu
:class: tip, dropdown

Funktion $f(x)$ ensimmäinen derivaatta on $f'(x)=3x^2-30x+48$.

Derivaatan nollakohdiksi voidaan ratkaista $x=2$ ja $x=8$.

Funktion $f(x)$ toinen derivaatta on $f''(x)=6x-30$.

Kun $x=2$, niin $f''(x)=f''(2)=6\cdot 2 -30 = 12-30 = -18 < 0$. Pisteessä $x=2$ funktiolla on siis lokaali maksimi.

Kun $x=8$, niin $f''(x)=f''(8)=6\cdot 8 -30 = 48-30 = 18 > 0$. Pisteessä $x=8$ funktiolla on siis lokaali minimi.

:::

::::

Jos halutaan selvittää funktion globaali ääriarvo, pitää tarkastella lisäksi funktion arvoja määrittelyjoukon ääripäissä. (Työmatkavertauksessa tämä tarkoittaisi sitä, että suurin mäki tai kuoppa onkin heti kotiovella tai määränpäässä.) Jos funktion määrittelyjoukko on koko reaalilukujen joukko, niin globaalia minimiä tai maksimia ei välttämättä ole mahdollista selvittää. Sen sijaan jos määrittelyjoukko on rajattu joidenkin lukujen $a$ ja $b$ välille, niin globaali ääriarvo löytyy joko derivaatan nollakohtaa vastaavalla muuttujan arvolla, tai laskemalla $f(a)$ tai $f(b)$.

::::{admonition} Esimerkki

Selvitä funktion $f(x)=\frac{2}{3}x^3-4x^2+6x+10$ pienin ja suurin arvo välillä $[-2,10]$.

:::{admonition} Ratkaisu
:class: tip, dropdown

Funktion derivaatta on $f'(x)=2x^2-8x+6$, ja derivaatan nollakohdat yhtälöstä $2x^2-8x+6=0$ ovat $x=1$ ja $x=3$.

Taulukoidaan derivaatan arvoja nollakohtien väleissä:

| Muuttujan arvo | $x=0$| $x=2$ | $x=5$|
|----------------|-------|-------|-------|
|Derivaatan arvo |$6$ |$-6$|$ 16$|
|Derivaatan merkki| $+$ | $-$ | $+$ |
|Funktion suunta | kasvava | vähenevä |kasvava|

Kohdassa $x=1$ on siis funktion lokaali maksimikohta, ja kohdassa $x=3$ on funktion lokaali minimikohta. Sama asia voitaisiin selvittää myös toisen derivaatan avulla: $f''(x)=4x-8$, johon derivaatan nollakohdat sijoittamalla saadaan $f''(1)=4\cdot 1 -8 = -4 < 0$ (lokaali maksimi) ja $f''(3)=4\cdot 3 -8 = 12-8=4 > 0$ (lokaali minimi)$.

Lasketaan funktion arvot näissä pisteissä:

$f(1)=\frac{2}{3}\cdot 1^3-4\cdot 1^2+6\cdot 1 +10=\frac{38}{3}$  

$f(3)=\frac{2}{3}\cdot 3^3-4\cdot 3^2+6\cdot 3 +10=10$ 

On kuitenkin mahdollista, että funktion suurin tai pienin arvo löytyy välin $[-2,10]$ jommasta kummasta päätepisteestä. Lasketaan siis vielä varmuuden vuoksi funktion arvot kyseisissä pisteissä:

$f(-2)=\frac{2}{3}\cdot (-2)^3-4\cdot (-2)^2+6\cdot (-2) +10=-\frac{70}{3}$ 

$f(10)=\frac{2}{3}\cdot 10^3-4\cdot 10^2+6\cdot 10 +10=\frac{1010}{3}$ 

Todetaan, että derivaatan nollakohtien avulla löydetty minimi ja maksimi eivät ole funktion pienin ja suuri arvo välillä $[-2,10]$. Globaali maksimiarvo on $f(10)=\frac{1010}{3}$ ja globaali miniarvo on $f(-2)=-\frac{70}{3}$.

:::

::::