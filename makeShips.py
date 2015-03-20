#!/opt/local/bin/python3.4

from PyQt4 import QtGui, QtCore
import sys


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

        # Create a dictonairy with ships, an empty dictonairy for ships with coords and a list for the lengts of the
        # boats.
        self.shipDic = {5: "Aircraft Carrier", 4: "Battleship", 3: "Submarine", 2: "Patrol Boat"}
        self.boatCoords = {}
        self.boatLengths = list(self.shipDic.keys())

        # Create button for placing ships
        self.placeBtn = QtGui.QPushButton('Place Ship!', self)
        self.placeBtn.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 30px; width: 150px;}')
        self.placeBtn.clicked.connect(self.submitShip)

        # Create button for placing ships vertically or horizontally
        self.directionBtn = QtGui.QPushButton('Horizontal', self)
        self.directionBtn.setStyleSheet('QPushButton {background-color: orange; margin: 0; '
                                        'height: 30px; width: 150px;}')
        self.directionBtn.clicked.connect(self.direction)

        # Create button for starting game
        self.placeAllBtn = QtGui.QPushButton('Start Game!', self)
        self.placeAllBtn.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 30px; width: 150px;}')
        #self.placeAllBtn.clicked.connect(self.setAllShips)

        # Create a dictionary for buttons, and create 100 buttons for the board
        self.btnsDict = {}
        for row in range(10):
            for column in range(1, 11):
                # Make a unique variable name bij adding de coordinates together in a string
                #coord = str(row)+"."+str(column)
                coord = (row, column)
                self.btnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.btnsDict[coord].setStyleSheet('QPushButton {background-color: white; margin: 0; height: 30px; '
                                                   'width: 30px;}')
                # Connect the button to a _method_ where x and y are specified by using lambda
                self.btnsDict[coord].clicked.connect(lambda c, x=row, y=column: self.placeShip(x, y))
                self.grid.addWidget(self.btnsDict[coord], row, column)

        # Add other buttons to grid
        self.grid.addWidget(self.placeBtn, 0, 0)
        self.grid.addWidget(self.directionBtn, 1, 0)
        self.grid.addWidget(self.placeAllBtn, 2, 0)
        self.show()

    def placeShip(self, x, y):
        """
        This function does all the work. If a button is pressed, it generates the coordinates for a ship and makes
        the surrounding buttons red.
        """
        self.row = y
        self.column = x
        self.shipCoords = self.generateShip(self.boatLengths[0])
        self.clearBtns()
        for i in self.shipCoords:
            self.colorBtn(i, "red")

    def generateShip(self, boatLength):
        """
        This function generates the coordinates for every boat, depending of the lenght.
        """
        coordsList = []
        if self.directionBtn.text() == "Horizontal":
            for i in range(boatLength):
                coordsList.append((int(self.column), int(self.row) + int(i)))
        elif self.directionBtn.text() == "Vertical":
            for i in range(boatLength):
                coordsList.append((int(self.column) + int(i), int(self.row)))
        return coordsList

    def submitShip(self):
        """
        Places the ship and its coordinates in a dictionary.
        """
        self.boatCoords[self.shipDic[self.boatLengths[0]]] = self.shipCoords
        self.boatLengths.pop(0)
        print(self.boatCoords)

    def colorBtn(self, coord, color):
        """
        Colors buttons red or white.
        """
        #b = str(coord[0]) + "." + str(coord[1])
        self.btnsDict[coord].setStyleSheet('QPushButton {background-color: %s; margin: 0; color: black; width: 30px; '
                                           'height: 30px;}' % color)

    def clearBtns(self):
        """
        Clears buttons, everything will be white again.
        """
        for b in self.btnsDict:
            if b in self.boatCoords.values():
                self.btnsDict[b].setStyleSheet('QPushButton {background-color: %s; margin: 0; height: 30px; '
                                               'width: 30px;}' % "white")

    def direction(self):
        """
        This function gets the direction of  the ship from the user and changes the label of the button
        """
        if self.directionBtn.text() == "Horizontal":
            self.directionBtn.setText("Vertical")
        else:
            self.directionBtn.setText("Horizontal")
        for i in self.shipCoords:
            self.colorBtn(i, "white")

    def checkBoundaries(self):
        """
        Check of a ship is placed within the board
        """
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
        click = (self.row,self.column)

        # Loop through dictionary with ships and coords
        for ship, coord in coords.items():
            for el in coord:
                if click == el:
                    coord.remove(el)

                    # Check if ship is destroyed after the hit
                    Battleships.checkDestroyed(self, coords)
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