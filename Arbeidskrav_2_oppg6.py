"""
Arbeidskrav 2, oppgave 6
Vidar Due (vidar_due@hotmail.com)
Oppdatert 2025.11.14

Dette programmet plotter funksjonen med verdiene for x og y som gitt under

"""


import numpy as np

import matplotlib.pyplot as plt   # Henter funksjon for å kunne plotte og lage grafer 

x = np.linspace(-10, 10, 200)   # Lager x-verdier fra -10 til 10 med 200 punkter

y = (-x)**2 - 5   # Definerer y-funksjonen (-x)^2 - 5

plt.plot(x,y)   #Plotter grafen