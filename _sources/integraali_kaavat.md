# Integraalilaskenta

Funktio $F(x)$ on funktion $f(x)$ _integraalifunktio_, jos $F'(x)=f(x)$. Esimerkiksi funktio $F(x)=\frac{1}{3}x^3$ on funktion $f(x)=x^2$ integraalifunktio, sillä derivointikaavoilla saadaan: $F'(x)=3\cdot \frac{1}{3}x^2 = x^2$.

Yleisesti funktiolla $f(x)$ on äärettömän monta integraalifunktiota $F(x)+C$, missä $C$ on jokin reaaliluku. Lukua $C$ kutsutaan integroimisvakioksi. Kaikki funktiot $F(x)+C$ ovat funktion $f(x)$ integraalifunktioita riippumatta luvun $C$ arvosta, sillä vakio $C$ ei vaikuta funktion derivaattaan. Näin ollen myös esimerkiksi funktio $F(x)=\frac{1}{3}x^3+5$ on funktion $f(x)$ eräs integraalifunktio.

Funktioiden $f(x)$ ja $F(x)+C$ yhteyttä merkitään seuraavasti:

$\int f(x)~\text{d}x = F(x)+C$

Merkintä $\text{d}x$ tarkoittaa, että funktiota $f(x)$ käsitellään nimenomaan muuttujan $x$ suhteen.

Integraalilaskennassa on siis tarkoituksena löytää funktio $F(x)+C$, kun tiedossa on funktio $f(x)$. Vakion $C$ arvon saa selville, jos funktiosta $F(x)+C$ tiedetään jokin tiettyä muuttujan arvoa vastaava arvo.

Seuraavaksi esitellään kaavat, joilla onnistuu yksinkertaisten funktioiden integrointi, eli funktion $F(x)+C$ määrittäminen funktion $f(x)$ perusteella. Aluksi esitellään perusfunktioiden integrointikaavat. Kun integroitava funktio on yhdistelmä useammasta perusfunktiosta, integrointiin on omat laskukaavansa. Ne perustuvat vastaaviin derivaattalaskujen kaavoihin ja voidaan perustella derivoimalla. Aina useasta perusfunktiosta muodostuvan funktion integrointi ei  ole helppoa tai edes mahdollista. 

## Perusfunktioiden integrointi

- Vakiofunktio: $\int a~\text{d}x = ax+C$

- Potenssifunktio $(n \neq -1)$: $\int x^n~\text{d}x = \frac{1}{n+1}x^{n+1} + C$

- Potenssifunktion erikoistapaus: $\int \frac{1}{x}~\text{d}x=\text{ln}~x+C$

- Eksponenttifunktio: $\int e^x~\text{d}x=e^x+C$

- Sinifunktio: $\int\text{sin}~x~\text{d}x=-\text{cos}~x+C$

- Kosinifunktio: $\int\text{cos}~x~\text{d}x=\text{sin}~x+C$

::::{admonition} Esimerkki

Suorita seuraavat laskut:

a) $\int x^5 ~\text{d}x$

b) $\int x^{-3}~\text{d}x$

c) $\int \sqrt{x}~\text{d}x$

:::{admonition} Ratkaisu
:class: tip, dropdown

a) $\int x^5 ~\text{d}x=\frac{1}{6} x^6 +C $

b) $\int x^{-3}~\text{d}x = -\frac{1}{2} x^{-2} + C = -\frac{1}{2x^2}+C$

c) Kirjoitetaan neliöjuuri $\sqrt{x}$ murtopotenssimuodossa: $\sqrt{x}=x^{\frac{1}{2}}$ ja käytetään sitten potenssifunktion derivointisääntöä:

$\int x^{\frac{1}{2}}~\text{d}x = \frac{1}{\frac{1}{2}+1}x^{\frac{1}{2}+1} = \frac{1}{\frac{3}{2}}x^{\frac{3}{2}}=\frac{2}{3}x^{\frac{3}{2}}$

:::

::::


## Yhdistetyn funktion integrointi

- Summan integraali: $\int f(x) + g(x) ~\text{d}x = \int f(x) ~\text{d}x+\int g(x) ~\text{d}x$

