# Logaritmit ja eksponenttiyhtälöt

Monia insinöörialoilla tarpeellisia ilmiöitä voidaan kuvailla eksponenttifunktioilla. Esimerkiksi tietokoneen sisällä kondensaattoreissa sähkövaraus purkautuu eksponentiaalisesti. Toinen toisinaan esiintyvä matemaattinen malli on logaritmifunktio. Esimerkiksi maanjäristyksien voimakkuutta kuvaillaan logaritmisella asteikolla. Tällä sivulla on saatavilla riittävät tiedot siihen, että tällaisia ilmiöitä voidaan käsitellä laskennallisesti. 

Matemaattisina käsitteitä sekä eksponentti- että logaritmifunktio ovat alkeisfunktioita. Niitä voidaan siis tarkastella samasta näkökulmasta kuin muitakin funktioita osiossa "Funktiot". Logaritmifunktio on eksponenttifunktion käänteisfunktio. Kummallekin funktiolle voidaan laskea esimerkiksi raja-arvoja, derivaatta ja integraali. Näitä asioita tarkastellaan tässä oppimateriaalissa toisaalla.

## Logaritmin määritelmä

Logaritmi $\log_a x$ on luku $y$, johon korotettuna luku $a$ muuttuu luvuksi $x$, siis $a^y = x$ tai $a^{\log_a x} = x$. Merkinnästä $\log_a x$ käytetään nimitystä "luvun $x$ $a$-kantainen logaritmi". Esimerkiksi luvun 16 2-kantainen logaritmi on 4, sillä $2^4=16$.

Kantalukujen $e$ (Neperin luku, $e\approx 2.72$) ja $10$ logaritmeilla on omat merkintänsä: $\log_e{x} = \ln{x}$ ja $\log_{10}{x}=\lg{x}$. Logaritmia, jossa on kantalukuna $e$, kutsutaan luonnolliseksi logaritmiksi. Kymmenkantaisen logaritmin toinen nimitys on Briggsin logaritmi. Nämä kaksi logaritmia löytyvät useista laskimista, ja niille onkin paljon sovelluksia. 

