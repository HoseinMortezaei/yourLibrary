import sys
from PySide2.QtWidgets import QApplication, QMainWindow,QMessageBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
import fileProc
import os

# for i in os.listdir('LibraryAppBooks'):
#     books += []

class MainWindow():
    def __init__(self):
        ui_file = QFile("main.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.mainWindow = loader.load(ui_file)
        ####
        ui_file = QFile("bookAdd.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.bookAdd = loader.load(ui_file)
        ####
        self.pgs()
        self.HomeBtn()
        self.bookAddWin()
        ####
        self.mainWindow.show()
        sys.exit(app.exec_())

    def HomeBtn(self):
        self.mainWindow.addBook.clicked.connect(self.bookAdd.show)

    def pgc(self):
        self.pubs = {}
        if not('Pubs' in os.listdir()):
            os.mkdir('Pubs')
        else:
            for i in os.listdir('Pubs'):
                self.pubs[i] = fileProc.readP(i)
        self.cats= {}
        if not('Cats' in os.listdir()):
            os.mkdir('Cats')
        else:
            for i in os.listdir('Cats'):
                self.cats[i] = fileProc.readC(i)           
        self.groups = {}
        if not('Groups' in os.listdir()):
            os.mkdir('Groups')
        else:
            for i in os.listdir('Groups'):
                self.groups[i] = fileProc.readG(i)



    def bookAddWin(self):
        if not('LibraryAppBooks' in os.listdir()):
            os.mkdir('LibraryAppBooks')
        def okClicked():
            x = self.bookAdd.number.text()
            if f'{x}.blf' in os.listdir("LibraryAppBooks"):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText('Book with this "number" is already exist')
                msg.setWindowTitle('ERROR adding book')
                msg.setWindowIcon(QIcon('icon.png'))
                msg.setStandardButtons(QMessageBox.Ok)
                msg.show()
                msg.exec_()
            else:
                thing = [self.bookAdd.name.text(),self.bookAdd.writer.text(),self.bookAdd.number.text(),self.bookAdd.year.text()]
                if '' in thing :
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText('fill all fields with star(*)')
                    msg.setWindowTitle('Incomplete informations')
                    msg.setWindowIcon(QIcon('icon.png'))
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.show()
                    msg.exec_()    
                else:                        
                    book =  fileProc.write(self.bookAdd.name.text(),self.bookAdd.writer.text(),
                    self.bookAdd.number.text(),self.bookAdd.year.text(),
                    self.bookAdd.staryes.isChecked(),
                    self.bookAdd.additional.toPlainText(),self.bookAdd.cate.currentText(),
                    self.bookAdd.group.currentText(),self.bookAdd.publisher.currentText())   

                    self.pubs[self.bookAdd.publisher.currentText()] = [self.bookAdd.number.text()]+self.pubs.get(self.bookAdd.publisher.currentText(),[])
                    fileProc.writeP(self.bookAdd.publisher.currentText(),self.bookAdd.number.text())
                    self.cats[self.bookAdd.cate.currentText()] = [self.bookAdd.number.text()]+self.cats.get(self.bookAdd.cate.currentText(),[])
                    fileProc.writeC(self.bookAdd.cate.currentText(),self.bookAdd.number.text())
                    self.groups[self.bookAdd.group.currentText()] = [self.bookAdd.number.text()]+self.groups.get(self.bookAdd.group.currentText(),[])
                    fileProc.writeG(self.bookAdd.group.currentText(),self.bookAdd.number.text())
                    
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText('seccessfully added book')
                    msg.setWindowTitle('successful')
                    msg.setWindowIcon(QIcon('icon.png'))
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.show()
                    msg.exec_()
                    
                    self.bookAdd.name.setText('')
                    self.bookAdd.writer.setText('')
                    self.bookAdd.year.setText('')
                    self.bookAdd.number.setText('')
                    self.bookAdd.close()
                    self.bookAdd.starno.setChecked(True)
                    self.bookAdd.additional.setPlainText('')
                    self.bookAdd.cate.setCurrentIndex(0)
                    self.bookAdd.group.setCurrentIndex(0)
                    self.bookAdd.publisher.setCurrentIndex(0)
                    self.bookAdd.close()
        
        self.bookAdd.ok.clicked.connect(okClicked)
        self.bookAdd.discard.clicked.connect(self.bookAdd.close)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
