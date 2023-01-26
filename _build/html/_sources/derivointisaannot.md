# Derivointisääntöjä

Funktioiden derivaattoja ei käytännössä koskaan tarvitse laskea erotusosamäärän raja-arvon avulla. Funktioille on johdettu - erotusosamäärän raja-arvoa hyödyntäen - valmiita derivoimiskaavoja, jotka esitellään tässä luvussa. Lopuksi tarkastellaan myös sitä, miten voidaan arvioida derivaatta numeeriselle aineistolle, jota kuvaava funktio ei ole tiedossa.

## Perusfunktioiden derivaatat

Vakio: $D~C = 0 $

Potenssi: $D~x^n = nx^{n-1}$

Sini: $D~ \text{sin}~x = \text{cos}~x$

Kosini: $D~ \text{cos}~x = -\text{sin}~x$

Eksponentti: $D~ e^x = e^x$

Logaritmi: $D~ \text{ln}~x = \frac{1}{x}$

## Yleisiä derivointisääntöjä

Funktioiden summa: $D~ [f(x)+g(x)] = D~ f(x) + D~ g(x)$

Esim. $D~(2x+x^4) = D~2x + D~x^4 = 2 + 4x^3 $

Vakiolla kerrottu funktio: $D~ a f(x) = a D~f(x)$

Esim. $D~3 x^2 = 3 D~x^2 = 3\cdot 2x = 6x$

Funktioiden tulo: $D~ [f(x) g(x)] = g(x) D~ f(x) + f(x) D~ g(x)$

Esim. $D~(2x\cdot e^x) = e^x D~2x + 2x D~e^x = 2e^x + 2xe^x$

Funktioiden osamäärä: $D~ \frac{f(x)}{g(x)} = \frac{[D~ f(x)] \cdot g(x) - [D~ g(x)]\cdot f(x)}{[g(x)]^2}$

Esim. $D~\frac{3x}{2x+1}=\frac{[D~3x]\cdot(2x+1)-3x\cdot D~(2x+1)}{(2x+1)^2} = \frac{3\cdot(2x+1)-3x\cdot 2}{(2x+1)^2} = \frac{3}{(2x+1)^2}$

Yhdistetty funktio: $D~ f(g(x)) = [D~ f(g(x))] \cdot D~ g(x)$

Esim. $D~\text{sin}~(3x^2)=\text{cos}~(3x^2)\cdot D~3x^2 = 6x\cdot \text{cos}~(3x^2)$

## Numeerinen derivointi

Aina ei ole käytettävissä funktion lauseketta, jota voisi edellisten sääntöjen mukaan derivoida. Kuvitellaan esimerkiksi, että yötaivaalla näkyisi tuntematon lentävä esine, ja haluaisimme selvittää sen hetkellisiä nopeuksia. Tällöin selvittäisimme esineen sijainnin eri ajanhetkinä, siis esimerkiksi hetkellä $t_1$ sijainti olisi $y(t_1)$, ja mittausväliä $\Delta t$ myöhemmin, hetkellä $t_2=t_1+\Delta t$, sijainti olisi $y(t_2)$.

Käytännössä nopeus hetkellä $t$ voitaisiin laskea siten, että valittaisiin kiinnostavan ajanhetken $t$ molemmin puolin arvot $t-\Delta t$ ja $t+\Delta t$ sekä näitä vastaavat mittaustulokset $y(t-\Delta t)$ ja $y(t+\Delta t)$, ja laskettaisiin erotusosamäärä:

$\frac{y(t+\Delta t)-y(t-\Delta t)}{2 \Delta t}$

::::{admonition} Esimerkki

Tuntematon lentävä esine liikkui seuraavan taulukon mukaisesti:

|aika $t$ (s)| etäisyys $y$ (km)|
|---|---|
|18|2.24|
|19|2.58|
|20|2.99|
|21|3.41|
|22|3.84|

Laske esineen hetkellinen nopeus hetkillä 19 s, 20 s ja 21 s.

:::{admonition} Ratkaisu
:class: tip, dropdown

- Hetkellä 19 s hetkellinen nopeus oli $\frac{2.99~\text{km}-2.24~\text{km}}{2~\text{s}}=0.375~\frac{\text{km}}{\text{s}}$,

- hetkellä 20 s hetkellinen nopeus oli $\frac{3.41~\text{km}-2.58~\text{km}}{2~\text{s}}=0.415~\frac{\text{km}}{\text{s}}$,

- hetkellä 21 s hetkellinen nopeus oli $\frac{3.84~\text{km}-2.99~\text{km}}{2~\text{s}}=0.425~\frac{\text{km}}{\text{s}}$.

:::

::::

## Osittaisderivaatat

Osittaisderivaatta tarkoittaa monen muuttujan funktion derivointia vain yhden muuttujan suhteen. Funktion $f(x,y)$ osittaisderivaattaa muuttujan $x$ suhteen merkitään $\frac{\partial f}{\partial x}$ ja osittaisderivaattaa muuttujan $y$ suhteen $\frac{\partial f}{\partial y}$

Osittaisderivaattaa kuvaava merkki $\partial$ lausutaan "doo". Osittaisderivaattoja laskettaessa muita muuttujia ajatellaan vakioina. Esimerkiksi funktion $f(x,y)=3xy+4x-2y$ osittaisderivaatat ovat  $\frac{\partial f}{\partial x}=3y+4$ ja $\frac{\partial f}{\partial y} = 3x-2$.