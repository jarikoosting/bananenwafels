#!/opt/local/bin/python3

from PyQt4 import QtGui, QtCore
import sys
"""
This function places the ships on the board of the user
"""
class Test(QtGui.QWidget):
    def __init__(self):
        """creert interface en unigrammen"""
        super(Test,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 500)
        self.setWindowTitle("Unigrammen")
        self.show

def userPlaceShips(board, ships):
    for ship in ships.keys() #schepen moeten dus dictionairy zijn

        valid = False  #initaliseer waarde, aangeroepen met andere functie
        while (not valid):
            # Mouseevent en haal hier de x & y uit en geef deze weer aan de getCoords functie

            # Laat zien dat je een schip kan plaatsen dmv van een qlabel ofzo?

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
    return coord

def mouseEvent(self, QMouseEvent):
        cursor =QtGui.QCursor()
        position= cursor.pos()
        return position

if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    interface=Test()
    interface.show()
    app.exec_()

