#!/opt/local/bin/python3.4

from PyQt4 import QtGui, QtCore
import os, sys
import time


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

    def playing(self):
        while self.botBoatCoords != {} or self.usrBoatCoords != {}:
            # Your turn label

            # Computers turn label

    def fire(self, x, y):
        self.checkShips(x, y, self.botBoatCoords)
        autox, autoy = self.randomShoot()
        time.sleep(1)
        self.checkShips(autox, autoy, self.usrBoatCoords)

    def randomShoot(self):
        """
        Function that generates random coordinations.
        Needs randrange() from random module.
        """
        return randrange(10), randrange(10)

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

    def checkShips(self, x, y, coords):
        """
        Check if a ship has been hit
        After placement, if the user clicks, it goes to this function!
        """
        click = (x, y)

        # Loop through dictionary with ships and coords
        for ship, coord in coords.items():
            for el in coord:
                if click == el:
                    # KLEUR HEM ROOD el moet rood worden
                    # HIT A SHIP LABEL
                    coord.remove(el)

                    # Check if ship is destroyed after the hit
                    self.checkDestroyed()
                    return True

        # None of the ships got a hit!
        # KLEUR HEM DONKERBLAUW
        # MISSED A SHIP LABEL
        return False

    def checkDestroyed(self):
        """
        Check if a ship is destroyed
        """

        # Return True when ship is destroyed
        for ship, coord in coords.items():
            if coords.get(ship) == []:
                # LABEL SHIP IS DESTROYED
                return ship, True

        # None of the ships are destroyed
        return False

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    game = BSGame()
    game.show()
    app.exec_()