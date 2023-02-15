import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from fileProc import read,write
import os

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
        self.HomeBtn()
        self.bookAddWin()
        ####
        self.mainWindow.show()
        sys.exit(app.exec_())

    def HomeBtn(self):
        self.mainWindow.addBook.clicked.connect(self.bookAdd.show)

    def bookAddWin(self):
        if not('LibraryAppBooks' in os.listdir()):
            os.mkdir('LibraryAppBooks')
        def okClicked():
            x = self.bookAdd.number.text()
            if f'{x}.blf' in os.listdir():
                #book with this number is already exist message
                pass
            else:
                if not (write(self.bookAdd.name.text(),self.bookAdd.writer.text(),self.bookAdd.number.text(),self.bookAdd.year.text(),self.bookAdd.staryes.isChecked(),self.bookAdd.additional.toPlainText(),self.bookAdd.cate.currentText(),self.bookAdd.group.currentText(),self.bookAdd.publisher.currentText())):
                    #something went wrong message
                    pass                    

                # successfully added book message
                self.bookAdd.close()
        self.bookAdd.ok.clicked.connect(okClicked)
        self.bookAdd.discard.clicked.connect(self.bookAdd.close)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    