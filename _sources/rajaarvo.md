# Funktion raja-arvo

Raja-arvo on arvo, jota funktion arvo lähestyy, kun muuttujan arvo $x$ lähestyy jotakin valittua arvoa $x_0$. Ilmaisu "funktion $f(x)$ raja-arvo, kun $x$ lähestyy lukua $x_0$" kirjoitetaan $\lim_{x \to x_0} f(x)$. 

Jos luku $x_0$ kuuluu funktion määrittelyjoukkoon, niin funktion arvo kyseisessä pisteessä voidaan laskea. Tällöin raja-arvonkin saa suoraan sijoittamalla luvun $x_0$ funktion lausekkeeseen. Tällöin $\lim_{x \to x_0} f(x)=f(x_0)$, ja sanotaan, että funktio on **jatkuva** pisteessä $x_0$. Jatkuvalle funktiolle voidaan myöhemmin laskea derivaattoja ja integraaleja.

Valitun muuttujan arvon $x_0$ ei kuitenkaan tarvitse kuulua funktion määrittelyjoukkoon. Tällöin raja-arvokaan ei siis kuulu funktion arvojoukkoon. Raja-arvon määritykseen tarvitaan tällä sivulla myöhemmin esiteltyjä keinoja.

## Raja-arvon laskeminen

Jos $x_0$ kuuluu funktion $f(x)$ määrittelyjoukoon, niin raja-arvon $\lim_{x \to x_0} f(x) = f(x_0)$ saa suoraan sijoittamalla luvun $x_0$ funktion lausekkeeseen. Jatkuvia funktioita kaikissa määrittelyjoukkonsa pisteissä ovat polynomit, potenssifunktiot, eksponenttifunktiot, logaritmifunktiot ja trigonometriset funktiot. Jatkuvia ovat myös sellaiset funktiot, jotka on muodostettu edellämainituista funktioista kerto-, jako-, yhteen- tai vähennyslaskulla (esimerkiksi $f(x)=x^2+3 e^x$).

::::{admonition} Esimerkki

Laske raja-arvo $\lim_{x \to 3} \frac{x^2-6}{2x}$.

:::{admonition} Ratkaisu
:class: tip, dropdown

Luku 3 kuuluu funktion määrittelyjoukkoon, joten sijoitetaan se funktion lausekkeeseen ja lasketaan lausekkeen arvo:

$\lim_{x \to 3} \frac{x^2-6}{2x} = \frac{3^2-6}{2\cdot 3} = \frac{3}{6} = \frac{1}{2}$.

Koska funktio on kahden (jatkuvan) polynomifunktion osamäärä, niin funktio on jatkuva. Tällöin raja-arvo pisteessä $x=3$ on sama kuin funktion arvo kyseisessä pisteessä.

:::

::::

Muuttujan arvoja, jotka eivät kuulu muuten jatkuvien funktioiden määrittelyjoukkoon, ovat mm. sellaiset arvot $x_0$, joiden sijoittaminen funktion lausekkeeseen aiheuttaisi nollalla jakamisen. Tällöin pyritään muokkaamaan funktion lauseketta siten, että sijoitus on mahdollinen. Lauseketta voi muokata käyttämällä binomikaavoja tai erottamalla polynomista yhteinen tekijä. Polynomi voidaan esittää tulomuodossa myös sen nollakohtien avulla: jos nollakohdat ovat $x_1, x_2, \dots x_n$, niin polynomin lauseke voidaan muodostaa tulona $(x-x_1) (x-x_2) \cdot \dots \cdot (x-x_n)$. Lausekkeen muokkaamisella pyritään siihen, että lausekkeesta supistuisi pois termi, johon lukua $x_0$ ei voi sijoittaa.

::::{admonition} Esimerkki

Laske raja-arvo $\lim_{x \to 2} \frac{3x^2-6x}{x-2}$.

:::{admonition} Ratkaisu
:class: tip, dropdown

Lausekkeen osoittaja $3x^2-6x$ voidaan esittää tulomuodossa yhteisen tekijän $3x$ avulla. Osoittaja muuttuu tällöin muotoon $3x(x-2)$. Nyt funktion lauseketta voidaan muokata seuraavasti:

$\frac{3x^2-6x}{x-2}=\frac{3x(x-2)}{x-2}=3x$

Siis 

$\lim_{x \to 2} \frac{3x^2-6x}{x-2} = \lim_{x \to 2} 3x = 3\cdot 2 = 6$.

:::

::::

::::{admonition} Esimerkki

Laske raja-arvo $\lim_{x \to 2} \frac{x^2-4}{x^2-2x}$.

:::{admonition} Ratkaisu
:class: tip, dropdown

