from PyQt5.QtWidgets import *


class Widget1(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.topLayout = QHBoxLayout()
        self.mainLayout = QGridLayout()

        self.imuLayout = QGridLayout()
        self.imuLayout.addWidget(QLabel('IMU'), 0, 0)
        self.imuLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.imuLayout, 1, 0)
        self.setLayout(self.mainLayout)

class Widget2(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.topLayout = QHBoxLayout()
        self.mainLayout = QGridLayout()

        self.idsLayout = QGridLayout()
        self.idsLayout.addWidget(QLabel('Long Distance Sensor'), 0, 0)
        self.idsLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.idsLayout, 1, 0)
        self.setLayout(self.mainLayout)

class Widget3(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.topLayout = QHBoxLayout()
        self.mainLayout = QGridLayout()

        self.psLayout = QGridLayout()
        self.psLayout.addWidget(QLabel('Pressure Sensor'), 0, 0)
        self.psLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.psLayout, 1, 0)
        self.setLayout(self.mainLayout)

class Widget4(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.topLayout = QHBoxLayout()
        self.mainLayout = QGridLayout()

        self.pesLayout = QGridLayout()
        self.pesLayout.addWidget(QLabel('Photo Electric Sensor'), 0, 0)
        self.pesLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.pesLayout, 1, 0)
        self.setLayout(self.mainLayout)

class Widget5(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.topLayout = QHBoxLayout()
        self.mainLayout = QGridLayout()

        self.reLayout = QGridLayout()
        self.reLayout.addWidget(QLabel('Rotary Encoders'), 0, 0)
        self.reLayout.addWidget(QTableWidget(2, 2), 1, 0)
        self.mainLayout.addLayout(self.reLayout, 1, 0)
        self.setLayout(self.mainLayout)

class stackedExample(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        lay = QVBoxLayout(self)
        self.Stack = QStackedWidget()
        self.Stack.addWidget(Widget1())
        self.Stack.addWidget(Widget2())
        self.Stack.addWidget(Widget3())
        self.Stack.addWidget(Widget4())
        self.Stack.addWidget(Widget5())

        btnNext = QPushButton("Next")
        btnNext.clicked.connect(self.onNext)
        btnPrevious = QPushButton("Previous")
        btnPrevious.clicked.connect(self.onPrevious)
        btnLayout = QHBoxLayout()
        btnLayout.addWidget(btnPrevious)
        btnLayout.addWidget(btnNext)

        lay.addWidget(self.Stack)
        lay.addLayout(btnLayout)

    def onNext(self):
        self.Stack.setCurrentIndex((self.Stack.currentIndex()+1) % 5)

    def onPrevious(self):
        self.Stack.setCurrentIndex((self.Stack.currentIndex()-1) % 5)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = stackedExample()
    w.show()
    sys.exit(app.exec_())