Logaritmeille on olemassa muutamia [laskusääntöjä](https://fi.wikipedia.org/wiki/Logaritmi), joista tässä yhteydessä tarvitaan yhtä. Alla on myös tiivistettynä myös logaritmin määritelmä.

::::{admonition} Logaritmi työkaluna

1. $\log_a{x} = y \Leftrightarrow a^y = x$

2. $\log_a{x^n}=n \log_a{x}$

:::{admonition} Kohdan 2 perustelu
:class: tip, dropdown

Määritellään aluksi, että $\log_a{x}=y$. Logaritmin määritelmän perusteella voidaan kirjoittaa, että $a^y=x$. Korotetaan tämän yhtälön molemmat puolet potenssiin $n$:

$(a^y)^n=x^n$

Sievennetään vasen puoli potenssin laskusääntöjen mukaan:

$a^{yn}=x^n$

Nyt voidaan taas soveltaa logaritmin määritelmää: koska $a^{yn}=x^n$, niin $\log_a{x^n}=yn$. Toisaalta edellä määriteltiin, että $y=\log_a{x}$. Näin ollen voidaan kirjoittaa: $\log_a{x^n}=n \log_a{x}$.

:::

::::

## Logaritmiset suureet

Logaritmeja käytetään sellaisten asioiden ilmaisemiseen, jotka voivat saada sekä hyvin pieniä että hyvin suuria arvoja. Esimerkki tästä on ihmisen kuulemat äänet. Tällaisten suureiden ilmaisussa tarvitaan suureeseen liittyvää intensiteettiä eli tehoa pinta-alayksikköä kohden, jota verrataan johonkin vertailuarvoon. Näiden intensiteettien suhteesta lasketaan kymmenkantainen logaritmi. Äänen tapauksessa vielä kerrotaan tämä logaritmi luvulla 10, jotta saadaan käytännöllinen asteikko äänenvoimakkuuksille. Äänen voimakkuutta kuvailevat desibelit (dB) saadaan seuraavasti:

$\text{dB}=10 \lg{\frac{I}{I_0}}$

missä $I$ on kyseisen äänen intensiteetti ja $I_0$ on vertailuarvo, joka on määritelty nollaksi desibeliksi ja vastaa hyvin heikkoa, juuri ja juuri kuuluvaa ääntä. Eri sovelluksissa on kuitenkin olemassa myös erilaisia määritelmiä desibelille.

Kun laskuissa käytetään logaritmisia suureita, joutuu usein välivaiheena ratkaisemaan intensiteetin. Esimerkiksi kaksi 40 dB voimakkuudella toimivaa laitetta **eivät** tuota yhteensä 80 dB melua, vaan sellainen äänentason, joka muodostuu sijoittamalla desibelin määritelmään kaksinkertaisen **intensiteetin** ja laskemalla sitten kymmenkantaisen logaritmin.

::::{admonition} Esimerkki

Laulukuorossa on 50 jäsentä. Yksi ihminen laulaa noin 65 dB voimakkuudella. Millainen äänenvoimakkuus tulee koko kuorosta?

:::{admonition} Ratkaisu
:class: tip, dropdown

Ratkaistaan ensin yhden laulajan äänen intensiteetti $I$. Sievennetään yhtälöä ja sitten sovelletaan logaritmin määritelmää:

$\text{60}=10 \log{\frac{I}{I_0}}$

$\lg{\frac{I}{I_0}}=\frac{\text{65}}{10}$

$\lg{\frac{I}{I_0}}=6.5$

$\frac{I}{I_0}=10^{6.5}$

$I=I_0\cdot 10^{6.5}$

Saatiin siis intensiteetti $I$ ilmaistuna vertailuarvon ja desibelilukeman avulla. Vertailuarvon $I_0$ suuruutta ei tarvitse tietää, sillä desibelien laskukaavassa se on nimittäjässä ja siten supistuu kuitenkin pois. Yksittäisen laulajan äänen intensiteetti voidaan nyt kertoa laulajien määrällä ja sijoittaa takaisin desibelin laskukaavaan:

$\text{dB}=10 \lg{\frac{50\cdot I}{I_0}} = 10 \lg{\frac{50\cdot I_0 \cdot 10^{6.5}}{I_0}} = 10 \lg{(50\cdot 10^{6.5})} \approx 82$

:::

::::

::::{admonition} Esimerkki

Vahvistimen sisäänmeno- ja ulostulojännite $u_{\text{in}}$ ja $u_{\text{out}}$ liittyvät desibeleinä ilmaistuun vahvistukseen $D$ siten, että $D=20~\lg{(\frac{u_{\text{out}}}{u_{\text{in}}})}$. 

a) Kuinka monta desibeliä on vahvistus, jos sisään menevä jännite on 0.1 V ja vahvistettu jännite on 2 V? 

b) Kuinka moninkertaiseksi jännite voimistuu, jos vahvistus on 65 dB?

:::{admonition} Ratkaisu
:class: tip, dropdown

a) Vahvistus on $D=20~\lg{(\frac{2}{0.1})} \approx 26~\text{dB}$

b) Ratkaistaan $u_{\text{out}}$ yhtälöstä $65=20~\lg{(\frac{u_{\text{out}}}{u_{\text{in}}})}$:

$\frac{65}{20}=\lg{(\frac{u_{\text{out}}}{u_{\text{in}}})}$

$10^{\frac{65}{20}}=10^{\lg{\frac{u_{\text{out}}}{u_{\text{in}}}}}$

$10^{\frac{65}{20}}=\frac{u_{\text{out}}}{u_{\text{in}}}$

$u_{\text{out}}=10^{\frac{65}{20}}~u_{\text{in}}$ eli $u_{\text{out}} \approx 1778~u_{\text{in}}$ 

:::

::::


::::{admonition} Esimerkki logaritmisesta suureesta, jossa ei käytetä desibelejä

