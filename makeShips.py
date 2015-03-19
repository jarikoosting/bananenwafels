#!/opt/local/bin/python3.4

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

        self.botendic = {"Aircraft Carrier": 5, "Battleship": 4, "Submarine": 3, "Destroyer": 3, "Patrol Boat": 2}

        # Create buttons for playing game
        self.placeBtn = QtGui.QPushButton('Place Ship!', self)
        self.placeBtn.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 30px; width: 150px;}')

        self.directionBtn = QtGui.QPushButton('Horizontal!', self)
        self.directionBtn.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 30px; width: 150px;}')
        self.directionBtn.clicked.connect(self.direction)
        self.shipDirection = "Horizontal"

        self.placeAllBtn = QtGui.QPushButton('Submit Ships!', self)
        self.placeAllBtn.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 30px; width: 150px;}')
        self.placeAllBtn.clicked.connect(self.direction)

        #for lengteschip in lengteschepen:
            #self.makeShips(lengteschip)


        self.btnsDict = {}
        for row in range(10):
            for column in range(1, 11):
                coord = str(row)+"."+str(column)
                self.btnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.btnsDict[coord].setStyleSheet('QPushButton {background-color: white; margin: 0; height: 30px; '
                                                   'width: 30px;}')
                self.btnsDict[coord].clicked.connect(lambda c, x=row, y=column, btn=coord: self.btnPressed(x, y, btn))
                self.grid.addWidget(self.btnsDict[coord], row, column)

        self.grid.addWidget(self.placeBtn, 0, 0)
        self.grid.addWidget(self.directionBtn, 1, 0)
        self.grid.addWidget(self.placeAllBtn, 2, 0)
        self.show()

    def btnPressed(self, x, y, b):
        self.row = x
        self.column = y
        if b == "0.0" or b == "6.6":
            self.btnsDict[b].setStyleSheet('QPushButton {background-color: red; margin: 0; color: black; width: 30px;'
                                           'height: 30px;}')
            self.infoLabel.setText("hit a ship")
        else:
            self.btnsDict[b].setStyleSheet('QPushButton {background-color: lightblue; margin: 0; color: black; '
                                           'width: 30px; height: 30px;}')

    def createShip(self):
        self.lenShips = list(self.botendic.values())
        self.lenShips.sort()
        # for loopje door de lijst
        lenShips = self.lenShips.pop()
        self.makeShip(lenShips)
        return lenShips

    def makeShip(self, lenShips):
        """
        this function creates the ships and gives a list of coordinates back of where the 5 ships are
        """
        #initialisatie van de waarden

        self.startship = (self.row, self.column)

        print("lengte schip is", lenShips, "blokjes")

        #richting schip
        if self.shipDirection == "Horizontal":
            self.row = self.row + lenShips

        else:
            self.column = self.column + lenShips

        self.endship = (self.row, self.column)

        self.shipsList=[]
        self.shipsList.append(self.startship)
        self.shipsList.append(self.endship)

    def setAllShips(self):
        coords = {}

        #coords = {"Aircraft Carrier":[(9,2),(9,3),(9,4),(9,5)], "Battleship":[(1,1)]}
        for ship in self.botendic:
            coords[ship] = self.shipsList
        print(coords)

        return coords

    def direction(self, pressed):
        """
        This function gets the direction of  the ship from the user and changes the label of the button
        """
        source = self.sender()
        if pressed:
            source.setText("Horizontal")
            self.shipDirection = "Horizontal"
        else:
            source.setText("Vertical")
            self.shipDirection = "Vertical"

    def checkBoundaries(self):

        if self.shipDirection == "Horizontal" and self.lenShips + self.row > 10:
            return False
        elif self.shipDirection == "Vertical" and self.lenShips + self.column > 10:
            return False

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