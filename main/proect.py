from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
app = QApplication([])
ex = Widget()
def nachalo():
    ex.hide()
ex.ui.STARt.clicked.connect(nachalo)
ex.show()
app.exec_()