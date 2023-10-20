gastheer = input("Wie is de gastheer? ")
gasten = False #aanpassen als de aanwezigheid hiervan is
drank = True   #aanpassen als de aanwezigheid hiervan is
chips = True   #aanpassen als de aanwezigheid hiervan is 

if ((gastheer == "bjorn" or gastheer == "slemmers") and drank) or (gasten and chips and drank) or (gasten and gastheer and drank):
    print('Start the Party')
else:
    print('No Party')
 