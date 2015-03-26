#!/opt/local/bin/python3.4
# voor linux
#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
import os, sys
import time
from random import randrange
import makeShips


class BSGame(QtGui.QWidget):
    def __init__(self, usrBoatCoordinates, botBoatCoordinates):
        """
        Constructs a Battleship game object, with which the user can play a game.
        """
        super(BSGame, self).__init__()
        self.usrBoatCoords = usrBoatCoordinates
        self.botBoatCoords = botBoatCoordinates
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

        self.firedCoords = []

        # Read QSS file for styles
        self.stylesheet = open(os.getcwd() + '/styles.qss').read()

        # Create label for the user field
        self.userLabel = QtGui.QLabel('Your field:')

        # Create label for the bot field
        self.botLabel = QtGui.QLabel('Enemy field:')
        self.botLabel.setObjectName('EnemyFeedback')
        self.botLabel.setStyleSheet(self.stylesheet)

        # Feedback with actions
        self.feedbackLabel = QtGui.QLabel('')
        self.feedbackLabel.setObjectName('FeedbackLabel')
        self.feedbackLabel.setStyleSheet(self.stylesheet)

        # Create a dictionary for buttons, and create 100 buttons for the board
        self.userBtnsDict = {}
        for row in range(10):
            for column in range(1, 11):
                # Make a unique variable name bij adding de coordinates together in a string
                coord = (row, column)
                self.userBtnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.userBtnsDict[coord].setStyleSheet(self.stylesheet)
                self.userBtnsDict[coord].setObjectName('Tile')
                self.grid.addWidget(self.userBtnsDict[coord], row, column)

        self.botsBtnsDict = {}
        for row in range(10):
            for column in range(12, 22):
                # Make a unique variable name bij adding de coordinates together in a string
                coord = (row, column)
                self.botsBtnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.botsBtnsDict[coord].setStyleSheet(self.stylesheet)
                self.botsBtnsDict[coord].setObjectName('Tile')
                # Connect the button to a _method_ where x and y are specified by using lambda
                self.botsBtnsDict[coord].clicked.connect(lambda c, x=row, y=column: self.fire(x, y))
                self.grid.addWidget(self.botsBtnsDict[coord], row, column)


        # Add other buttons to grid
        self.grid.addWidget(self.userLabel, 0, 0)
        self.grid.addWidget(self.botLabel, 0, 11)
        self.grid.addWidget(self.feedbackLabel, 4, 11)
        self.manageShips()
        self.show()

    def fire(self, x, y):
        self.feedbackLabel.setText('')
        self.checkShips(x, y, self.botBoatCoords, self.botsBtnsDict, 'You')
        autox, autoy = self.randomShoot()
        self.checkShips(autox, autoy, self.usrBoatCoords, self.userBtnsDict, 'Computer')

        if self.botBoatCoords == {} or self.usrBoatCoords == {}:
            for b in self.botsBtnsDict:
                    self.btnsDict[b].setEnabled(False)
            self.btnRestart = QtGui.QPushButton('Restart Game')
            self.btnRestart.setObjectName('MenuButton')
            self.btnRestart.setStyleSheet(self.stylesheet)
            self.grid.addWidget(self.btnRestart, 12, 11)
            self.btnRestart.clicked.connect(self.restart)

    def randomShoot(self):
        """
        Function that generates random coordinations.
        Needs randrange() from random module.
        """
        c = 1
        while c == 1:
            coord = (randrange(10), randrange(1,11))
            c = self.checkCoord(coord)
            if c == 2:
                self.firedCoords.append(coord)
                return coord[0], coord[1]

    def checkCoord(self, coord):
        if coord in self.firedCoords:
            return 1
        else:
            return 2

    def manageShips(self):
        """
        This function does all the work. If a button is pressed, it generates the coordinates for a ship and makes
        the surrounding buttons red.
        """
        for l in self.usrBoatCoords.values():
            for c in l:
                self.colorBtn(c)

    def colorBtn(self, coord):
        """
        Colors buttons red or white.
        """
        self.userBtnsDict[coord].setObjectName('Ship')
        self.userBtnsDict[coord].setStyleSheet(self.stylesheet)

    def checkShips(self, x, y, coords, field, name):
        """
        Check if a ship has been hit
        After placement, if the user clicks, it goes to this function!
        """
        click = (x, y)
        # Loop through dictionary with ships and coords
        for ship, coord in coords.items():
            for el in coord:
                if click == el:
                    field[el].setObjectName('ShipHit')
                    field[el].setStyleSheet(self.stylesheet)
                    if name == "You":
                        ndx = coord.index(el)
                        print("de index van de coordinaat is: ", ndx)
                        print("Het hele woord", ship[1])
                        letter = ship[1][ndx]
                        print("De letter die hierbij past is:", letter)
                        self.botsBtnsDict[click] = QtGui.QPushButton(letter)
                    coord.remove(el)
                    # Check if ship is destroyed after the hit
                    self.checkDestroyed(coords, name)

                    return True

        # None of the ships got a hit!
        field[click].setObjectName('Shot')
        field[click].setStyleSheet(self.stylesheet)
        return False

    def checkDestroyed(self, coords, name):
        """
        Check if a ship is destroyed
        """

        # Return True when ship is destroyed
        for ship, coord in coords.items():
            if set(coords.get(ship)) == set(self.hit):

                # Feedback
                self.feedbackLabel.setText(str(name) + ' destroyed a ship')

                del coords[ship]
                return

        # None of the ships are destroyed
        return

    def restart(self):

        makeShips.Battleships()

        self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    game = BSGame()
    game.show()
    app.exec_()