- Vakiolla kerrotun funktion integraali: $\int af(x)~\text{d}x=a\int f(x)~\text{d}x$

- Jos $\int f(x)~\text{d}x = F(x)+C\), niin \(\int f(ax)~\text{d}x = \frac{1}{a} F(ax) + C$

- Jos $\int f(x)~\text{d}x = F(x)+C\), niin \(\int f(ax+b)~\text{d}x = \frac{1}{a} F(ax+b) + C$

- Jos $\int f(x)~\text{d}x = F(x)+C\), niin \(\int f(s(x))\cdot s'(x)~\text{d}x=F(s(x))+C$


::::{admonition} Esimerkki

Suorita seuraavat laskut:

a) $\int 2x+4x^2 ~\text{d}x$

b) $\int \text{cos}(3x)~\text{d}x$

c) $\int (7x+2)^3~\text{d}x$

d) $\int \text{sin}(x^2)\cdot 2x~\text{d}x$


:::{admonition} Ratkaisu
:class: tip, dropdown

a) $\int 2x+4x^2 ~\text{d}x=\int 2x~\text{d}x+\int{4x^2}~\text{d}x=x^2+\frac{4}{3}x^3+C$

b) $\int \text{cos}(3x)~\text{d}x=\frac{1}{3}\text{sin}(3x)+C$

c) $\int (7x+2)^3~\text{d}x=\frac{1}{7}\frac{(7x+2)^4}{4}+C$

d) $\int \text{sin}(x^2)\cdot 2x~\text{d}x = -\text{cos}(2x)+C$

:::

::::

::::{admonition} Esimerkki

Määritä funktiolle $f(x)$ integraalifunktio $F(x)$ annetulla ehdolla:

a) $f(x)=3x^2-4, F(1)=8$

b) $f(x)=2x^3+2x, F(1)=4$

:::{admonition} Ratkaisu
:class: tip, dropdown

a) Lasketaan ensin integraalifunktio $F(x)+C$:

$\int 3x^2-4 ~\text{d}x=x^3-4x+C$

Ratkaistaan vakion $C$ arvo sijoittamalla $x=1$:

$1^3-4\cdot 1 + C = 8$

$C=8-1+4=11$

Kysytty funktio on siis $F(x)=x^3-4x+11$.

b) Lasketaan ensin integraalifunktio $F(x)+C$:

$\int 2x^3-2x ~\text{d}x=2\cdot \frac{1}{4}x^4-2\cdot \frac{1}{2}x^2+C=\frac{1}{2}x^4+x^2+C$

Ratkaistaan vakion $C$ arvo sijoittamalla $x=1$:

$\frac{1}{2}\cdot 1^4+1^2+ C = 4$

$C=4-1-\frac{1}{2}=\frac{5}{2}$

Kysytty funktio on siis $F(x)=\frac{1}{2}x^4+x^2+\frac{5}{2}$.

:::

::::

Tulon ja osamäärän integroinnille ei ole vastaavia sääntöjä kuin derivoinnille. Tulomuodossa esitetty polynomi kannattaa sieventää summamuotoon. Polynomien osamääräkin sievenee joskus summaksi. Summamuodosta jokaisen termin voi integroida erikseen.

::::{admonition} Esimerkki

Integroi seuraavat funktiot:

a) $f(x)=(x-1)(x+1)$

b) $f(x)=\frac{x^2+x+1}{x}$

:::{admonition} Ratkaisu
:class: tip, dropdown

a) Muutetaan funktion $f(x)$ lauseke summamuotoon: $(x-1)(x+1)=x^2+x-x-1^2=x^2-1$

Siis $\int (x-1)(x+1) ~\text{d}x = \int x^2-1 ~\text{d}x =\frac{1}{3}x^3-x+C$

b) Funktion $f(x)$ lauseke voidaan sieventää seuraavasti:

$\frac{x^2+x+1}{x}=\frac{x^2}{x}+\frac{x}{x}+\frac{1}{x}=x+1+\frac{1}{x}$

Integraaliksi saadaan 

$\int \frac{x^2+x+1}{x}~\text{d}x = \int x+1+\frac{1}{x}~\text{d}x=\frac{1}{2}x^2+x+\ln{x}+C$

:::

::::





