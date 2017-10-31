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

        self.setGeometry(300, 300, 500, 250)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.lblname1 = QLabel("Name",self)
        self.editname1 = QLineEdit(self)

        self.lblname2 = QLabel("Age", self)
        self.editname2 = QLineEdit(self)

        self.lblname3 = QLabel("Score", self)
        self.editname3 = QLineEdit(self)

        self.hbox.addWidget(self.lblname1)
        self.hbox.addWidget(self.editname1)


        self.hbox.addWidget(self.lblname2)
        self.hbox.addWidget(self.editname2)


        self.hbox.addWidget(self.lblname3)
        self.hbox.addWidget(self.editname3)
        self.vbox.addLayout(self.hbox)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addStretch(1)

        self.lblname4 = QLabel("Amount", self)
        self.editname4 = QLineEdit(self)

        self.combo = QComboBox(self)
        self.combo.addItem("--SECTION--")
        self.combo.addItem("Name")
        self.combo.addItem("Score")
        self.combo.addItem("Age")




        self.lblname5 = QLabel("Key", self)

        self.hbox2.addWidget(self.lblname4)
        self.hbox2.addWidget(self.editname4)

        self.hbox2.addWidget(self.lblname5)


        self.hbox2.addWidget(self.combo)
        self.vbox.addLayout(self.hbox2)

        self.hbox3 = QHBoxLayout()
        self.hbox.addStretch(1)

        self.button1 = QPushButton("Add",self)
        self.button2 = QPushButton("Dle", self)
        self.button3 = QPushButton("Find", self)
        self.button4 = QPushButton("Inc", self)
        self.button5 = QPushButton("Show", self)

        self.button1.clicked.connect(self.readScoreDB)
        self.button2.clicked.connect(self.readScoreDB)
        self.button3.clicked.connect(self.readScoreDB)
        self.button4.clicked.connect(self.readScoreDB)
        self.button5.clicked.connect(self.readScoreDB)

        self.combo.activated[str].connect(self.newshow)

        self.hbox3.addWidget(self.button1)
        self.hbox3.addWidget(self.button2)
        self.hbox3.addWidget(self.button3)
        self.hbox3.addWidget(self.button4)
        self.hbox3.addWidget(self.button5)
        self.vbox.addLayout(self.hbox3)

        self.hbox4 = QHBoxLayout()
        self.lblname6 = QLabel("Result")
        self.hbox4.addWidget(self.lblname6)
        self.vbox.addLayout(self.hbox4)


        self.hbox5 = QHBoxLayout()
        self.edit = QTextEdit("",self)
        self.hbox5.addWidget(self.edit)
        self.vbox.addLayout(self.hbox5)





        self.vbox.addStretch(1)
        self.setLayout(self.vbox)
        self.vbox.addStretch(1)


        self.setWindowTitle('Assignment6')
        self.show()





    def closeEvent(self, event):
        count = 0
        while True:
            if (len(self.scoredb)==0):
                break
            else:
                for i in self.scoredb:
                    self.scoredb.remove(i)

        recore = []
        recore += [{'Name': 'Choi', 'Age': 21, 'Score': 161},{'Name': 'Yoo', 'Age': 33, 'Score': 72},{'Name': 'James', 'Age': 28, 'Score': 81},{'Name': 'You', 'Age': 10, 'Score': 78},{'Name': 'Choi', 'Age': 12, 'Score': 119},{'Name': 'Park', 'Age': 24, 'Score': 143}]

        self.scoredb += recore

        self.writeScoreDB()


    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb = pickle.load(fH)
            send = self.sender()
            option = send.text()

            a = []
            b = []
            c = []
            t = ""
            record = []
            if option == "Add":
                name = self.editname1.text()
                age = self.editname2.text()
                score = self.editname3.text()

                record = {'Name': name, 'Age': int(age), 'Score': int(score)}
                self.scoredb += [record]
                self.writeScoreDB()

            elif option == "Dle":
                name = self.editname1.text()
                count = 0
                print(name)
                while True:
                    if (count == len(self.scoredb)):
                        break
                    else:
                        for a in self.scoredb:
                            if (name == a['Name']):
                                self.scoredb.remove(a)
                            else:
                                count = len(self.scoredb)
                self.writeScoreDB()

            elif option == "Find":
                name = self.editname1.text()
                count = 0
                a =[]
                b = []
                c = []
                t1 = ""
                for t in self.scoredb:
                    if count == len(self.scoredb)-1:
                        self.edit.setText("No exist Data")
                    else:
                        if t['Name'] == name:
                            a += [t["Name"]]
                            b += [t["Age"]]
                            c += [t["Score"]]
                        else:
                            count = count +1
                for i in range(len(a)):
                    t1 += "Age=" + str(b[i]) + " " + "Name=" + str(a[i]) + " " + "Score=" + str(c[i]) + "\n"
                self.edit.setText(t1)




            elif option == "Inc":
                name = self.editname1.text()
                score = self.editname4.text()
                count = 0
                for t in self.scoredb:
                    if count == len(self.scoredb)-1:
                        self.edit.setText("No exist Data")
                    else:
                        if t['Name'] == name:

                            t['Score'] = int(t['Score']) + int(score)

                        else:
                            count = count +1
                self.writeScoreDB()
                pass

            elif option == "Show":
                for i in self.scoredb:
                    a += [i["Name"]]
                    b += [i["Age"]]
                    c += [i["Score"]]

                for i in range(len(a)):
                    t += "Age="+str(b[i])+" "+"Name="+str(a[i])+" "+"Score="+str(c[i])+"\n"
                self.edit.setText(t)











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

        pass


    def newshow(self,text):
        b=""
        a = ""
        for p in sorted(self.scoredb, key=lambda person: person[text]):
            for attr in sorted(p):
                a += attr + "=" + str(p[attr])+" "
            b += str(a) + "\n"
            a = ""
        self.edit.setText(b)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())