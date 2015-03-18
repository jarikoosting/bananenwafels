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
        print(x, y)
        if b == "0.0" or b == "6.6":
            self.btnsDict[b].setStyleSheet('QPushButton {background-color: red; color: black; width: 60px;'
                                           'height: 60px;}')
            self.infoLabel.setText("hit a ship")
        else:
            self.btnsDict[b].setStyleSheet('QPushButton {background-color: blue; color: black; width: 60px;'
                                           'height: 60px;}')


def main():
    app = QtGui.QApplication(sys.argv)
    game = Battleships()
    app.exec_()


if __name__ == '__main__':
    main()
