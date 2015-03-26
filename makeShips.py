#!/opt/local/bin/python3.4
# voor linux
#!/usr/bin/env python

from PyQt4 import QtGui, QtCore
import os, sys
from random import randrange
import playGame


class Battleships(QtGui.QWidget):
    def __init__(self):
        """
        Constructs a Battleship game object, with which the user can play a game.
        """
        super(Battleships, self).__init__()
        self.makeAIShips()
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

        # Create a dictonairy with ships, an empty dictonairy for ships with coords and a list for the lengts of the
        # boats.
        self.shipDic = {5: ("Aircraft Carrier"), 4: ("Battleship"), 3: ("Submarine"), 3.4: ("Destroyer"), 2: ("Patrol Boat")}
        self.boatCoords = {}
        self.boatLengths = list(self.shipDic.keys())
        self.boatLengths.sort()

        # Create button for placing ships
        self.placeBtn = QtGui.QPushButton('Place Ship!', self)
        self.placeBtn.setObjectName('MenuButton')
        self.placeBtn.setStyleSheet(self.stylesheet)
        self.placeBtn.clicked.connect(self.submitShip)
        self.placeBtn.setEnabled(False)

        # Create button for placing ships vertically or horizontally
        self.directionBtn = QtGui.QPushButton('Horizontal', self)
        self.directionBtn.setStyleSheet(self.stylesheet)
        self.directionBtn.setObjectName('MenuButton')
        self.directionBtn.clicked.connect(self.direction)

        # Create button for starting game
        self.startGame = QtGui.QPushButton('Start Game!', self)
        self.startGame.setStyleSheet(self.stylesheet)
        self.startGame.setObjectName('MenuButton')
        self.startGame.setEnabled(False)
        self.startGame.clicked.connect(self.start)
        #self.placeAllBtn.clicked.connect(self.setAllShips)

        # Create label with game updates
        self.feedback = QtGui.QLabel('', self)

        # Create a dictionary for buttons, and create 100 buttons for the board
        self.btnsDict = {}
        for row in range(10):
            for column in range(1, 11):
                # Make a unique variable name bij adding de coordinates together in a string
                #coord = str(row)+"."+str(column)
                coord = (row, column)
                self.btnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.btnsDict[coord].setStyleSheet(self.stylesheet)
                self.btnsDict[coord].setObjectName('Tile')
                # Connect the button to a _method_ where x and y are specified by using lambda
                self.btnsDict[coord].clicked.connect(lambda c, x=row, y=column: self.placeShip(x, y))
                self.grid.addWidget(self.btnsDict[coord], row, column)

        # Add other buttons to grid
        self.grid.addWidget(self.placeBtn, 1, 0)
        self.grid.addWidget(self.directionBtn, 2, 0)
        self.grid.addWidget(self.startGame, 0, 0)
        self.grid.addWidget(self.feedback, 3, 0)
        self.show()

    def placeShip(self, x, y):
        """
        This function does all the work. If a button is pressed, it generates the coordinates for a ship and makes
        the surrounding buttons red.
        """
        self.row = y
        self.column = x
        self.clearBtns()
        for l in self.boatCoords.values():
            for c in l:
                self.colorBtn(c)
        self.shipCoords = self.generateShip(self.boatLengths[0])

        # Check if the coords are within the board
        if self.checkBoundaries(self.shipCoords):
            self.feedback.setText("Ship can't be placed here.")
            self.shipCoords = []
            return
        self.placeBtn.setEnabled(True)
        self.feedback.setText('')
        for i in self.shipCoords:
            self.colorBtn(i)

    def generateShip(self, boatLength):
        """
        This function generates the coordinates for every boat, depending of the length.
        """
        coordsList = []
        if self.directionBtn.text() == "Horizontal":
            for i in range(int(boatLength)):
                coordsList.append((int(self.column), int(self.row) + int(i)))
        elif self.directionBtn.text() == "Vertical":
            for i in range(int(boatLength)):
                coordsList.append((int(self.column) + int(i), int(self.row)))
        self.checkBoundaries(coordsList)
        return coordsList

    def submitShip(self):
        """
        Places the ship and its coordinates in a dictionary.
        """
        if self.shipCoords != []:
            self.boatCoords[self.shipDic[self.boatLengths[0]]] = self.shipCoords
            self.feedback.setText('Your ship is placed.')
            self.shipCoords = []
            if len(self.boatLengths) >= 2:
                self.boatLengths.pop(0)
            elif len(self.boatLengths) == 1:
                self.boatLengths.pop(0)
                self.placeBtn.setEnabled(False)
                self.startGame.setEnabled(True)
                for b in self.btnsDict:
                    self.btnsDict[b].setEnabled(False)
                self.feedback.setText('You can start the game!')
        else:
            # Place ship again
            self.feedback.setText('Please place your ship.')

    def colorBtn(self, coord):
        """
        Colors buttons red or white.
        """
        self.btnsDict[coord].setObjectName('Ship')
        self.btnsDict[coord].setStyleSheet(self.stylesheet)

    def removeCoords(self):
        for b in self.shipCoords:
            self.btnsDict[b].setObjectName('Tile')
            self.btnsDict[b].setStyleSheet(self.stylesheet)

    def clearBtns(self):
        """
        Clears buttons, everything will be white again.
        """
        for b in self.btnsDict:
            self.btnsDict[b].setObjectName('Tile')
            self.btnsDict[b].setStyleSheet(self.stylesheet)

    def direction(self):
        """
        This function gets the direction of  the ship from the user and changes the label of the button
        """
        if self.directionBtn.text() == "Horizontal":
            self.directionBtn.setText("Vertical")
        else:
            self.directionBtn.setText("Horizontal")
        self.removeCoords()

    def makeAIShips(self):
        """
        This function creates the ships and words for the Computer and validates them
        """
        words2 = []
        words3 = []
        words4 = []
        words5 = []
        listwords = []

        with open('words.txt') as in_f:
            for line in in_f:
                woord = line.replace('\n', ' ').strip()
                if len(woord) == 2:
                    words2.append(woord)
                elif len(woord) == 3:
                    words3.append(woord)
                elif len(woord) == 4:
                    words4.append(woord)
                elif len(woord) == 5:
                    words5.append(woord)

        word5 = words5[randrange(len(words5))]
        word4 = words4[randrange(len(words4))]
        word3 = words3[randrange(len(words3))]
        word3_5 = words3[randrange(len(words3))]
        word2 = words2[randrange(len(words2))]
        listwords.append(word5)
        listwords.append(word4)
        listwords.append(word3)
        listwords.append(word3_5)
        listwords.append(word2)
        print(listwords)
        self.boatAICoords={}
        boatLength = [5, 4, 3, 3, 2]

        while boatLength != []:
            coordsList = []
            # set direction ship
            direction = randrange(2)
            if direction == 0:
                directionShip = "Horizontal"
            elif direction == 1:
                directionShip = "Vertical"

            startX = randrange(10)
            startY = randrange(12,22)

            if directionShip == "Horizontal":
                for i in range(boatLength[0]):
                    coordsList.append((int(startX), int(startY) + int(i)))

            elif directionShip == "Vertical":
                for j in range(boatLength[0]):
                    coordsList.append((int(startX) + int(j), int(startY)))

            if self.checkAIboundaries(coordsList, self.boatAICoords.values()):
                self.boatAICoords[(boatLength[0], listwords[0])] = coordsList
                listwords.pop(0)
                boatLength.pop(0)
                print(self.boatAICoords)
        return self.boatAICoords

    def checkAIboundaries(self, l, dv):
        for i in l:
            if (i[0] > 9) or (i[1] > 21):
                return False
            for coords in dv:
                for x, y in coords:
                    if (x,y) in l:
                        return False
        return True

    def checkBoundaries(self, coordList):
        """
        Check of a ship is placed within the board
        """
        for i, j in coordList:
            if (i > 9 or i < 0) or (j > 10 or j < 0):
                return True
            for ship, coords in self.boatCoords.items():
                if (i, j) in coords:
                    return True



    def start(self):

        # Close the window
        self.close()

        # Go to the game
        playGame.BSGame(self.boatCoords, self.makeAIShips())

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    game = Battleships()
    game.show()
    app.exec_()