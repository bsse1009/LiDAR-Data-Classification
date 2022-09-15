################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import pyqtgraph.opengl as gl



## ==> MAIN WINDOW
from GUI import Ui_MainWindow
from ui_splash_screen import Ui_SplashScreen

## ==> GLOBALS
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
        ## Add a grid to the view
        self.g = gl.GLGridItem()
        self.g.scale(2,2,1)
        self.g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        self.w.addItem(self.g)
        self.w1.addItem(self.g)

        self.ui.pushButton.clicked.connect(lambda:self.draw3D())

        self.ui.btnClassify.clicked.connect(lambda:self.draw3D())


    def draw3D(self): 
        # self.ui.stackedWidget.setCurrentWidget(self.ui.classification_page)
        x = np.linspace(-8, 8, 50)
        y = np.linspace(-8, 8, 50)
        z = 0.1 * ((x.reshape(50,1) ** 2) - (y.reshape(1,50) ** 2))
        p2 = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader='normalColor')
        p2.translate(-10,-10,0)
        self.w.addItem(p2)

    def draw(self):
        x = []
        y = []
        with open('C://Users//user//Desktop//SPL3//LiDAR_Classification_APP//Final//Data//KME_cars.xyz', 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    continue
                x.append(float(line.split(';')[0]))
                y.append(float(line.split(';')[1]))

        self.ui.graphicsView.plot(x, y, pen=(i,3))

    def clear(self):
        self.ui.graphicsView.clear()


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(150, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(300, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
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
