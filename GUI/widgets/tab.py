from PyQt5.QtWidgets import *

class Tab(QTabWidget):
    def __init__(self, parent=None):
        super(Tab, self).__init__(parent)
        self.imu_tab = QWidget()
        self.lds_tab = QWidget()
        self.ps_tab = QWidget()
        self.pes_tab = QWidget()
        self.re_tab = QWidget()

        self.addTab(self.imu_tab, "IMU")
        self.addTab(self.lds_tab, "LDS")  # light
        self.addTab(self.ps_tab, "PS")  # pressure
        self.addTab(self.pes_tab, "PES")  # distance
        self.addTab(self.re_tab, "RE")  # temperaure
        self.ImuTab()
        self.LdsTab()
        self.PsTab()
        self.PesTab()
        self.ReTab()

        self.setWindowTitle("Sensors Data")
        self.setStyleSheet(
            "QTabBar::tab { height : 80px; width : 200px; background: rgb(79,79,79); font-weight: bold; font-size: large; color: rgb(255,255,255); border: 2px solid black}; background-color : rgb(224,224,224); border-radius: 5px")

    # replace ?? with live data
    def ImuTab(self):
        mainLayout = QGridLayout()

        duration = QLabel()
        state = QLabel()
        acceleration = QLabel()

        duration.setText("Disarm Duration: ?? s left")
        duration.setAlignment(Qt.AlignCenter)
        duration.setFont(QFont('AnyStyle', 18))
        duration.setStyleSheet(
            "padding: 15px; color: rgb(255,183,183); background-color : rgb(79,79,79)")

        state.setText("Current State: ??")
        state.setAlignment(Qt.AlignCenter)
        state.setFont(QFont('AnyStyle', 18))
        state.setStyleSheet(
            "padding: 15px; color: rgb(255,183,183); background-color : rgb(79,79,79)")

        acceleration.setText("Estimate Acceleration: ??")
        acceleration.setAlignment(Qt.AlignCenter)
        acceleration.setFont(QFont('AnyStyle', 18))
        acceleration.setStyleSheet(
            "padding: 15px; color: rgb(255,183,183); background-color : rgb(79,79,79)")

        labelLayout = QVBoxLayout()
        labelLayout.addWidget(duration)
        labelLayout.addWidget(state)
        labelLayout.addWidget(acceleration)

        soft_stop = QPushButton()
        soft_stop.setText("SOFT STOP")
        soft_stop.setFont(QFont('AnyStyle', 18))
        soft_stop.setStyleSheet(
            "padding: 20px; background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        soft_stop.clicked.connect(self.softStop)

        shutdown = QPushButton()
        shutdown.setText("SHUTDOWN")
        shutdown.setFont(QFont('AnyStyle', 18))
        shutdown.setStyleSheet(
            "padding: 20px; background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        shutdown.clicked.connect(self.Shutdown)

        teleop = QPushButton()
        teleop.setText("TELEOP")
        teleop.setFont(QFont('AnyStyle', 18))
        teleop.setStyleSheet(
            "padding: 20px; background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        teleop.clicked.connect(self.Teleop)

        arm = QPushButton()
        arm.setText("ARM")
        arm.setFont(QFont('AnyStyle', 18))
        arm.setStyleSheet(
            "padding: 20px; background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        arm.clicked.connect(self.Arm)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(soft_stop)
        buttonLayout.addWidget(shutdown)
        buttonLayout.addWidget(teleop)
        buttonLayout.addWidget(arm)

        tare = QPushButton()
        tare.setText("Tare Acceleration Estimates")
        tare.setFont(QFont('AnyStyle', 18))
        tare.setStyleSheet(
            "background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 3px solid black")
        tare.clicked.connect(self.Tare)

        table = QTableWidget(10, 2)
        table.setHorizontalHeaderLabels(['Time', 'Acceleration'])
        table.setStyleSheet("background-color: rgb(224,224,224)")

        tableLayout = QVBoxLayout()
        tableLayout.addWidget(tare)
        tableLayout.addWidget(table)

        bottomLayout = QHBoxLayout()
        bottomLayout.addLayout(buttonLayout)
        bottomLayout.addLayout(tableLayout)

        rightLayout = QVBoxLayout()
        rightLayout.addLayout(labelLayout)
        rightLayout.addLayout(bottomLayout)

        imuLayout = QHBoxLayout()
        imuLayout.addWidget(Graph())
        imuLayout.addLayout(rightLayout)
        mainLayout.addLayout(imuLayout, 1, 0)
        self.imu_tab.setLayout(mainLayout)

    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())

    def softStop(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Do you want to stop the program?")
        self.msgBox.setWindowTitle("Soft Stop Button Pushed!")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # TODO: stop programme
        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
        else:
            print("Action cancelled")

    def Shutdown(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Do you want to shutdown the program?")
        self.msgBox.setWindowTitle("Shutdown Button Pushed!")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # TODO: terminate system?
        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
            sys.exit()
        else:
            print("Action cancelled")

    def Teleop(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Some error message for teleop?")
        self.msgBox.setWindowTitle("Teleop Button Pushed!")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # TODO: what happens?
        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
        else:
            print("Action cancelled")

    def Arm(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Some error message for ARM")
        self.msgBox.setWindowTitle("Arm Button Pushed!")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # TODO: What happens then?
        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
        else:
            print("Action cancelled")

    def Tare(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Do you want to tare acceleration estimates?")
        self.msgBox.setWindowTitle(
            "Tare Acceleration Estimates Button Pushed!")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # TODO: tare data
        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
        else:
            print("Action cancelled")

    # TODO: complete these tabs below
    def LdsTab(self):
        mainLayout = QGridLayout()

        ldsLayout = QHBoxLayout()
        ldsLayout.addWidget(Graph())
        ldsLayout.addWidget(QTableWidget(2, 2))
        mainLayout.addLayout(ldsLayout, 1, 0)
        self.lds_tab.setLayout(mainLayout)

    def PsTab(self):
        mainLayout = QGridLayout()

        psLayout = QHBoxLayout()
        psLayout.addWidget(Graph())
        psLayout.addWidget(QTableWidget(2, 2))
        mainLayout.addLayout(psLayout, 1, 0)
        self.ps_tab.setLayout(mainLayout)

    def PesTab(self):
        mainLayout = QGridLayout()

        pesLayout = QHBoxLayout()
        pesLayout.addWidget(Graph())
        pesLayout.addWidget(QTableWidget(2, 2))
        mainLayout.addLayout(pesLayout, 1, 0)
        self.pes_tab.setLayout(mainLayout)

    def ReTab(self):
        mainLayout = QGridLayout()

        reLayout = QHBoxLayout()
        reLayout.addWidget(Graph())
        reLayout.addWidget(QTableWidget(2, 2))
        mainLayout.addLayout(reLayout, 1, 0)
        self.re_tab.setLayout(mainLayout)