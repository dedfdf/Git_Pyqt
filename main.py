import random
import sys
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.setWindowTitle('Рисование круга')
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        s = random.randint(150, 200)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(100, 60, s, s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mainwindow()
    ex.show()
    sys.exit(app.exec())