Lausekkeen osoittaja $x^2-4$ voidaan kirjoittaa muodossa $x^2-2^2$. Tämä vastaa binomikaavaa $a^2-b^2=(a+b)(a-b)$. Niinpä lauseke muuttuu muotoon

$\frac{x^2-4}{x^2-2x}=\frac{(x+2)(x-2)}{x^2-2x}$.

Lausekkeen nimittäjä $x^2-2x$ voidaan esittää yhteisen tekijän avulla muodossa $x(x-2)$. Lauseke sievenee siis muotoon

$\frac{(x+2)(x-2)}{x(x-2)}=\frac{x+2}{x}$. 

Siis

$\lim_{x \to 2} \frac{x^2-4}{x^2-2x} = \lim_{x \to 2} \frac{x+2}{x} = \frac{2+2}{2}=\frac{4}{2}=2$.

:::

::::

::::{admonition} Esimerkki

Laske raja-arvo $\lim_{x \to 3} \frac{x^2+x-12}{x-3}$.

:::{admonition} Ratkaisu
:class: tip, dropdown

Nyt lausekkeen osoittajaa $x^2+x-12$ ei voi ainakaan helposti muokata tulomuotoon yhteisen tekijän tai binomikaavojen avulla. Polynomi voidaan kuitenkin esittää tulona nollakohtien avulla. Tätä varten ratkaistaan yhtälö $x^2+2-12=0$. Yhtälön ratkaisuksi saadaan toisen asteen yhtälön ratkaisukaavalla (tai laskimella) $x_1=3$ ja $x_2=-4$. Osoittaja voidaan siis esittää muodossa $(x-3)(x-(-4))$ eli $(x-3)(x+4)$. Siis

$\lim_{x \to 3} \frac{x^2+x-12}{x-3} = \lim_{x \to 3} \frac{(x-3)(x+4)}{x-3} = \lim_{x \to 3} x+4 = 3+4=7$.

:::

::::

## Raja-arvot äärettömyydessä

Usein kiinnostava valinta luvuksi $x_0$ on positiivinen tai negatiivinen ääretön, siis $\infty$ tai $-\infty$. Esimerkiksi mitä tapahtuu virtapiirissä, jos sähkövirran annetaan kasvaa äärettömän suureksi? Entä rakennuksessa, jos tiettyyn kohtaan kohdistuva kuormitus kasvaa äärettömän suureksi? Miten ympäristöön päätyneen myrkyn hajoaminen tai laimeneminen etenee äärettömän pitkällä aikavälillä tarkasteltuna? Tai millainen on jonkin aineen pitoisuus vaikkapa kallioperässä ollut hyvin kauan sitten, kun nykyinen arvo tiedetään?

Luvulle $\infty$ ei ole määritelty samankaltaisia laskutoimituksia kuin reaaliluvuille. Esimerkiksi kahden äärettömän summa on edelleen ääretön, siis $\infty+\infty=\infty$, mutta luvuista $\infty-\infty$ tai $\frac{\infty}{\infty}$ ei voida sanoa mitään.

Eräs hyvin määritelty laskukaava on mikä tahansa reaaliluku $a$ jaettuna äärettömällä:

$\frac{a}{\infty}=0$

Raja-arvon avulla ilmaistuna sama asia on $\lim_{x \to \infty}\frac{a}{x^n} = 0$. Luvun $x$ mikä tahansa potenssi $x^n$, missä $n$ on jokin positiivinen kokonaisluku, ei voi milloinkaan saavuttaa arvoa $\infty$, mutta se voi kuitenkin lähestyä sitä.

Tämän laskukaavan avulla päästään käsittelemään lausekkeita, joissa luvun $x$ paikalle pitäisi sijoittaa positiivinen tai negatiivinen ääretön. Lausekkeet pitää siis muokata sellaiseen muotoon, jossa luku $x$ tai jokin sen potenssi esiintyy murtoluvun nimittäjässä. Käytännössä tämä muokkaus onnistuu rationaalilausekkeilla siten, että lauseke supistetaan lausekkeen nimittäjässä esiintyvällä korkeimmalla $x$:n potenssilla.

::::{admonition} Esimerkki

Laske raja-arvo $\lim_{x \to \infty} \frac{2x^2+3x+4}{3x^2+4x+5}$.

:::{admonition} Ratkaisu
:class: tip, dropdown

Supistetaan lauseke nimittäjässä esiintyvällä korkeimmalla $x$:n potenssilla $x^2$:

