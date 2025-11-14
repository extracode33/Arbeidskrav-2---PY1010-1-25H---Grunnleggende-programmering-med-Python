"""
Arbeidskrav 2, oppgave 2
Vidar Due (vidar_due@hotmail.com)
Oppdatert 2025.11.14

Programmet skal regnet ut hvor mange pizzaer man trenger ut i fra antall elever som deltar på klassefest. 
Man kan kun kjøpe hele pizzaer, og hver elev spiser 1/4 pizza.

"""
import math

antall_elever = int(input("Skriv inn antall elever:"))   # antall elever som skal delta på klassefest

antall_pizzaer = math.ceil((antall_elever/4))  # bruker math.ceil for å runde opp

print("Det må handles inn", (antall_pizzaer), "pizzaer til festen")
