__author__ = 'Laurence'

"""
This function places the ships on the board of the user
"""


def userPlaceShips(board, ships):
    for ship in ships:  # lijst of dic ofzo? wat zijn de schepen?

        # get coordinates from the user and validate if position is correct
        valid = False
        while (not valid):
    # Laat zien dat je schip kan plaatsen dmv van popup oid
    # verififeer waar de gebruiker heeft geklikt met x & y, roep hier functie getCoords aan met userinput
    # vraag ook aan de gebruiker of het schip horizontaal of verticaal moet worden geplaatst
    # kijk of dit schip past: validate functie aanroepen met parameters
    # als het niet past, laat nieuwe popup met foutmeldingen zien

    #plaats het schip, roep hiervoor de functie plaats schip aan met parameters vled, schip, orientatie & coordinaten

    # return ingevoerde coordinaten in het speelveld


def getCoords(userinput):
    # see that user entered 2 values seprated by comma
    coor = userinput.split(",")
    if len(coor) != 2:
        # laat weten dat de invoer qua getallen niet klopt

    # Maak van de invoer getallen
    coor[0] = int(coor[0])
    coor[1] = int(coor[1])

    #check that values of integers are between 1 and 10 for both x and y
    if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
       # laat hier ook weten dat je getallen binnen de 1 en 10 moet invoeren

    #klopt alles, geef dan coordinaten terug (joepie!)
    return coor


