#!/usr/bin/env python
# coding: utf-8

# # Testailusivu
# 
# Tälle sivulle tulee Python-ohjelmointisoluja. Sivu täydentyy!
# 
# Osoita hiirellä sivun oikean yläreunan raketti-kuvaa. Valitse Live Code. 
# 
# Voit muokata koodisoluja vapaasti. Koodi suoritetaan koodisolun alareunan **run**-nappulasta.
# 
# ## Funktion siirto
# 
# Testaa, miten funktion kuvaajaa siirretään vaaka- ja pystysuunnassa.

# In[1]:


from sympy import Function, Symbol
from sympy.plotting import plot
x = Symbol('x')

# Mitä funktiota siirretään?
f = 4*x**2+2

# Kuinka paljon siirretään vaakasuunnassa?
a = 3

# Kuinka paljon siirretään pystysuunnassa?
b = 4

# Siirretty funktio: korvataan x luvulla x+a, ja lisätään b
g=f.subs(x,x+a)+b

# Komennot xlim ja ylim  säätävät piirtoalueen rajoja, voit muokata niitä
# Komennot voi myös poistaa, tällöin piirtoalue skaalautuu automaattisesti
x1, x2 = -5, 5
y1, y2 = 0, 10

# Komento p1.extend(p2) yhdistää kuvaajat ja komento p1.show() näyttää ne samassa kuvassa
# Komento show=False aiheuttaa sen, että ei tule kahta erillistä kuvaa
p1=plot(f, xlim=(x1, x2), ylim=(y1, y2), show=False)
p2=plot(g, xlim=(x1, x2), ylim=(y1, y2), show=False, line_color="g")
p1.extend(p2)
p1.show()


# ## Raja-arvot
# 
# Tällä työkalulla voit laskea funktioiden raja-arvoja ja tarkastella funktion kuvaajaa.

# In[ ]:


import sympy
x = sympy.Symbol('x')

# Minkä funktion raja-arvoa lasketaan?
f = x/(x-3)

# Missä pisteessä raja-arvo lasketaan?
# Huom! Ääretön merkitään 'oo' (lainausmerkit oltava mukana)
x0 = 3

# Raja-arvon laskeminen
raja_arvo=sympy.limit(f,x,x0)
print("Funktion", f, "raja-arvo pisteessä", x0, "on", raja_arvo)

# Komennot xlim ja ylim  säätävät piirtoalueen rajoja, voit muokata niitä
x1, x2 = 1, 5
p1=sympy.plotting.plot(f, xlim=(x1, x2),show=True)

