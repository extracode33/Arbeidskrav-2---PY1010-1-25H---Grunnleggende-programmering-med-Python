"""
Arbeidskrav 2, oppgave 4a,b
Vidar Due (vidar_due@hotmail.com)
Oppdatert 2025.11.14

Det er opprettet en dictionary og programmet er laget for å kunne svare ut fakta om et spesifikt land.
Det er kun lagt til fire land i dette programmet der man kan skrive inn hvilket land man ønsker
ved å bruke funksjonen input.

"""

data = {"Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

land = input("Skriv inn et land:")   # Her skriver man inn hvilket land man ønsker info om

hovedstad = data[land][0]   # Hovedstad ligger på indeksplass 0 for det spesifikke landet
innbyggere = data[land][1]   # # Innbyggertall ligger på indeksplass 1 for det spesifikke landet

svar = f"{hovedstad} er hovedstaden i {land}, og det er {innbyggere} millioner innbyggere i {hovedstad}."
print(svar)   #Her er det brukt f-string for å kunne flette info i en setning/string