$\frac{2x^2+3x+4}{3x^2+4x+5}=\frac{\frac{2x^2}{x^2}+\frac{3x}{x^2}+\frac{4}{x^2}}{\frac{3x^2}{x^2}+\frac{4x}{x^2}+\frac{5}{x^2}}=\frac{2+\frac{3}{x}+\frac{4}{x^2}}{3+\frac{4}{x}+\frac{5}{x^2}}$

Siis päädytään laskemaan raja-arvoa

$\lim_{x \to \infty} \frac{2+\frac{3}{x}+\frac{4}{x^2}}{3+\frac{4}{x}+\frac{5}{x^2}}$

Termit $\frac{3}{x}, \frac{4}{x^2}, \frac{4}{x}$ ja $\frac{5}{x^2}$ lähestyvät lukua 0, kun luku $x$ lähestyy ääretöntä. Raja-arvoksi saadaan siis

$\lim_{x \to \infty} \frac{2+0+0}{3+0+0} = \frac{2}{3}$

:::

::::

## Vasemman- ja oikeanpuoleiset raja-arvot

Joidenkin funktioiden arvot lähestyvät eri lukua silloin, kun muuttujan arvoa $x_0$ lähestytään vasemmalta ja oikealta puolelta. Raja-arvoa siten, että luku $x_0$ lähestytään vasemmalta, merkitään $\lim_{x \to x_0 -} f(x)$. Vastaavasti raja-arvoa, kun lukua $x_0$ lähestytään oikealta, merkitään $\lim_{x \to x_0 +} f(x)$. Näitä kutsutaan vasemman- ja oikeanpuoleiseksi raja-arvoksi. Jos nämä kaksi raja-arvoa ovat samat, niin kyseinen luku, jota funktion arvot lähestyvät, on funktion raja-arvo muuttujan arvolla $x_0$.

Vasemman- ja oikeanpuolisia raja-arvoja voi tarkastella taulukoimalla muuttujan arvoja läheltä lukua $x_0$ ja laskemalla niitä vastaavat funktion arvot. Tarkastellaan esimerkiksi, onko funktiolla $f(x)=\frac{(x-1)^2}{2x-4}$ raja-arvoa pisteessä $x_0=2$. Valitaan taulukkoon muuttujan arvoja luvun 2 molemmilta puolilta ja lasketaan vastaavat funktion arvot:

|$x$|$f(x)$|
|---|------|
|1.95|-9.025|
|1.99|-49.005|
|1.999|-499.001|
|1.9999|-4999|
|2.0001|5001|
|2.001|501.001| 
|2.01|51.005|
|2.05|11.025|

Lähestyessä lukua 2 vasemmalta puolelta funktion arvot muuttuvat aina vain pienemmiksi, ja lähestyttäessä oikealta aina vain suuremmiksi. Näin ollen funktiolla ei ole raja-arvoa kohdassa $x=2$.

Jotkut funktiot ovat paloittain määriteltyjä, eli niiden lauseke on erilainen eri $x$:n arvoilla. Jos tällöin funktion raja-arvo on sama, kun lähestytään funktion lausekkeen muutoskohtaa eri suunnista, niin kyseinen funktio on muutoskohdassaan jatkuva. 

Tarkastellaan esimerkiksi seuraavaa funktiota:

$f(x)=\begin{equation}\begin{cases}-x^2+1, x \leq 1\\x-1, x >1 \end{cases}\end{equation}$  

Lasketaan raja-arvo kohdassa $x_0=1$ erikseen vasemmalta ja oikealta. Nyt luvun 1 voi sijoittaa suoraan funktion lausekkeeseen:

$\lim_{x \to 1-} f(x) = \lim_{x \to 1} -x^2+1 = -1^2+1=-1+1=0$

$\lim_{x \to 1+} f(x) = \lim_{x \to 1} x-1 = 1-1=0$

Koska $\lim_{x \to 1-} f(x) = \lim_{x \to 1+} f(x) = f(1)$, niin funktio on jatkuva pisteessä $x=1$.

::::{admonition} Esimerkki

Määritä luku $a$ siten, että funktio on jatkuva kohdassa $x=3$, kun funktio on

$f(x)=\begin{equation}\begin{cases}2x+a, x \leq 3 \\ ax+4, x > 3\end{cases}\end{equation}$

:::{admonition} Ratkaisu
:class: tip, dropdown

Lasketaan vasemman- ja oikeanpuoleiset raja-arvot:

$\lim_{x \to 3-} f(x) = \lim_{x \to 3} 2\cdot3+a=6+a$

$\lim_{x \to 3+} f(x) = \lim_{x \to 3} a\cdot 3+4 = 3a+4$

Raja-arvojen pitää olla yhtä suuret, joten $6+a=3a+4$, josta voidaan ratkaista $a=1$.

:::

::::