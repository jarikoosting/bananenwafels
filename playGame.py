#!/opt/local/bin/python3.4

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

        # Read QSS file for styles
        self.stylesheet = open(os.getcwd() + '/styles.qss').read()

        # Create button for placing ships
        self.userLabel = QtGui.QLabel('Users Field')
        self.userLabel.setObjectName('UserLabel')
        self.userLabel.setStyleSheet(self.stylesheet)

        self.botLabel = QtGui.QLabel('Bots Field')
        self.botLabel.setObjectName('UserLabel')
        self.botLabel.setStyleSheet(self.stylesheet)

        # Feedback with AI actions
        self.botFeedback = QtGui.QLabel('')
        self.botFeedback.setObjectName('FeedbackLabel')
        self.botFeedback.setStyleSheet(self.stylesheet)

        # Feedback with User actions
        self.userFeedback = QtGui.QLabel('')
        self.userFeedback.setObjectName('FeedbackLabel')
        self.userFeedback.setStyleSheet(self.stylesheet)

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
        self.grid.addWidget(self.userFeedback, 4, 0)
        self.grid.addWidget(self.botFeedback, 4, 11)
        self.manageShips()
        self.show()

    def fire(self, x, y):
        self.checkShips(x, y, self.botBoatCoords, self.botsBtnsDict)
        autox, autoy = self.randomShoot()
        time.sleep(1)
        self.checkShips(autox, autoy, self.usrBoatCoords, self.userBtnsDict)

        if self.botBoatCoords == {} or self.usrBoatCoords == {}:
            self.btnRestart = QtGui.QLabel('Restart Game')
            self.btnRestart.setObjectName('MenuButton')
            self.btnRestart.setStyleSheet(self.stylesheet)
            self.grid.addWidget(self.btnRestart, 12, 11)
            self.button.clicked.connect(self.restart)

    def randomShoot(self):
        """
        Function that generates random coordinations.
        Needs randrange() from random module.
        """
        return randrange(10), randrange(1,10)

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

    def checkShips(self, x, y, coords, field):
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
                    coord.remove(el)

                    # Check if ship is destroyed after the hit
                    self.checkDestroyed(coords)
                    return True

        # None of the ships got a hit!
        field[click].setObjectName('Shot')
        field[click].setStyleSheet(self.stylesheet)
        return False

    def checkDestroyed(self, coords):
        """
        Check if a ship is destroyed
        """

        # Return True when ship is destroyed
        for ship, coord in coords.items():
            if coords.get(ship) == []:
                del coords[ship]
                return

        # None of the ships are destroyed
        return

    def createWords(self):
        self.words2=[]
        self.words3=[]
        self.words4=[]
        self.words5=[]
        with open('words.txt') as in_f:
            for line in in_f:
                x = line.split('\n')
                woord=x[0]
                if len(woord) == 2:
                    self.words2.append(woord)
                elif len(woord) == 3:
                    self.words3.append(woord)
                elif len(woord)== 4:
                    self.words4.append(woord)
                elif len(woord) == 5:
                    self.words5.append(woord)
                else:
                    return

    def restart(self):

        self.close()

        makeShips.Battleships()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    game = BSGame()
    game.show()
    app.exec_()