Kemiassa liuoksen happamuutta kuvaava pH-arvo on määritelty seuraavasti: $\text{pH}=-\lg{c}$, missä $c$ on hapon konsentraatio (tai oikeastaan hapon vesiliuokseen luovuttamien oksoniumionien konsentraatio - kemian oppikirjoissa on myös muunlaisia määritelmiä, mutta tämä riittää matematiikkaan). Konsentraatio kuvaa veteen liuenneiden hiukkasten määrää (yksikkönä mooli, lyhenne mol) jaettuna veden tilavuudella (yksikkönä litra). Konsentraatiot ovat yleensä hyvin pieniä lukuja. Esimerkiksi jos hapon konsentraatio on 0.00345 mol/l, niin pH on $-\lg{0.00345}\approx 2.5$. Mitä pienempi on pH-arvo, niin sitä happamampaa liuos on. Arvo 2.5 vastaa suunnilleen sitruunamehua tai colajuomaa.

Kuvitellaan, että kemistin pitää valmistaa happoliuosta, jonka pH on 3.5. Hän lisää veteen happoa siten, että hapon konsentraatio vastaa haluttua pH-arvoa. Lounastauon aikana hän unohtaa, että valmisti jo liuoksen, ja lisää veteen saman määrän happoa uudelleen. Tällöin konsentraatio kaksinkertaistuu. Mikä on liuoksen pH-arvo tämän virheen jälkeen?


:::{admonition} Ratkaisu
:class: tip, dropdown

Lasketaan ensin, mikä oli konsentraatio ensimmäisessä happoliuoksessa:

$3.5=-\lg{x}$ eli $-3.5=\lg{x}$

Korotetaan molemmat puolet luvun 10 eksponentiksi: $10^{-3.5}=10^{\lg{x}}$

Logaritmin määritelmän perusteella $x=10^{-3.5} \approx 0.000316$

Uusi konsentraatio on kaksinkertainen, ja uudeksi pH-arvoksi saadaan $-\lg{(2\cdot 0.000316)} \approx 3.2$

:::


::::

## Eksponenttiyhtälöt

Eksponenttiyhtälössä tuntematon $x$ esiintyy eksponentissa. Yhtälön ratkaisussa tarvitaan tällöin välivaihetta, jossa otetaan kummastakin puolesta logaritmi. Ei ole väliä, mikä on logaritmin kantaluku. Usein käytetään luonnollista logaritmia. Seuraavista esimerkeistä huomataan, että sovelluksia eksponenttiyhtälöille löytyy monilta aloilta taloustieteestä fysiikkaan. Esimerkiksi kofeiinin hajoamista ihmisen elimistössä voidaan myös mallintaa tällaisilla yhtälöillä. Tässä kuitenkin aluksi esimerkki ilman sen kummempaa sovellusta:

::::{admonition} Esimerkki

Ratkaise luku $x$ yhtälöstä $7^{3x}=15$.

:::{admonition} Ratkaisu
:class: tip, dropdown

Otetaan yhtälön kummastakin puolesta _mikä tahansa_ logaritmi, vaikkapa 10-kantainen logaritmi:

$\lg{7^{3x}}=\lg{15}$

Käytetään sääntöä $\lg{x^n}=n~\lg{x}$:

$3x~\lg{7}=\lg{15}$

Nyt yhtälö ratkeaa ihan suoraviivaisesti jakolaskulla:

$x=\frac{\lg{15}}{3\lg{7}}$ ja jos halutaan likiarvoinen ratkaisu, niin laskimella saadaaan $x\approx 0.464$. Laskin saattaa antaa myös sellaisia ratkaisuja, jotka ovat kompleksilukuja, mutta tässä yhteydessä ratkaisuksi riittää reaaliluku.

:::

::::



::::{admonition} Esimerkki

