import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
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
        
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        result = QLabel('Result:')

        nameEdit = QLineEdit()
        ageEdit = QLineEdit()
        scoreEdit = QLineEdit()
        amountEdit = QLineEdit()
        resultEdit = QTextEdit()

        addButton = QPushButton('Add')
        addButton.clicked.connect(self.AddbuttonClicked)
        delButton = QPushButton('Del')
        delButton.clicked.connect(self.DelbuttonClicked)
        findButton = QPushButton('Find')
        findButton.clicked.connect(self.FindbuttonClicked)
        incButton = QPushButton('Inc')
        incButton.clicked.connect(self.IncbuttonClicked)
        showButton = QPushButton('Show')
        showButton.clicked.connect(self.ShowbuttonClicked)


        keyBox = QComboBox()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(name, 1, 0)
        grid.addWidget(nameEdit, 1, 1)

        grid.addWidget(age, 1, 2)
        grid.addWidget(ageEdit, 1, 3)

        grid.addWidget(score, 1, 4)
        grid.addWidget(scoreEdit, 1, 5)

        grid.addWidget(amount, 2, 2.5)
        grid.addWidget(amountEdit, 2, 3.5)

        list1 = [
            self.tr('Name'),
            self.tr('Age'),
            self.tr('Score')
        ]

        grid.addWidget(key, 2, 4.5)
        grid.addWidget(keyBox, 2, 5.5)
        keyBox.addItems(list1)

        grid.addWidget(addButton, 3, 1.5)
        grid.addWidget(delButton, 3, 2.5)
        grid.addWidget(findButton, 3, 3.5)
        grid.addWidget(incButton, 3, 4.5)
        grid.addWidget(showButton, 3, 5.5)

        grid.addWidget(result, 4, 0)
        grid.addWidget(resultEdit, 5, 0, -1, 0)



        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def AddbuttonClicked(self):
        name = self.nameEdit.text()
        age = self.ageEdit.text()
        score = self.scoreEdit.text()
        dic1 = {'name': name, 'age': age, 'score': score}
        self.scoredb += [dic1]
        self.showScoreDB


    def DelbuttonClicked(self):
        delname = self.nameEdit.text()
        for i in self.scoredb:
            if i['name'] == delname:
                self.scoredb.remove(i)
        self.showScoreDB

    def FindbuttonClicked(self):
        findname = self.nameEdit.text()
        fshowtext = ""
        for i in self.scoredb:
            if i['name'] == findname:
                for j in i:
                    fshowtext += (j + "=" + i[j] + "=")
                fshowtext += "/n"
        self.output.setText(fshowtext)

    def IncbuttonClicked(self):
        incname = self.nameln.text()
        incobj = int(self.amountln.text())
        for i in self.scoredb:
            if i['Name'] == incname:
                i['Score'] += incobj
        self.showScoreDB()

    def ShowbuttonClicked(self):
        self.showScoreDB()


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        sortkey = str(self.keyBox.currentText())
        sshowtext = ""
        sortkey = "Name" if not sortkey else sortkey
        for i in sorted(self.scoredb, key=lambda person: person[sortkey]):
            for j in sorted(i):
                sshowtext += str(j) + " = " + str(i[j]) + "    "
            sshowtext += "\n"
        self.output.setText(sshowtext)



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
