# Asymptootit

Asymptootit ovat funktioiden kuvaajiin liittyviä suoria, joita funktion arvot lähestyvät, kun muuttujat arvot kasvavat tai pienenevät rajattomasti tai lähestyvät sellaista lukua, joka ei kuulu funktion määrittelyjoukkoon. Asymptootit ovat siis raja-arvoja. Asymptootteja vastaavat suorat voivat olla pystysuoria, vaakasuoria tai vinoja. Kaikissa tapauktissa asymptootin sijainnin tai lausekkeen voi selvittää tarkastelemalla funktion kuvaajaa, mutta usein myös laskemalla. Tarkastellaan näitä tapauksia seuraavaksi yksitellen.

## Pystysuorat asymptootit

Funktiolla $f(x)$ on pystysuora asymptootti kohdassa $x_0$ sellaisessa tilanteessa, että $\lim_{x \to x_0-} = \pm \infty$ tai $\lim_{x \to x_0+} = \pm \infty$. Toisin sanoen kun muuttujat arvot lähenevät arvoa $x_0$ joko vasemmalta tai oikealta (tai molemmilta puolilta), funktion arvot kasvavat tai pienenevät rajattomasti.

Pystysuorille asymptooteille ei kannata määritellä funktiota $y(x)$, sillä ne ovat aina suoria joiden kulmakerroin on ääretön. Sen sijaan voidaan laskea, missä kohdassa vaaka-akselilla asymptootti sijaitsee. Pystysuorat asympootit vastaavat niitä $x$:n arvoja, jotka funktion lausekkeeseen sijoitettuna tuottaisivat esimerkiksi nollalla jakamisen, eivätkä kuulu funktion määrittelyjoukkoon. Käytännössä pystysuora asymptootti etsitään esimerkiksi selvittämällä rationaalifunktion nimittäjän nollakohdat.

::::{admonition} Esimerkki

Määritä funktion $f(x)=\frac{x^2+2}{x^2+x-12}$ pystysuorat asymptootit.

:::{admonition} Ratkaisu
:class: tip, dropdown

Funktiota ei ole määritelty pisteissä, jotka ovat polynomin $x^2+x-12$ nollakohtia. Ratkaisemalla yhtälö $x^2+x-12=0$ saadaan selville nämä nollakohdat $x_1=3$ ja $x_2=-4$. Funktiolla on siis asymptootit pisteissä $x=3$ ja $x=-4$.

:::

::::


## Vaakasuorat asymptootit

Tarkastellaan funktiota $f(x)$. Funktion vaakasuora asymptootti on vakioarvoinen suora $y(x)=a$, jos reaaliluku $a$ on funktion $f(x)$ raja-arvo, kun $x$ lähestyy positiivista tai negatiivista ääretöntä. Vaakasuoria asymptootteja voi samalla funktiolla olla kaksikin kappaletta: toisin sanoen asymptootti voi olla $\lim_{x\to -\infty} f(x) = a$ tai $\lim_{x\to \infty} f(x) = b$.

Rationaalifunktiolla, joka on muotoa $f(x)=\frac{g(x)}{h(x)}$ on vaakasuora asymptootti, jos funktion $g(x)$ asteluku on pienempi tai yhtä suuri kuin funktion $h(x)$ asymptootti. Jos funktion $g(x)$ asteluku on pienempi kuin funktion $h(x)$ asteluku, niin asymptootti on suora $y=0$. Jos funktioiden $g(x)$ ja $h(x)$ asteluvut ovat yhtä suuret, niin asymptootti riippuu funktioiden kertoimista.

::::{admonition} Esimerkki

Määritä seuraavien funktioiden vaakasuorat asymptootit:
a) $f(x)=\frac{2x^2}{5x^3}$, b) $g(x)=\frac{3x^2}{2x^2+1}$.

:::{admonition} Ratkaisu
:class: tip, dropdown

a) Lasketaan funktion raja-arvot, kun $x \to \pm \infty$, sieventämällä funktion lauseketta:

$\lim_{x \to \pm \infty} f(x) = \lim_{x \to \pm \infty} \frac{2x^2}{5x^3} = \lim_{x \to \pm \infty} \frac{2x^2/x^3}{5x^3/x^3}= \lim_{x \to \pm \infty} \frac{2/x}{5} = 0$

b) Vastaavalla tavalla kuin edellä saadaan raja-arvot:

$\lim_{x \to \pm \infty} g(x) = \lim_{x \to \pm \infty} \frac{3x^2}{2x^2+1} = \lim_{x \to \pm \infty} \frac{3x^2/x^2}{(2x^2+1)/x^2} = \lim_{x \to \pm \infty} \frac{3}{2+1/x^2} = \frac{3}{2}$

:::
::::

::::{admonition} Esimerkki

Määritä funktion $f(x)=\frac{2}{x+1}, x\neq -1$ vaakasuorat asymptootit.

:::{admonition} Ratkaisu
:class: tip, dropdown

Osoittajan $2$ asteluku on 0 ja nimittäjän $x+1$ asteluku on 1, joten vaakasuora asymptootti on olemassa. Lasketaan raja-arvot, kun muuttujan arvo lähestyy lukuja $-\infty$ ja $\infty$:

