# name of student: 
# number of student:
# purpose of program: 
# structure of program: 

coinValues = [500,200,100,50,20,10,5,2,1] #

returnedCoins = {coinValue: 0 for coinValue in coinValues}

toPay = int(float(input('Amount to pay: '))* 100) # reken waarde uit to pay x 100 //
paid = int(float(input('Paid amount: ')) * 100) # reken waarde uit paid x 100 // omdat het centen zijn moet het naar 1 worden 
change = paid - toPay # rekent uit hoeveel geld er terug moet geven worden 

while change > 0 and len(coinValues) > 0: #

  coinValue = coinValues.pop(0) # haalt steeds 1 waarde uit de list weg 
  nrCoins = change // coinValue # maakt een floor divion en kijk wat het maximale getal is wat je terug kan geven 

  if nrCoins > 0: #
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # dit geeft aan hoeveel de klant maiximaal kan wisselen van het bepaalde bedrag per waarde, als je 700 en 900 betaald kan je 40 x 500 doen en dan is je wisselgeld op dat geeft dit aan hoeveel je kunt innen
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # vraagt hoeveel je terug wilt van de waarde uit de lijst 
    change -= nrCoinsReturned * coinValue # de hoeveel coins keer de waarde berekenen en dat min de wisselgeld
    returnedCoins[coinValue] += nrCoinsReturned

print('<-------- Coins returning ------->')
for coinValue, count in returnedCoins.items():
    print(f'{count} coins of {coinValue} cents returned')

if change > 0: # als er nog  wisselgeld is nadat je alles heb ingevuld laat hij zien wat je mist
  print('Change not returned: ', str(change) + ' cents') #
else:
  print('done')