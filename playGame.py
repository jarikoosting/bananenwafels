#!/opt/local/bin/python3.4

from PyQt4 import QtGui, QtCore
import os, sys


class BSGame(QtGui.QWidget):
    def __init__(self):
        """
        Constructs a Battleship game object, with which the user can play a game.
        """
        super(BSGame, self).__init__()
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

        # Create a dictionary for buttons, and create 100 buttons for the board
        self.userBtnsDict = {}
        for row in range(10):
            for column in range(1, 11):
                # Make a unique variable name bij adding de coordinates together in a string
                coord = (row, column)
                self.userBtnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.userBtnsDict[coord].setStyleSheet(self.stylesheet)
                self.userBtnsDict[coord].setObjectName('Tile')
                # Connect the button to a _method_ where x and y are specified by using lambda
                self.userBtnsDict[coord].clicked.connect(lambda c, x=row, y=column: self.placeShip(x, y))
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
                self.botsBtnsDict[coord].clicked.connect(lambda c, x=row, y=column: self.placeShip(x, y))
                self.grid.addWidget(self.botsBtnsDict[coord], row, column)


        # Add other buttons to grid
        self.grid.addWidget(self.userLabel, 0, 0)
        self.grid.addWidget(self.botLabel, 0, 11)
        self.show()

    def checkShips(self):
        """
        Check if a ship has been hit
        After placement, if the user clicks, it goes to this function!
        """
        coords = {"Aircraft Carrier":[(9,2),(9,3),(9,4),(9,5)], "Battleship":[(1,1)]}
        click = (self.row, self.column)

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
    game = BSGame()
    game.show()
    app.exec_()