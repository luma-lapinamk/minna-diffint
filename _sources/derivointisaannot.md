# Derivointisääntöjä

Funktioiden derivaattoja ei käytännössä koskaan tarvitse laskea erotusosamäärän raja-arvon avulla. Funktioille on johdettu - erotusosamäärän raja-arvoa hyödyntäen - valmiita derivoimiskaavoja, jotka esitellään tässä luvussa. Lopuksi tarkastellaan myös sitä, miten voidaan arvioida derivaatta numeeriselle aineistolle, jota kuvaava funktio ei ole tiedossa.

## Perusfunktioiden derivaatat

|Funktio|Laskukaava|
|---|---|
|Vakiofunktio | $D~C = 0 $ |
|Potenssifunktio | $D~x^n = nx^{n-1}$ |
|Sinifunktio | $D~ \sin{x} = \cos{x}$ |
|Kosinifunktio | $D~ \cos{x} = -\sin{x}$|
|Yleinen eksponenttifunktio | $D~a^x = a^x ~\ln{a}$ |
|Eksponenttifunktio, erikoistapaus | $D~ e^x = e^x$|
|Logaritmifunktio | $D~ \text{ln}~x = \frac{1}{x}$|

## Yleisiä derivointisääntöjä

Funktiot ovat usein edellisten perusfunktioiden summia tai tuloja tai perusfunktioista yhdistettyjä funktioita. Tässä laskukaavat, joilla sellaisia funktioita voi derivoida.

|Tapaus|Laskukaava|
|---|---|
|Funktioiden summa | $D~ [f(x)+g(x)] = D~ f(x) + D~ g(x)$ |
|Vakiolla kerrottu funktio | $D~ a f(x) = a D~f(x)$ |
|Funktioiden tulo | $D~ [f(x) g(x)] = g(x) D~ f(x) + f(x) D~ g(x)$ |
|Funktioiden osamäärä | $D~ \frac{f(x)}{g(x)} = \frac{[D~ f(x)] \cdot g(x) - [D~ g(x)]\cdot f(x)}{[g(x)]^2}$ |
|Yhdistetty funktio | $D~ f(g(x)) = [D~ f(g(x))] \cdot D~ g(x)$ |

:::: {admonition} Esimerkki

Derivoi seuraavat funktiot:

a) $f(x)=2x+x^4$

b) $f(x)=3 x^2$

c) $f(x)=2x\cdot e^x$

d) $f(x)=\frac{3x}{2x+1}$

e) $f(x)=\sin{3x^2}$

:::{admonition} Ratkaisu
:class: tip, dropdown

a) $D~(2x+x^4) = D~2x + D~x^4 = 2 + 4x^3 $

b) $D~3 x^2 = 3 D~x^2 = 3\cdot 2x = 6x$

c) $D~(2x\cdot e^x) = e^x D~2x + 2x D~e^x = 2e^x + 2xe^x$

d) $D~\frac{3x}{2x+1}=\frac{[D~3x]\cdot(2x+1)-3x\cdot D~(2x+1)}{(2x+1)^2} = \frac{3\cdot(2x+1)-3x\cdot 2}{(2x+1)^2} = \frac{3}{(2x+1)^2}$

e) $D~\sin{3x^2}=\cos{3x^2}\cdot D~3x^2 = 6x\cdot \cos{3x^2}$

:::

::::

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

Osittaisderivaattaa sovelletaan tässä materiaalissa erityyppisten mittausvirheiden arviointiin omassa luvussaan.


## Esimerkkejä

Yleisesti ottaen derivaatta tarkoittaa hetkellistä muutosnopeutta. Tästä seuraa se, että esimerkiksi fysiikassa pystytään ratkaisemaan muunkinlaisia ongelmia kuin niitä mihin löytyy taulukkokirjasta valmis fysiikan kaava. Esimerkiksi liikkuvan kappaleen _hetkellinen_ nopeus saattaa olla jotain muuta kuin saman kappaleen _keskinopeus_.

::::{admonition} Esimerkki

Tarkastellaan liikkuvaa kappaletta, jonka sijainti hetkellä $t$ on $x(t)$. Kappaleen hetkellinen nopeus on määritelty $v(t)=x'(t)$, ja hetkellinen kiihtyvyys puolestaan $a(t)=v'(t)$. Robotin halutaan liikkuvan siten, että sen sijainti noudattaa funktiota $x(t)=t-\sin{t}$. Mikä pitää tällöin olla robotin nopeuden ja kiihtyvyyden ajan funktiona?

:::{admonition} Ratkaisu
:class: tip, dropdown

Nopeus on $v(t)=x'(t)=1-\cos{t}$.

Kiihtyvyys on $a(t)=v'(t)=0-(-\sin{t})=\sin{t}$.

Tarkastele esimerkiksi [GeoGebralla](https://www.geogebra.org/calculator) sekä paikan, nopeuden että kiihtyvyyden kuvaajaa, niin ymmärrät, miten robotti liikkuu! Tehtävää voisi tietysti vielä jatkaa fysiikalla, sillä Newtonin lakien mukaisesti tiettyyn kiihtyyteen tarvitaan tietyn suuruinen voima...

:::

::::

::::{admonition} Esimerkki

Oletetaan, että erään auton arvo jollakin hetkellä on 45 000 euroa ja se alenee 10 % vuodessa. Joka vuosi siis auton arvo kerrotaan luvulla 0.9, eli arvo noudattaa funktiota $f(x)=45000\cdot 0.9^x$. Miten nopeasti auton arvo alenee hetkellä $x=5$ vuotta?

:::{admonition} Ratkaisu
:class: tip, dropdown

Lasketaan derivaatta $f'(x)=45000\cdot D~0.9^x=45000\cdot 0.9^x\cdot \ln{0.9}$

Derivaatan arvo hetkellä $x=5$ vuotta on $f'(5)=45000\cdot 0.9^5\cdot \ln{0.9} \approx -2800$ eli tuolla hetkellä arvo alenee 2800 euroa vuodessa.

:::

::::