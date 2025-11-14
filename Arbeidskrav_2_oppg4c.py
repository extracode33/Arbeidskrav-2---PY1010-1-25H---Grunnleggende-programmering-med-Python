"""
Arbeidskrav 2, oppgave 4c
Vidar Due (vidar_due@hotmail.com)
Oppdatert 2025.11.14

Det er opprettet en dictionary og programmet er laget for å kunne legge til et nytt land med info om hovedstad og innbyggere

"""

data = {"Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

nytt_land = input("Skriv inn et nytt land: ")   # Nytt land man ønsker å legge til dictionary
hovedstad = input(f"Hva er hovedstaden i {nytt_land}? ")   # Hovedstad til det nye landet
innbyggere = float(input(f"Hvor mange millioner innbyggere er det i {hovedstad}? "))   # Innbyggertall til det nye landet

data[nytt_land] = [hovedstad, innbyggere]   # Alle nye inputs blir dermed lagt til den eksisterende dictionarien

print(data)   # Oppdatert dictionary blir fremvist