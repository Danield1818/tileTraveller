#Hugmindin okkar að þessu vandamáli
#segja fyrst notendanum hvert hann getur farið
#Ef notandi slær inn annað en það sem hann má slá inn mun prentast "Not a valid direction"
#Gera breytu sem heitir victory og gefa henni gildið False
#Þegar notandi er kominn á lokareit í leiknum mun þá victory breytan breytast í True
#Búa til breytu sem yrði þá byrjendarreitur notendans (1, 1)
#Gera lykkju sem keyrir leikinn þegar victory != False
#Skrifa svo hvert notandi getur farið á hverjum reit fyrir sig undir if-setningum sem spyrja ef directionið er valid
#og hvert hann væri þá að fara.
#ef suður þá færist hann neðar ef norður, ef austur þá hægri og ef vestur þá vinstri.

x = 1
y = 1

valid_direction = "nN"

start = (x, y)
victory = False
print ("You can travel: (N)orth.")

if not direction in valid_direction:
        print("Not a valid direction!")
    else:
        if direction == "s" or direction == "S":
            y -= 1
            start = (x, y)

        elif direction == "n" or direction == "N":
            y += 1
            start = (x, y)
        
        elif direction == "w" or direction == "W":
            x -= 1
            start = (x, y)
            
        elif direction == "e" or direction == "E":
            x += 1
            start = (x, y)
        

 
