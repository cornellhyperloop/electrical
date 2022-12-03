from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph.opengl as gl
import numpy as np
import constants as cons
import random
from OpenGL.GL import *


class Pod(QOpenGLWidget):

    def __init__(self, random_rotate, parent=None):
        super(Pod, self).__init__(parent)
        self.random_rotate = random_rotate
        # Create object form GLviewWidget
        self.view = gl.GLViewWidget()
        #self.view.setFixedSize(500, 500)
        x = gl.GLGridItem()
        y = gl.GLGridItem()
        z = gl.GLGridItem()
        x.rotate(90, 0, 1, 0)
        y.rotate(90, 1, 0, 0)
        self.view.addItem(x)
        self.view.addItem(y)
        self.view.addItem(z)


        self.layout = QGridLayout()
        self.layout.addWidget(self.view)
        # coordinates
        point1 = np.array([0, 0, 0])
        point2 = np.array([0, 3, 0])

        center = (point1 + point2) / 2
        radius = np.linalg.norm(point2 - point1) / 2

        self.md = gl.MeshData.sphere(rows=10, cols=20, radius=radius)

        self.m1 = gl.GLMeshItem(
            meshdata=self.md,
            smooth=True,
            color=(1, 0, 0, 0.2),
            shader="balloon",
            glOptions="additive",
        )
        self.m1.scale(1, 1, 2)
        self.m1.rotate(90, 1, 0, 0)
        self.t = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.paintGL)
        self.timer.start(1000)

        self.setLayout(self.layout)
        #self.layout.setGeometry(100,100,100,100)

    def initializeGL(self):
        pass

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)

    def paintGL(self):
        if (self.t == len(cons.PITCH)):
            self.t = 0
        
        if (self.random_rotate):
            rotate_pitch = random.randint(0, 360)
            rotate_yaw = random.randint(0, 360)
            rotate_roll = random.randint(0, 360)
        else:
            rotate_pitch = cons.PITCH[self.t]
            rotate_yaw = cons.YAW[self.t]
            rotate_roll = cons.ROLL[self.t]

        self.m1.rotate(rotate_pitch, 1, 0, 0)
        self.m1.rotate(rotate_yaw, 0, 1, 0)
        self.m1.rotate(rotate_roll, 0, 0, 1)
        self.t += 1

        self.view.addItem(self.m1)
