#!/opt/local/bin/python3

from PyQt4 import QtGui, QtCore
import sys
"""
This function places the ships on the board of the user
"""
class Battleships(QtGui.QWidget):
    def __init__(self):
        """
        Constructs a Battleship game object, with which the user can play a game.
        """
        super(Battleships, self).__init__()
        self.initUI()

    def initUI(self):
        """
        Constructs the UI with a 2 grids, multiple buttons and labels.
        """

        #Create window and create grid layout
        self.setWindowTitle("Battleships")
        self.setGeometry(150, 150, 600, 600)
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)

        self.botendic= {"Aircraft Carrier":5,"Battleship":4,"Submarine":3,"Destroyer":3,"Patrol Boat":2}

        self.richting=QtGui.QPushButton('Horizontaal',self)
        self.richting.move(10,10)
        self.richting.setCheckable(True)
        self.richting.clicked.connect(self.direction)

        self.setship=QtGui.QPushButton('Plaats schip!',self)
        self.setship.move(100,10)
        self.setship.clicked.connect(self.setShips)
        lengteschip=int(3)
        self.btnsDict = {}
        for row in range(10):
            for column in range(10):
                coord = str(row)+"."+str(column)
                self.btnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                # andere functie maken om te checken of alle boten zijn aangeklikt, en als er geen 5 elementen zijn
                # dan dit zeggen en als ze er wel zijn pas naar makeShips gaan.
                self.btnsDict[coord].clicked.connect(lambda c, x=row, y=column: self.makeShips(x, y,lengteschip))
                self.grid.addWidget(self.btnsDict[coord], row, column)

        #dus eigenlijk een grote loop maken met alle waardes die ik nu krijg, hoe doe je dat?
        lengteschepen=list(self.botendic.values())
        lengteschepen.sort()
        #for lengteschip in lengteschepen:
            #self.makeShips(x,y,lengteschip)

        self.show()

    def makeShips(self,x,y,lengteschip):
        """
        this function creates the ships and gives a list of coordinates back of where the 5 ships are
        """
        #initialisatie van de waarden
        rij=x
        kolom=y
        richting=self.richting
        self.startship=(x,y)

        print("lengte schip is", lengteschip, "blokjes")

        if richting == "horizontaal":
            rij=rij+(lengteschip)

        else:
            kolom=kolom+(lengteschip)

        self.endship=(rij,kolom)

        # coordinaten van het hele schip uitrekenen, in een for loop


    def direction(self,pressed):
        """
        This function gets the direction of  the ship from the user and changes the label of the button
        """
        source=self.sender()
        if pressed:
            source.setText("horizontaal")
            self.richting="horizontaal"
        else:
            source.setText("verticaal")
            self.richting="verticaal"

    def setShips(self):
        #deze functie aanroepen als alles al is geplaatst
        # Dan dus de coordinaten in een dictionairy: schip en dan coordinaten met lijst erachter.
        self.lijstships=[]
        self.lijstships.append(self.startship)
        self.lijstships.append(self.endship)
        print("de coordinaat van het geplaatste schip is ",self.lijstships)

        coords={}

        coords = {"Aircraft Carrier":[(9,2),(9,3),(9,4),(9,5)], "Battleship":[(1,1)]}
        for ship in self.botendic:
            coords[ship]=self.lijstships
        print(coords)

        return coords

    #def validate(self,board,ship,x,y,ori):3
    #validate the ship can be placed at given coordinates
    #if ori == "v" and x+ship > 10:
        #return False
    #elif ori == "h" and y+ship > 10:
        #return False
    #else:
        #if ori == "v":
            #for i in range(ship):
              #if board[x+i][y] != -1:
                    #return False
        #elif ori == "h":
            #for i in range(ship):
                #if board[x][y+i] != -1:
                    #return False

    def checkShips(self):
        """
        Check if a ship has been hit
        After placement, if the user clicks, it goes to this function!
        """
        coords = {"Aircraft Carrier":[(9,2),(9,3),(9,4),(9,5)], "Battleship":[(1,1)]}
        click = (9,10)

        # Loop through dictionary with ships and coords
        for ship, coord in coords.items():
            for el in coord:
                if click == el:
                    coord.remove(el)

                    # Check if ship is destroyed after the hit
                    Battleships.checkDestroyed(self,coords)
                    return True

        # None of the ships got a hit!
        return False

    def checkDestroyed(self,coords):
        """
        Check if a ship is destroyed
        """

        # Return True when ship is destroyed
        for ship, coord in coords.items():
            if coords.get(ship) == []:
                return ship, True

        # None of the ships are destroyed
        return False

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    game = Battleships()
    game.show()
    app.exec_()





