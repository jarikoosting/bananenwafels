#!/opt/local/bin/python3.4
# Simon de Wit, maart 2015

import sys
from PyQt4 import QtCore, QtGui


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

        # Create buttons for playing game
        placeBtn = QtGui.QPushButton('Place Ship!', self)
        placeBtn.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 30px; width: 150px;}')
        #btn.clicked.connect(self.placeShip)

        self.square = QtGui.QFrame(self)
        self.square.setGeometry(20, 65, 200, 200)
        p1 = QtGui.QPushButton('Vertical', self)
        p1.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 30px; width: 75px;}')
        p2 = QtGui.QPushButton('Horizontal', self)
        p2.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 30px; width: 50px;}')

        self.btnsDict = {}

        for row in range(10):
            for column in range(1, 11):
                coord = str(row)+"."+str(column)
                self.btnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.btnsDict[coord].setStyleSheet('QPushButton {background-color: white; margin: 0; height: 30px; '
                                                   'width: 30px;}')
                self.btnsDict[coord].clicked.connect(lambda c, x=row, y=column, btn=coord: self.btnPressed(x, y, btn))
                self.grid.addWidget(self.btnsDict[coord], row, column)

        self.grid.addWidget(placeBtn, 0, 0)
        self.grid.addWidget(p1, 1, 0)
        self.grid.addWidget(p2, 2, 0)
        self.show()

    def btnPressed(self, x, y, b):
        print(x, y)
        c = (x, y)
        #listcoord = checkShips(c)
        if b == "0.1" or b == "6.7":
            self.btnsDict[b].setStyleSheet('QPushButton {background-color: red; margin: 0; color: black; width: 30px;'
                                           'height: 30px;}')
            self.infoLabel.setText("hit a ship")
        else:
            self.btnsDict[b].setStyleSheet('QPushButton {background-color: lightblue; margin: 0; color: black; width: 30px;'
                                           'height: 30px;}')


def main():
    app = QtGui.QApplication(sys.argv)
    game = Battleships()
    app.exec_()


if __name__ == '__main__':
    main()
