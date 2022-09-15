# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QWidget)

from PySide6 import QtWidgets

from pyqtgraph import PlotWidget
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.New = QAction(MainWindow)
        self.New.setObjectName(u"New")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.New.setIcon(icon)
        self.Open = QAction(MainWindow)
        self.Open.setObjectName(u"Open")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Open.setIcon(icon1)
        self.Open_Recent = QAction(MainWindow)
        self.Open_Recent.setObjectName(u"Open_Recent")
        self.save = QAction(MainWindow)
        self.save.setObjectName(u"save")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save.setIcon(icon2)
        self.Exit = QAction(MainWindow)
        self.Exit.setObjectName(u"Exit")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-closed-captioning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.testbtn = QMenu(self.menubar)
        self.testbtn.setObjectName(u"testbtn")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.testbtn.menuAction())
        self.menu_File.addAction(self.New)
        self.menu_File.addAction(self.Open)
        self.menu_File.addAction(self.Open_Recent)
        self.menu_File.addAction(self.save)
        self.menu_File.addAction(self.Exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.draw()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
#if QT_CONFIG(tooltip)
        self.New.setToolTip(QCoreApplication.translate("MainWindow", u"Open New File", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.New.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.Open.setText(QCoreApplication.translate("MainWindow", u"&Open", None))
#if QT_CONFIG(tooltip)
        self.Open.setToolTip(QCoreApplication.translate("MainWindow", u"Open a existing file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.Open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.Open_Recent.setText(QCoreApplication.translate("MainWindow", u"&Open Recent", None))
#if QT_CONFIG(tooltip)
        self.Open_Recent.setToolTip(QCoreApplication.translate("MainWindow", u"Open Recent files", None))
#endif // QT_CONFIG(tooltip)
        self.save.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(tooltip)
        self.save.setToolTip(QCoreApplication.translate("MainWindow", u"Save a file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Exit.setText(QCoreApplication.translate("MainWindow", u"&Exit", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.testbtn.setTitle(QCoreApplication.translate("MainWindow", u"test", None))
    # retranslateUi

    def draw(self):
        x = np.random.normal(size=1000)
        y = np.random.normal(size=(3,1000))
        for i in range(3):
            self.graphicsView.plot(x,y[i],pen=(i,3))

    def clear(self):
        self.graphicsView.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())