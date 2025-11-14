"""
Arbeidskrav 2, oppgave 5
Vidar Due (vidar_due@hotmail.com)
Oppdatert 2025.11.14

Programmet er laget for å regne ut areal og omkrets av en gitt figur som består av en rettvinklet trekant og en halvsirkel.


"""

import numpy as np

a = float(input("Skriv inn verdien for a:"))   # legger inn verdi for katet(side) a, dette er også diameter for halvsirkelen
b = float(input("Skriv inn verdien for b:"))   # legger inn verdi for katet(side) b
radius = (a/2)   # regner ut radius for halvsirkel 

areal_halvsirkel = (np.pi * radius**2)/2   # bruker formel for areal sirkel, deler på 2 fordi vi kun skal måle halve sirkelen
omkrets_halvsirkel = (2*np.pi*radius)/2   # bruker formel for omkrets sirkel, deler på 2 fordi vi kun skal måle halve sirkelen
areal_trekant = (a*b)/2   # formel for å finne areal av trekant
c = np.sqrt(a**2 + b**2)   # regner ut hypotenusen(den lengste siden i en rettvinklet trekant) som her er kalt c
omkrets_trekant = a + b + c   # regner ut omkrets av trekanten

areal_figur = round((areal_halvsirkel + areal_trekant), 2)   # regner ut areal av halvsirkelen pluss trekant. Runder ned til 2 desimaler
omkrets_figur = round((omkrets_halvsirkel + omkrets_trekant - a), 2)   # regner ut omkrets av halvsirkel og trekant, side a er trukket i fra siden den ikke er den del av omkretsen for hele figuren. Runder ned til 2 desimaler.

print(f"Arealet til figuren er: {areal_figur}, Omkretsen til figuren er: {omkrets_figur}")

