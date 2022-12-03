################################################################################
##
# BY: Md Ibrahim Khalil
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
##
################################################################################

import sys
import os
import platform
import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pyqtgraph.opengl as gl
import open3d as o3d
from DataManager.read_point_cloud import point_cloud_reader
from prediction import predict

# ==> MAIN WINDOW
from GUI.GUI import Ui_MainWindow
from GUI.ui_splash_screen import Ui_SplashScreen

# ==> GLOBALS
counter = 0

# YOUR APPLICATION


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.w = gl.GLViewWidget()
        self.w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
        self.w.setCameraPosition(distance=50)

        self.w1 = gl.GLViewWidget()
        self.w1.setCameraPosition(distance=50)

        self.ui.display_layout.addWidget(self.w)
        self.ui.classification_layout.addWidget(self.w1)
        self.ui.stackedWidget.setCurrentWidget(self.ui.display_page)
        # Add a grid to the view
        self.g = gl.GLGridItem()
        self.g.scale(2, 2, 1)
        # draw grid after surfaces since they may be translucent
        self.g.setDepthValue(10)
        self.w.addItem(self.g)
        self.w1.addItem(self.g)
        self.pcd = o3d.geometry.PointCloud()
        self.ui.pushButton.clicked.connect(lambda: self.open_file())

        self.ui.btnClassify.clicked.connect(lambda: self.prediction())

    def open_file(self):
        self.clear()
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c://Users//user//Desktop//SPL3//Project//LiDAR_Classification_APP//src//data', "Point cloud files (*.ply *.txt *.xyz *.pcd *.las *.laz *.obj *.off *.stl *.vtk *.bin *.pts *.csv *.asc *.npy)")
        self.path = fname[0]
        self.file = self.path.strip().split('/')[-1]
        print(self.path)
        self.pcd = point_cloud_reader(self.path)
        self.points = self.pcd.points
        self.colors = self.pcd.colors
        self.draw_raw()

    def view_point_cloud(self):
        o3d.visualization.draw_geometries([self.pcd],
                                          width=1850,
                                          height=920,
                                          #   left=10,
                                          #   top=10
                                          )

    def draw3D(self):
        # self.ui.stackedWidget.setCurrentWidget(self.ui.classification_page)
        x = np.linspace(-8, 8, 50)
        y = np.linspace(-8, 8, 50)
        z = 0.1 * ((x.reshape(50, 1) ** 2) - (y.reshape(1, 50) ** 2))
        print(x, z)
        p2 = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader='normalColor')
        p2.translate(-10, -10, 0)
        self.w.addItem(p2)

    def draw_raw(self):
        self.clear()
        p2 = gl.GLScatterPlotItem(pos = self.points, color=(1,1,1,.4), size=0.5)
        self.w.addItem(p2)

    def prediction(self):
        if self.has_predictions():
            print("Predictions are available")
        else:
            predict({"file": self.file, "num_votes": 1, "test_area": 5, "visual": True})

    def has_predictions(self):
        dirs = os.listdir('log/visual')
        f = self.file.split('.')[0]+'_pred.obj'
        print(f)
        if  f in dirs:
            return True
        return False


    def clear(self):
        self.w1.clear()


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # UI ==> INTERFACE CODES
        ########################################################################

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText(
            "<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(150, lambda: self.ui.label_description.setText(
            "<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(300, lambda: self.ui.label_description.setText(
            "<strong>LOADING</strong> USER INTERFACE"))

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    # ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 10:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
