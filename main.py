import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

class ThingAdd():
    def __init__(self):
        pass

class BookAdd():
    def __init__(self):
        ui_file = QFile("bookAdd.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        window = loader.load(ui_file)
        window.show()
        sys.exit(app.exec_())

class MainWindow():
    def __init__(self):
        ui_file = QFile("main.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.mainWindow = loader.load(ui_file)
        ####
        self.HomeBtn()
        ####
        self.mainWindow.show()
        sys.exit(app.exec_())

    def HomeBtn(self):
        self.mainWindow.addBook.clicked.connect(lambda:BookAdd())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    