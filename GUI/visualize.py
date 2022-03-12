from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys
import constants

app = QtGui.QApplication([])
view = gl.GLViewWidget()
view.show()

x = gl.GLGridItem()
y = gl.GLGridItem()
z = gl.GLGridItem()
view.addItem(x)
view.addItem(y)
view.addItem(z)
x.rotate(90, 0, 1, 0)
y.rotate(90, 1, 0, 0)

# coordinates
point1 = np.array([0, 0, 0])
point2 = np.array([0, 3, 0])

center = (point1 + point2) / 2
radius = np.linalg.norm(point2 - point1) / 2

md = gl.MeshData.sphere(rows=10, cols=20, radius=radius)

m1 = gl.GLMeshItem(
    meshdata=md,
    smooth=True,
    color=(1, 0, 0, 0.2),
    shader="balloon",
    glOptions="additive",
)
m1.scale(1, 1, 2)
m1.rotate(90, 1, 0, 0)
t = 0


def rotate():
    global t
    m1.rotate(constants.PITCH[t], 1, 0, 0)
    m1.rotate(constants.YAW[t], 0, 1, 0)
    m1.rotate(constants.ROLL[t], 0, 0, 1)
    t += 1
    if (t == len(constants.PITCH)):
        timer.stop()


timer = QtCore.QTimer()
timer.timeout.connect(rotate)
timer.start(1000)

view.addItem(m1)

if __name__ == "__main__":

    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtGui.QApplication.instance().exec_()
