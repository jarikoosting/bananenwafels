#!/opt/local/bin/python3.4

from PyQt4 import QtGui, QtCore
import os, sys
import makeShips

"""
Start screen for the game Battleship
"""

class StartGame(QtGui.QWidget):
    def __init__(self):
        """
        Constructs a start object
        """
        super(StartGame, self).__init__()
        self.initUI()

    def initUI(self):
        """
        Create a start screen
        """
        # Create a window
        self.setWindowTitle("Battle Ships")
        self.setGeometry(0, 0, 300, 300)

        # Make a grid
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)

        # Create the logo
        self.logo = QtGui.QLabel(self)
        self.logo.setPixmap(QtGui.QPixmap(os.getcwd() + "/logo.png"))
        self.logo.setStyleSheet('QLabel {qproperty-alignment: AlignCenter;}')

        # Create a start button
        self.startButton = QtGui.QPushButton("Start my game!", self)
        self.startButton.setStyleSheet('QPushButton {background-color: orange; margin: 0; height: 60px; width: 150px;'
                                       'border-radius: 5px; border-bottom: 4px solid #CD6839; font-size: 20px;}'
                                       'QPushButton:hover {background-color: #E87025; border-bottom: 4px solid #CD6839;}')

        self.names = QtGui.QLabel("© 2015 De Bananenwafels. Don't distribute this game. ")
        self.names.setStyleSheet('QLabel {qproperty-alignment: AlignCenter;}')

        # Add widgets to grid
        self.grid.addWidget(self.logo, 0, 0)
        self.grid.addWidget(self.startButton, 1, 0)
        self.grid.addWidget(self.names, 2, 0)

        # Center the screen
        self.move(QtGui.QApplication.desktop().screen().rect().center()- self.rect().center())

        # Show the start window
        self.show()

        # Connect the start button
        self.startButton.clicked.connect(self.start)

    def start(self):

        # Close the window
        self.close()

        # Go to the game
        makeShips.Battleships()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    start = StartGame()
    start.show()
    app.exec_()