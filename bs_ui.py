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
                self.btnsDict[coord].clicked.connect(lambda c, x=row, y=column: self.yeah(x, y))
                self.grid.addWidget(self.btnsDict[coord], row, column)

        self.show()

    def yeah(self, x ,y):
        print(x, y)


def main():
    app = QtGui.QApplication(sys.argv)
    game = Battleships()
    app.exec_()


if __name__ == '__main__':
    main()
