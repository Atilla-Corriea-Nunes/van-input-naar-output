# Atilla Correia Nunes opdracht: Pizza Calculator


print("Welkom bij Atilla's pizzeria!") # dit is de begroeting voor de klant
print("Hoeveel pizza's wilt u?")
small, med, big = input ("Hoeveelheid small pizza's:"), input("Hoeveelheid medium pizza's:"), input("Hoeveelheid large pizza's:") # met deze code geeft de klant aan hoeveel pizza's zij willen

kosten1 = int(small) * 2.99 # deze code rekent de kosten op van alles
kosten2 = int(med) * 4.99
kosten3 = int(big) * 7.99
finalkost = int(kosten1) + int(kosten2) + int(kosten3)

print("Bedankt voor het bestellen! Uw kosten zullen "+ str(finalkost) +" euro zijn") # deze code verteld de klant hoeveel ze moeten betalen