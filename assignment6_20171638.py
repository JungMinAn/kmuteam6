import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, QGridLayout,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):

        namelabel = QLabel("Name:",self)
        nameedit = QLineEdit(self)
        agelabel = QLabel("Age: ", self)
        ageedit = QLineEdit(self)
        scorelabel = QLabel("Score: ", self)
        scoreedit = QLineEdit(self)
        amountlabel = QLabel("Amount: ", self)
        amountedit = QLineEdit(self)
        keylabel = QLabel("Key: ", self)

        addbutton = QPushButton("Add")
        delbutton = QPushButton("Del")
        findbutton = QPushButton("Find")
        incbutton = QPushButton("Inc")
        showbutton = QPushButton("Show")
        
        resultlabel = QLabel("Result: ")
        resultedit = QLineEdit()

        combo = QComboBox(self)
        combo.addItem("Name")
        combo.addItem("Age")
        combo.addItem("Score")

        combo.activated[str].connect(self.onActivated)
        
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(namelabel, 1,0)
        grid.addWidget(nameedit,1,1)
        grid.addWidget(agelabel,1,2)
        grid.addWidget(ageedit,1,3)
        grid.addWidget(scorelabel,1,4)
        grid.addWidget(scoreedit,1,5)
        grid.addWidget(amountlabel,2,3)
        grid.addWidget(amountedit, 2, 4)
        grid.addWidget(keylabel, 2, 5)
        grid.addWidget(combo, 2, 6)
        grid.addWidget(addbutton, 3, 1)
        grid.addWidget(delbutton, 3, 2)
        grid.addWidget(findbutton, 3, 3)
        grid.addWidget(incbutton, 3, 4)
        grid.addWidget(showbutton, 3, 5)
        grid.addWidget(resultlabel, 4,1)
        grid.addWidget(resultedit, 3, 1, 10, 1)

        self.setLayout(grid)
        self.setGeometry(300,300,500,250)
        self.setWindowTitle('Assignment6')
        self.show()

    def onActivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def closeEvent(self, Event):

        self.writeScoreDB()


    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB:", self.dbfilename)
            return[]
        self.scdb=[]

        try:
            self.scdb =  pickle.load(fH)
        except:
            print("Empty DB:", self.dbfilename)
        else:
            print("Open DB:", self.dbfilename)
        fH.close()
        return self.scdb
    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        for i in range(len(self.scdb)):
            self.resultedit.append("%s %29s %29s %29s %29s %29s" %('Name', str(self.scdb[i]['Name']),'Age',str(self.scdb[i]['Age']),'Score', str(self,scdb[i]['Score'])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