$\lim_{x \to -\infty} \frac{2}{x+1} = \lim_{x \to -\infty} \frac{2/x}{x/x+1/x} = \lim_{x \to -\infty} \frac{2/x}{1+1/x} = 0$

$\lim_{x \to \infty} \frac{2}{x+1} = \lim_{x \to \infty} \frac{2/x}{x/x+1/x} = \lim_{x \to \infty} \frac{2/x}{1+1/x} = 0$

Funktiolla $f(x)=\frac{2}{x+1}$ on siis yksi vaakasuora asymptootti, suora $y(x)=0$. Funktion lauseketta tarkastelemalla havaitaan, että funktiolla on olemassa myös pystysuora asymptootti kohdassa $x=-1$.

:::

::::

::::{admonition} Esimerkki

Määritä funktion $f(x)=\frac{x}{\sqrt{x^2+1}}$ vaakasuorat asymptootit.

:::{admonition} Ratkaisu
:class: tip, dropdown

Kyseessä ei ole rationaalifunktio, mutta asymptootin voi silti laskea. Muokataan funktion lauseketta muotoon, jossa siihen voidaan sijoittaa $\pm \infty$:

$\frac{x}{\sqrt{x^2+1}}=\frac{x}{\sqrt{x^2(1+1/x^2)}}=\frac{x}{|x|\sqrt{1+1/x^2}}$

Huomaa, että neliöjuuren ulkopuolelle tulee $|x|$ eikä pelkkä $x$, sillä on määritelty, että neliöjuuri $\sqrt{x^2}$ on sellainen _positiivinen_ luku, joka potenssiin 2 korotettuna tuottaa luvun $x$. Niinpä jos lähestytään lukua $-\infty$ eli muuttujan arvot ovat negatiivisia, niin luvun $x$ itseisarvo on $-x$ ja tällöin funktion lausekkeeksi tulee

$f(x)=\frac{x}{-x\sqrt{1+1/x^2}}$ eli sievennettynä $f(x)=-\frac{1}{\sqrt{1+1/x^2}}$.

Tällöin raja-arvo on $\lim_{x \to -\infty} -\frac{1}{\sqrt{1+1/x^2}} = -1$

Jos taas lähestytään lukua $\infty$, niin muuttujan arvot ovat positiivisia ja tällöin $|x|=x$. 

Siis $\lim_{x \to \infty} f(x) = \lim_{x \to \infty} \frac{1}{\sqrt{1+1/x^2}} = 1$

Funktiolla $f(x)=\frac{x}{\sqrt{x^2+1}}$ on siis kaksi asymptoottia, suorat $y(x)=-1$ ja $y(x)=1$.

:::

::::


## Vinot asymptootit

Funktion $f(x)$ asymptootti voi olla myös muu kuin vaaka- tai pystysuora viiva. Tällöin asymptootti on muotoa $y(x)=ax+b$, eli kyseessä on suoran yhtälö. Kyseinen suora on funktion $f(x)$ asymptootti, jos funktion $f(x)$ arvot lähestyvät suoran arvoja, kun $x$ lähestyy positiivista tai negatiivista ääretöntä. Toisin sanoen erotus $f(x)-y(x)$ lähestyy nollaa, kun $x$ kasvaa tai pienenee rajattomasti. Raja-arvon avulla ehto kirjoitetaan muodossa

$\lim_{x\to -\infty} f(x)-y(x) = 0$ tai $\lim_{x\to \infty} f(x)-y(x) = 0$.

Käytännössä tällaisia raja-arvoja voi olla hankalaa määrittää. Tarkastellaan tässä rationaalifunktioita, jotka voidaan kirjoittaa muodossa

$f(x)=\frac{g(x)}{h(x)}$.

Vino asymptootti on olemassa silloin, kun polynomin $g(x)$ asteluku on yhtä suurempi kuin polynomin $h(x)$ asteluku. Tällaisia funktioita ovat esimerkiksi

$f(x)=\frac{x^2+2}{3x+5}$ ja $f(x)=\frac{x^4+x-1}{2x^3+x^2}$

Suoran yhtälön $ax+b$ saa selville jakolaskulla $\frac{g(x)}{h(x)}$, josta tuloksena on polynomi $ax+b$ sekä mahdollisesti jakojäännös. Laskukaava on suoraa seurausta siitä, että raja-arvon avulla esitettyyn ehtoon sijoitetaan polynomifunktiot, joissa on keskenään sopivat asteluvut.

Polynomien jakolaskua jakokulmassa ei opetella tällä opintojaksolla. Jakolaskun voi suorittaa tietokoneella. Esimerkiksi jakolaskusta $\frac{x^2+2}{3x+5}$ saadaan [WolframAlpha](https://www.wolframalpha.com/) -laskimella tulos: 

$x^2 + 2 = (\frac{x}{3} - \frac{5}{9})(3x + 5) + \frac{43}{9}$,

josta voidaan päätellä, että funktion $f(x)=\frac{x^2+2}{3x+5}$ asymptootin yhtälö on $y(x)=\frac{x}{3} - \frac{5}{9}$.