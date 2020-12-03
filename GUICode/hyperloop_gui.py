from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
    
class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class Tab(QTabWidget):
    def __init__(self, parent = None):
        super(Tab, self).__init__(parent)
        self.imu_tab = QWidget()
        self.lds_tab = QWidget()
        self.ps_tab = QWidget()
        self.pes_tab = QWidget()
        self.re_tab = QWidget()
        
        self.addTab(self.imu_tab,"IMU")
        self.addTab(self.lds_tab,"LDS")
        self.addTab(self.ps_tab,"PS")
        self.addTab(self.pes_tab,"PES")
        self.addTab(self.re_tab,"RE")
        self.ImuTab()
        self.LdsTab()
        self.PsTab()
        self.PesTab()
        self.ReTab()

        self.setWindowTitle("Sensors Data")
        self.setStyleSheet("QTabBar::tab { height : 80px; width : 200px; background: rgb(79,79,79); font-weight: bold; font-size: large; color: rgb(255,255,255); border: 2px solid black}; background-color : rgb(224,224,224); border-radius: 5px")
		
    # replace ?? with live data
    def ImuTab(self):
        mainLayout = QGridLayout()

        duration = QLabel()
        state = QLabel()
        acceleration = QLabel()

        duration.setText("Disarm Duration: ?? s left")
        duration.setAlignment(Qt.AlignCenter)
        duration.setStyleSheet("font-weight: bold; color: rgb(255,183,183); background-color : rgb(79,79,79)")
        duration.resize(800, 100)

        state.setText("Current State: ??")
        state.setAlignment(Qt.AlignCenter)
        state.setStyleSheet("font-weight: bold; color: rgb(255,183,183); background-color : rgb(79,79,79)")
        state.resize(800, 100)

        acceleration.setText("Estimate Acceleration: ??")
        acceleration.setAlignment(Qt.AlignCenter)
        acceleration.setStyleSheet("font-weight: bold; color: rgb(255,183,183); background-color : rgb(79,79,79)")
        acceleration.resize(800, 100)

        labelLayout = QVBoxLayout()
        labelLayout.addWidget(duration)
        labelLayout.addWidget(state)
        labelLayout.addWidget(acceleration)

        soft_stop = QPushButton()
        soft_stop.setText("SOFT STOP")
        soft_stop.setStyleSheet("background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        soft_stop.clicked.connect(self.softStop)
        # soft_stop.resize(300, 150)

        shutdown = QPushButton()
        shutdown.setText("SHUTDOWN")
        shutdown.setStyleSheet("background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        shutdown.clicked.connect(self.Shutdown)
        # shutdown.resize(300, 150)

        teleop = QPushButton()
        teleop.setText("TELEOP")
        teleop.setStyleSheet("background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        teleop.clicked.connect(self.Teleop)
        # teleop.resize(300, 150)

        arm = QPushButton()
        arm.setText("ARM")
        arm.setStyleSheet("background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        arm.clicked.connect(self.Arm)
        # arm.resize(300, 150)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(soft_stop)
        buttonLayout.addWidget(shutdown)
        buttonLayout.addWidget(teleop)
        buttonLayout.addWidget(arm)

        tare = QPushButton()
        tare.setText("Tare Acceleration Estimates")
        tare.setStyleSheet("background-color : rgb(246,246,246); border-radius: 5px; font-weight: bold; border: 2px solid black")
        tare.clicked.connect(self.Tare)

        tableLayout = QVBoxLayout()
        tableLayout.addWidget(tare)
        tableLayout.addWidget(QTableWidget(2, 2))

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
        self.msgBox.setWindowTitle("Tare Acceleration Estimates Button Pushed!")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # TODO: tare data
        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
        else:
            print("Action cancelled")
		
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

# TODO: accommodate for different graphs in different tabs (axis labels, graph types, data sources)
class Graph(QWidget):
    def __init__(self, parent = None):
        super(Graph, self).__init__(parent)
        self.layout = QGridLayout()
        self.graphWidget = pg.PlotWidget()
        # Sample data as array (neater demo)
        second = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        # Sample data from a txt file
        graph_data = open('sample_data.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(float(x))
                ys.append(float(y))
        self.graphWidget.setBackground((224,224,224))
        pen = pg.mkPen(width=10)
        self.graphWidget.plot(second, temperature, pen=pen, symbol='x', symbolSize=30)
        self.layout.addWidget(self.graphWidget)
        self.setLayout(self.layout)

class EmergencyButton(QWidget):
    def __init__(self, parent = None):
        super(EmergencyButton, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Click button")
        self.push = QPushButton(self)
        self.push.setText("Emergency\nBreak")
        self.push.setFont(QFont('AnyStyle', 15))
        self.push.setStyleSheet("background-color : red; border-radius: 5px; font-weight: bold; border: 3px solid black")
        self.push.clicked.connect(self.pushedEmergency)
        self.push.resize(400, 200)
        self.push.move(0,50)
        
    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())

    def pushedEmergency(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Do you want to terminate program?")
        self.msgBox.setWindowTitle("Emergency Button Pushed!")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.msgButtonClick)

        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
            sys.exit()
        else:
            print("Action cancelled")

class Battery1(QWidget):
    def __init__(self, parent=None):
        super(Battery1, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        battery = QLabel(self)
        volts = QLabel(self)
        amps =  QLabel(self)
        temperature =  QLabel(self)

        battery.setText("Battery #1")
        battery.setAlignment(Qt.AlignCenter)
        battery.setStyleSheet("font-weight: bold")

        volts.setText("?? Volts")
        volts.setStyleSheet("background-color : rgb(143,255,91)")
        volts.setAlignment(Qt.AlignCenter)

        amps.setText("?? Amps")
        amps.setStyleSheet("background-color : rgb(143,255,91)")
        amps.setAlignment(Qt.AlignCenter)

        temperature.setText("?? °C")
        temperature.setStyleSheet("background-color : rgb(143,255,91)")
        temperature.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(battery)
        vbox.addWidget(volts)
        vbox.addWidget(amps)
        vbox.addWidget(temperature)

        self.setLayout(vbox)

class Battery2(QWidget):
    def __init__(self, parent=None):
        super(Battery2, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        battery = QLabel(self)
        volts = QLabel(self)
        amps =  QLabel(self)
        temperature =  QLabel(self)

        battery.setText("Battery #2")
        battery.setAlignment(Qt.AlignCenter)
        battery.setStyleSheet("font-weight: bold")

        volts.setText("?? Volts")
        volts.setStyleSheet("background-color : rgb(143,255,91)")
        volts.setAlignment(Qt.AlignCenter)

        amps.setText("?? Amps")
        amps.setStyleSheet("background-color : rgb(143,255,91)")
        amps.setAlignment(Qt.AlignCenter)

        temperature.setText("?? °C")
        temperature.setStyleSheet("background-color : rgb(143,255,91)")
        temperature.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()

        vbox.addWidget(battery)
        vbox.addWidget(volts)
        vbox.addWidget(amps)
        vbox.addWidget(temperature)

        self.setLayout(vbox)


class States(QWidget):
    def __init__(self, parent=None):
        super(States, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        fsm = QLabel(self)
        mode = QLabel(self)
        wheel =  QLabel(self)
        clamp =  QLabel(self)

        fsm.setText("FSM State:")
        fsm.setStyleSheet("background-color : white; font-weight: bold")
        fsm.setAlignment(Qt.AlignCenter)

        mode.setText("Mode:")
        mode.setStyleSheet("background-color : white; font-weight: bold")
        mode.setAlignment(Qt.AlignCenter)

        wheel.setText("Wheel State:")
        wheel.setStyleSheet("background-color : white; font-weight: bold")
        wheel.setAlignment(Qt.AlignCenter)

        clamp.setText("Clamp State:")
        clamp.setStyleSheet("background-color : white; font-weight: bold")
        clamp.setAlignment(Qt.AlignCenter)

        fsm_val = QLabel(self)
        mode_val = QLabel(self)
        wheel_val =  QLabel(self)
        clamp_val =  QLabel(self)

        # TODO: Replace ?? with data
        fsm_val.setText("??")
        fsm_val.setStyleSheet("background-color : rgb(239,239,239); border-radius: 5px")
        fsm_val.setAlignment(Qt.AlignCenter)

        mode_val.setText("??")
        mode_val.setStyleSheet("background-color : rgb(239,239,239); border-radius: 5px")
        mode_val.setAlignment(Qt.AlignCenter)

        wheel_val.setText("??")
        wheel_val.setStyleSheet("background-color : rgb(239,239,239); border-radius: 5px")
        wheel_val.setAlignment(Qt.AlignCenter)

        clamp_val.setText("??")
        clamp_val.setStyleSheet("background-color : rgb(239,239,239); border-radius: 5px")
        clamp_val.setAlignment(Qt.AlignCenter)
        
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        vbox1_val = QVBoxLayout()
        vbox2_val = QVBoxLayout()

        vbox1.addWidget(fsm)
        vbox1.addWidget(mode)
        vbox2.addWidget(wheel)
        vbox2.addWidget(clamp)
        vbox1_val.addWidget(fsm_val)
        vbox1_val.addWidget(mode_val)
        vbox2_val.addWidget(wheel_val)
        vbox2_val.addWidget(clamp_val)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox1_val)
        hbox.addLayout(vbox2)
        hbox.addLayout(vbox2_val)

        self.setLayout(hbox)

class PodMovement(QWidget):
    def __init__(self, parent=None):
        super(PodMovement, self).__init__(parent)
        self.movement = QLabel(self)

        # TODO: if__ then display "Stopped", else display "Moving"
        self.movement.setText("Pod Movement\n\nStopped")
        self.movement.setStyleSheet("background-color : rgb(239,239,239); border-radius: 5px; font-weight: bold; border: 3px solid black")
        self.movement.setAlignment(Qt.AlignCenter)
        self.movement.resize(400, 200)
        self.movement.move(0,50)

class Telemetry(QWidget):
    def __init__(self, parent=None):
        super(Telemetry, self).__init__(parent)
        self.initUI()
    
    def initUI(self):
        status = QLabel(self)
        status.setText("Telemetry Status\n\n??")
        status.setStyleSheet("background-color : rgb(239,239,239); border-radius: 5px; font-weight: bold;")
        status.setAlignment(Qt.AlignCenter)

        button = QPushButton(self)
        button.setText("Clear Telemetry Faults")
        # TODO: set larger height
        button.setStyleSheet("background-color : rgb(241,241,241); font-weight: bold")
        button.clicked.connect(self.clearTelemetry)
        button.resize(400, 150)

        vbox = QVBoxLayout()

        # top_size = QSizePolicy(Preferred, Preferred)
        # top_size.setVerticalStretch(1)
        # status.setSizePolicy(top_size)
        # bot_size = QSizePolicy(Preferred, Preferred)
        # bot_size.setVerticalStretch(2)
        # button.setSizePolicy(bot_size)

        vbox.addWidget(status)
        vbox.addWidget(button)

        self.setLayout(vbox)

    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())

    def clearTelemetry(self):
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Do you want to clear telemetry faults?")
        self.msgBox.setWindowTitle("Clear Telemetry Button Pushed!")
        self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # TODO: clear telemetry faults here if button clicked
        returnValue = self.msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
        else:
            print("Action cancelled")


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Hyperloop GUI")
        self.setStyleSheet("background-color : white")

        hbox = QHBoxLayout(self)
		
        top_left = QFrame()
        top_left.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)

        # splitter1.addWidget(top_left)
        battery1_text = Battery1()
        splitter1.addWidget(battery1_text)
        battery2_text = Battery1()
        splitter1.addWidget(battery2_text)
        states = States()
        splitter1.addWidget(states)
        pod_movement = PodMovement()
        splitter1.addWidget(pod_movement)
        telemetry = Telemetry()
        splitter1.addWidget(telemetry)
        emergency_button = EmergencyButton()
        splitter1.addWidget(emergency_button)
        splitter1.setSizes([2, 2, 1, 200, 1, 200])

        splitter2 = QSplitter(Qt.Horizontal)
        sensors_tab = Tab()
        splitter2.addWidget(sensors_tab)
        splitter2.setSizes([150,200])
        splitter2.setStyleSheet("background-color: rgb(224,224,224)")
            
        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)
        splitter3.addWidget(bottom)
        splitter3.setSizes([50,800,100])
            
        hbox.addWidget(splitter3)
            
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
            
        self.setGeometry(300, 300, 300, 200)
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

