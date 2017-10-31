import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
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

        namelb = QLabel("Name: ")
        self.nameln = QLineEdit()
        agelb = QLabel("Age: ")
        self.ageln = QLineEdit()
        scorelb = QLabel("Score: ")
        self.scoreln = QLineEdit()
        amountlb = QLabel("Amount: ")
        self.amountln = QLineEdit()
        keylb = QLabel("Key: ")
        self.keycombo = QComboBox()
        self.keycombo.addItem("Name")
        self.keycombo.addItem("Age")
        self.keycombo.addItem("Score")
        addbt = QPushButton("Add", self)
        addbt.clicked.connect(self.add_clicked)
        delbt = QPushButton("Del", self)
        delbt.clicked.connect(self.del_clicked)
        findbt = QPushButton("Find", self)
        findbt.clicked.connect(self.find_clicked)
        incbt = QPushButton("Inc", self)
        incbt.clicked.connect(self.inc_clicked)
        showbt = QPushButton("Show", self)
        showbt.clicked.connect(self.show_clicked)
        resultlb = QLabel("Result: ")
        self.output = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        hbox4 = QHBoxLayout()
        hbox5 = QHBoxLayout()
        hbox1.addWidget(namelb)
        hbox1.addWidget(self.nameln)
        hbox1.addWidget(agelb)
        hbox1.addWidget(self.ageln)
        hbox1.addWidget(scorelb)
        hbox1.addWidget(self.scoreln)
        hbox2.addStretch()
        hbox2.addWidget(amountlb)
        hbox2.addWidget(self.amountln)
        hbox2.addWidget(keylb)
        hbox2.addWidget(self.keycombo)
        hbox3.addStretch()
        hbox3.addWidget(addbt)
        hbox3.addWidget(delbt)
        hbox3.addWidget(findbt)
        hbox3.addWidget(incbt)
        hbox3.addWidget(showbt)
        hbox4.addWidget(resultlb)
        hbox5.addWidget(self.output)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.setLayout(vbox)
        self.show()

    def add_clicked(self):
        name = self.nameln.text()
        age = int(self.ageln.text())
        score = int(self.scoreln.text())
        dic1 = {'Name': name, 'Age': age, 'Score': score}
        self.scoredb += [dic1]
        self.showScoreDB()

    def del_clicked(self):
        delname = self.nameln.text()
        for i in self.scoredb:
            if i['Name'] == delname:
                self.scoredb.remove(i)
        self.showScoreDB()

    def find_clicked(self):
        findname = self.nameln.text()
        fshowtext = ""
        for i in self.scoredb:
            if i['Name'] == findname:
                for j in i:
                    fshowtext += j + " = " + str(i[j]) + "    "
                fshowtext += "\n"
        self.output.setText(fshowtext)

    def inc_clicked(self):
        incname = self.nameln.text()
        incobj = int(self.amountln.text())
        for i in self.scoredb:
            if i['Name'] == incname:
                i['Score'] += incobj
        self.showScoreDB()

    def show_clicked(self):
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
        sortkey = str(self.keycombo.currentText())
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





