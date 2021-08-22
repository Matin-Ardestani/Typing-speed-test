from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from typingtest import Ui_TestWindow
from welcome import Ui_WelcomeWindow


class Welcome(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_WelcomeWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.show()

        self.ui.pushButton.clicked.connect(self.main)
    def main(self):
        self.mainwindow = RootMain()
        self.mainwindow.show()
        self.close()

    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

class RootMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_TestWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


    def mousePressEvent(self , evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self , evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Welcome()
    sys.exit(app.exec_())