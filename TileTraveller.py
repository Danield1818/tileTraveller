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


while not victory:
    
    direction = input("Direction: ")

    if not direction in valid_direction:
        print("Not a valid direction!")
    else:
        if direction == "s" or direction == "S":
            y -= 1
            start = (x, y)
            
            if start == (2, 1):
                print("You can travel: (N)orth.")
                valid_direction = "nN"
            elif start == (3, 1):
                print("Victory!")
                victory = True
            elif start == (2, 2):
                print("You can travel: (S)outh or (W)est.")
                valid_direction = "wWsS"
            elif start == (2, 3):
                print("You can travel: (E)ast or (W)est.")
                valid_direction = "wWeE"
            elif start == (3, 3):
                print("You can travel: (S)outh or (W)est.")
                valid_direction = "sSwW"
            elif start == (3, 2):
                print("You can travel: (N)orth or (S)outh.")
                valid_direction = "sSnN"
            elif start == (1, 1):
                print("You can travel: (N)orth.")
                valid_direction = "nN"
            elif start == (1, 3):
                print("You can travel: (E)ast or (S)outh.")
                valid_direction = "sSeE"
            elif start == (1, 2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_direction = "nNeEsS"

        elif direction == "n" or direction == "N":
            y += 1
            start = (x, y)
        
            if start == (2, 1):
                print("You can travel: (N)orth.")
                valid_direction = "nN"
            elif start == (3, 1):
                print("Victory!")
                victory = True
            elif start == (2, 2):
                print("You can travel: (S)outh or (W)est.")
                valid_direction = "wWsS"
            elif start == (2, 3):
                print("You can travel: (E)ast or (W)est.")
                valid_direction = "wWeE"
            elif start == (3, 3):
                print("You can travel: (S)outh or (W)est.")
                valid_direction = "sSwW"
            elif start == (3, 2):
                print("You can travel: (N)orth or (S)outh.")
                valid_direction = "sSnN"
            elif start == (1, 1):
                print("You can travel: (N)orth.")
                valid_direction = "nN"
            elif start == (1, 3):
                print("You can travel: (E)ast or (S)outh.")
                valid_direction = "sSeE"
            elif start == (1, 2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_direction = "nNeEsS"

        elif direction == "w" or direction == "W":
            x -= 1
            start = (x, y)

            if start == (2, 1):
                print("You can travel: (N)orth.")
                valid_direction = "nN"
            elif start == (3, 1):
                print("Vicotry!")
                victory = True
            elif start == (2, 2):
                print("You can travel: (S)outh or (W)est.")
                valid_direction = "wWsS"
            elif start == (2, 3):
                print("You can travel: (E)ast or (W)est.")
                valid_direction = "wWeE"
            elif start == (3, 3):
                print("You can travel: (S)outh or (W)est.")
                valid_direction = "sSwW"
            elif start == (3, 2):
                print("You can travel: (N)orth or (S)outh.")
                valid_direction = "sSnN"
            elif start == (1, 1):
                print("You can travel: (N)orth.")
                valid_direction = "nN"
            elif start == (1, 3):
                print("You can travel: (E)ast or (S)outh.")
                valid_direction = "sSeE"
            elif start == (1, 2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_direction = "nNeEsS"

        elif direction == "e" or direction == "E":
            x += 1
            start = (x, y)

            if start == (2, 1):
                print("You can travel: (N)orth.")
                valid_direction = "nN"
            elif start == (3, 1):
                print("You are victorious!")
                victory = True
            elif start == (2, 2):
                print("You can travel: (S)outh or (W)est.")
                valid_direction = "wWsS"
            elif start == (1, 1):
                print("You can travel: (N)orth.")
                valid_direction = "nN"
            elif start == (2, 3):
                print("You can travel: (E)ast or (W)est.")
                valid_direction = "wWeE"
            elif start == (3, 3):
                print("You can travel: (S)outh or (W)est.")
                valid_direction = "sSwW"
            elif start == (3, 2):
                print("You can travel: (N)orth or (S)outh.")
                valid_direction = "sSnN"
            elif start == (1, 3):
                print("You can travel: (E)ast or (S)outh.")
                valid_direction = "sSeE"
            elif start == (1, 2):
                print("You can travel: (N)orth or (E)ast or (S)outh.")
                valid_direction = "sSeEnN"