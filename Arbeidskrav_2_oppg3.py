"""
Arbeidskrav 2, oppgave 3
Vidar Due (vidar_due@hotmail.com)
Oppdatert 2025.11.14

Programmet skal regne om fra grader til radianer ved bruk av input.

"""


import numpy as np

v_grad = float(input("Skriv inn gradtallet:"))  # her legger man inn gradtallet man ønsker å regne om

v_rad = v_grad*np.pi/180   # formel for å regne ut radian ut i fra gradtallet

print(v_grad, "grader tilsvarer radiantallet", round(v_rad,2))   # radiantallet blir svart ut med to desimaler