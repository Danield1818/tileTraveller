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


#Commentin:

#Which implementation was easier and why?
#Ég myndi segja að fyrra implementationið var auðveldara 
#þar sem hugsunin var einfaladri fannst mér og auðveldara að fá kóðann til að gera það sem að ég vildi að hann myndi gera

#Which implementation is more readable and why?
#Seinni implementationið með föllunum er mun lesanlegara, einfaldlega vegna þess að kóðinn er ekki eins clusteraður.

#Which problems in the first implementations were you able to solve with the latter implementation?
#föllin leystu aðalega eitt vandamál, sem var ólesanlegur kóði og kanski óþarfa flókinn kóði.

x = 1
y = 1

valid_direction = "nN"

start = (x, y)

def game(m):
    if start == (2, 1):
        print("You can travel: (N)orth.")
        m = "nN"
    elif start == (2, 2):
        print("You can travel: (S)outh or (W)est.")
        m = "wWsS"
    elif start == (2, 3):
        print("You can travel: (E)ast or (W)est.")
        m = "wWeE"
    elif start == (3, 3):
        print("You can travel: (S)outh or (W)est.")
        m = "sSwW"
    elif start == (3, 2):
        print("You can travel: (N)orth or (S)outh.")
        m = "nNsS"
    elif start == (1, 1):
        print("You can travel: (N)orth.")
        m = "nN"
    elif start == (1, 3):
        print("You can travel: (E)ast or (S)outh.")
        m = "NnsSeE"
    elif start == (1, 2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        m = "nNeEsS"
    return m


while start != (3, 1):

    valid_direction = game(valid_direction)
    direction = input("Direction: ")

    while direction not in valid_direction:
        print("Not a valid direction!")
        direction = input("Direction: ")

    if direction in valid_direction:
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

print("Victory!")

#Git link https://github.com/Danield1818/tileTraveller.git