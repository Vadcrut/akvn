import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


class okno(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUi()
        self.t = False
        self.btn = QPushButton('Круг', self)
        self.btn.clicked.connect(self.drawfield)

    def loadUi(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('title')

    def drawfield(self):
        self.t =True
        self.update()

    def paintEvent(self, event):
        if self.t:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            qp = QPainter()
            qp.begin(self)
            ra = randint(0, 100)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(150, 150, ra, ra)
            qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = okno()
    ex.show()
    sys.exit(app.exec())