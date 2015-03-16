#!/opt/local/bin/python3

from PyQt4 import QtGui, QtCore
import sys
"""
This function places the ships on the board of the user
"""
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

        self.botendic= {"Aircraft Carrier":5,"Battleship":4,"Submarine":3,"Destroyer":3,"Patrol Boat":2}

        self.richting=QtGui.QPushButton('Horizontaal',self)
        self.richting.move(10,10)
        self.richting.setCheckable(True)
        self.richting.clicked.connect(self.direction)

        self.setship=QtGui.QPushButton('Plaats schip!',self)
        self.setship.move(100,10)
        self.setship.clicked.connect(self.setShips)

        self.btnsDict = {}
        for row in range(10):
            for column in range(10):
                coord = str(row)+"."+str(column)
                self.btnsDict[coord] = QtGui.QPushButton(str(row) + ":" + str(column))
                self.btnsDict[coord].clicked.connect(lambda c, x=row, y=column: self.makeShips(x, y))
                self.grid.addWidget(self.btnsDict[coord], row, column)

        self.show()

    def makeShips(self,x,y):
        """
        this function creates the ships and gives a list of coordinates back of where the 5 ships are
        """
        #initialisatie van de waarden
        rij=x
        kolom=y
        richting=self.richting
        self.startship=(x,y)
        self.lijst=[]

        #maak lijst van de lengte van de boten om te sorten en erdoorheen te loopen
        x=list(self.botendic.values())
        x.sort()

        for lengteschip in x:
            lengteschip=int(lengteschip)
            print("lengte schip is", lengteschip, "blokjes")

            if richting == "horizontaal":
                rij=rij+(lengteschip)

            else:
                kolom=kolom+(lengteschip)

            self.endship=(rij,kolom)

            self.lijst.append(self.startship)
            self.lijst.append(self.endship)
        print(self.lijst)

    def direction(self,pressed):
        """
        This function gets the direction of  the ship from the user and changes the label of the button
        """
        source=self.sender()
        if pressed:
            source.setText("horizontaal")
            self.richting="horizontaal"
        else:
            source.setText("verticaal")
            self.richting="verticaal"

    def setShips(self):
        # Dan dus de coordinaten in een dictionairy: schip en dan getal erachter.
        lijst=[]
        lijst.append(self.lijst)
        print(self.lijst)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    game = Battleships()
    game.show()
    app.exec_()





