tekst = "Fortnite is en erg grote game. Die vooral populair is onder jongeren."
#0 is eerste getal

#wannneer while? Gebruiken we als we niet van te voren weten hoe vaak het moet gebeuren

#for teller in range(len(tekst)): # is gelijk aan (0, 1, 2, 3, 4, 5) teller wordt voor iedere iteratie gevuld met de waarde die aan de buurt is: van links naar rechts
#       
#    print(tekst[teller])
    
count_e = 0

for e in tekst:
    if e.lower() == 'e':
        count_e += 1

        
print(count_e)