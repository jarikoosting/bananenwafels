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
        self.richting.move(100,0)
        self.richting.setCheckable(True)
        self.richting.clicked.connect(self.direction)

        #for lengteschip in lengteschepen:
            #self.makeShips(lengteschip)

        self.setship=QtGui.QPushButton('Plaats schip!',self)
        self.setship.move(200,0)
        self.setship.clicked.connect(self.makeShip)

        self.setship=QtGui.QPushButton("Plaats alles!",self)
        self.setship.move(300,0)
        self.setship.clicked.connect(self.setAllShips)


        self.btnsDict = {}
        for row in range(10):
            for column in range(10):
                coord = str(row)+"."+str(column)
                self.btnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.btnsDict[coord].setStyleSheet('QPushButton {background-color: white; color: black; width: 60px;'
                                                   'height: 60px;}')
                self.btnsDict[coord].clicked.connect(lambda c, x=row, y=column, btn=coord: self.btnPressed(x, y, btn))
                self.grid.addWidget(self.btnsDict[coord], row, column)

        self.show()

    def btnPressed(self, x, y, b):
        self.rij=x
        self.kolom=y
        if b == "0.0" or b == "6.6":
            self.btnsDict[b].setStyleSheet('QPushButton {background-color: red; color: black; width: 60px;'
                                           'height: 60px;}')
            self.infoLabel.setText("hit a ship")
        else:
            self.btnsDict[b].setStyleSheet('QPushButton {background-color: blue; color: black; width: 60px;'
                                           'height: 60px;}')

    def createShip(self):
        self.lengteschepen=list(self.botendic.values())
        self.lengteschepen.sort()
        lengteschip=self.lengteschepen.pop()
        self.makeShip(lengteschip)
        return lengteschip

    def makeShip(self,lengteschip):
        """
        this function creates the ships and gives a list of coordinates back of where the 5 ships are
        """
        #initialisatie van de waarden

        richting=self.richting
        self.startship=(self.rij, self.kolom)

        print("lengte schip is", lengteschip, "blokjes")

        #richting schip
        if richting == "horizontaal":
            self.rij=self.rij+(lengteschip)

        else:
            self.kolom=self.kolom+(lengteschip)

        self.endship=(self.rij,self.kolom)

        self.lijstships=[]
        self.lijstships.append(self.startship)
        self.lijstships.append(self.endship)

    def setAllShips(self):
        coords={}

        #coords = {"Aircraft Carrier":[(9,2),(9,3),(9,4),(9,5)], "Battleship":[(1,1)]}
        for ship in self.botendic:
            coords[ship]=self.lijstships
        print(coords)

        return coords

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