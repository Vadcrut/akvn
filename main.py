import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class okno(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUi()

    def loadUi(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('title')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = okno()
    ex.show()
    sys.exit(app.exec())