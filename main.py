import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

class ThingAdd():
    def __init__(self):
        pass

class BookAdd():
    def __init__(self):
        pass 

class MainWindow():
    def __init__(self):
        ui_file = QFile("main.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        window = loader.load(ui_file)
        window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())