Rahaa talletetaan tilille 2000 euroa. Talletus kasvaa korkoa 4 % vuodessa. Toisin sanoen tilillä oleva rahamäärä kerrotaan joka vuoden lopussa luvulla 1.04. Tällöin vuoden jälkeen rahaa on $1.04\cdot 2000$ euroa, kahden vuoden jälkeen $1.04\cdot 1.04\cdot 2000$ euroa eli lyhyemmin kirjoitettuna $1.04^2 \cdot 2000$ euroa, kolmen vuoden jälkeen $1.04^3\cdot 2000$ euroa jne. ja yleisesti $x$ vuoden kuluttua $1.04^x\cdot 2000$ euroa. Kuinka pitkän talletusajan jälkeen tilillä oleva rahamäärä on kasvanut 3000 euroon? Laskussa ei tarvitse huomioida veroja, palvelumaksuja, inflaatiota  ym.

:::{admonition} Ratkaisu
:class: tip, dropdown

Ratkaistavana on yhtälö $1.04^x\cdot 2000=3000$. Sievennetään aluksi yhtälö jakamalla molemmat puolet luvulla $2000$:

$1.04^x = \frac{3000}{2000}$

$1.04^x = \frac{3}{2}$

Nyt otetaan logaritmi yhtälön molemmista puolista. Kantaluku voi olla mikä tahansa. Valitaan vaikka luonnollinen logaritmi:

$\ln{1.04^x}=\ln{\frac{3}{2}}$

Logaritmin laskusäännön $\log_a{x^n}=n \log_a{x}$ avulla saadaan tuntematon $x$ kertoimeksi yhtälön vasemmalle puolelle:

$x \ln{1.04}=\ln{\frac{3}{2}}$

Yhtälön molemmilla puolilla esiintyvät logaritmit ovat aivan tavallisia lukuja, joten $x$ saadaan selville jakolaskulla:

$x = \frac{\ln{\frac{3}{2}}}{\ln{1.04}}$ 

Laskimella saadaan tulos $x\approx 10.338$, eli hieman yli 10 vuotta. Ratkaisun voi tarkistaa sijoittamalla luvun alkuperäiseen yhtälöön: $1.04^{10.338}\cdot 2000 \approx 2999.996\dots$.

Sama tulos saataisiin, vaikka valittaisiin kantaluvuksi jokin muu kuin $e$, esimerkiksi $10$:

$x = \frac{\lg{\frac{3}{2}}}{\lg{1.04}} \approx 10.338$ 

:::

::::

::::{admonition} Esimerkki

Valon intensiteettiä $I$ jonkin ainekerroksen takana voidaan kuvata yhtälöllä $I=I_0~e^{kx}$, missä $I_0$ on alkuperäinen intensiteetti, $x$ on ainekerroksen paksuus ja $k$ on aineelle ominainen vaimennuskerroin. Oletetaan, että erään lammen pohjaa tutkitaan lampulla. Lammen vesi on sellaista, että kahden metrin syvyydessä valon intensiteetistä on jäljellä 20 % alkuperäisestä. Minkä verran intensiteetistä on jäljellä 4 metrin syvyydessä veden alla?

:::{admonition} Ratkaisu
:class: tip, dropdown

Vaimentunut intensiteetti on 20 % alkuperäisestä, joten voidaan kirjoittaa $I=0.2~I_0$. Tällöin ratkaistavaksi yhtälöksi muodostuu $0.2~I_0 = I_0~e^{k\cdot 2}$. Alkuperäinen intensiteetti $I_0$ supistuu pois, joten $0.2=e^{k\cdot 2}$. Ratkaistaan vaimennuskerroin $k$: 

$\ln{0.2}=\ln{e^{2k}}$

$\ln{0.2}=2k \ln{e}$

$\ln{0.2} = 2k$, koska $\ln{e} = 1$

Siis $k=\frac{\ln{0.2}}{2}\approx -0.80472$

Sijoitetaan sitten tämä luku ja uusi syvyys 4 m yhtälöön:

$I=I_0~e^{-0.80472\cdot 2}$ josta saadaan $I = 0.04~I_0$

Valon intensiteetistä on siis jäljellä 4 %.

:::

::::