# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(110, 0))
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setMinimumSize(QSize(850, 65))
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.pushButton = QPushButton(self.frame_top_info)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(False)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        self.label_top_info_2.setFont(font4)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(110, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btnHome = QPushButton(self.frame_left_menu)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        self.btnHome.setFont(font5)
        self.btnHome.setLayoutDirection(Qt.LeftToRight)
        self.btnHome.setStyleSheet(u"QPushButton {\n"
"	background-image:url(:/16x16/icons/16x16/cil-home.png);\n"
"	background-position: bottom;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btnHome)

        self.pushButton_3 = QPushButton(self.frame_left_menu)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.btnClassify = QPushButton(self.frame_left_menu)
        self.btnClassify.setObjectName(u"btnClassify")
        self.btnClassify.setMinimumSize(QSize(0, 30))
        self.btnClassify.setFont(font5)
        self.btnClassify.setLayoutDirection(Qt.LeftToRight)
        self.btnClassify.setStyleSheet(u"QPushButton {\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	// background-image:url(:/16x16/icons/16x16/cil-home.png);\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btnClassify)

        self.btnSeg = QPushButton(self.frame_left_menu)
        self.btnSeg.setObjectName(u"btnSeg")
        self.btnSeg.setMinimumSize(QSize(0, 30))
        self.btnSeg.setFont(font5)
        self.btnSeg.setLayoutDirection(Qt.LeftToRight)
        self.btnSeg.setStyleSheet(u"QPushButton {\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	// background-image:url(:/16x16/icons/16x16/cil-home.png);\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btnSeg)

        self.btnFilter = QPushButton(self.frame_left_menu)
        self.btnFilter.setObjectName(u"btnFilter")
        self.btnFilter.setMinimumSize(QSize(0, 30))
        self.btnFilter.setFont(font5)
        self.btnFilter.setLayoutDirection(Qt.LeftToRight)
        self.btnFilter.setStyleSheet(u"QPushButton {\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	// background-image:url(:/16x16/icons/16x16/cil-home.png);\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btnFilter)

        self.btnLog = QPushButton(self.frame_left_menu)
        self.btnLog.setObjectName(u"btnLog")
        self.btnLog.setMinimumSize(QSize(0, 30))
        self.btnLog.setFont(font5)
        self.btnLog.setLayoutDirection(Qt.LeftToRight)
        self.btnLog.setStyleSheet(u"QPushButton {\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	// background-image:url(:/16x16/icons/16x16/cil-home.png);\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_6.addWidget(self.btnLog)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.label_user_icon = QLabel(self.frame_left_menu)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(1000, 10000))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        self.label_user_icon.setFont(font6)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	background-image: url(:/16x16/icons/16x16/cil-user.png);\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_user_icon)


        self.horizontalLayout_2.addWidget(self.frame_left_menu, 0, Qt.AlignHCenter)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setMinimumSize(QSize(850, 0))
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.diplay_page = QWidget()
        self.diplay_page.setObjectName(u"diplay_page")
        self.verticalLayout_13 = QVBoxLayout(self.diplay_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.openGLWidget = QOpenGLWidget(self.diplay_page)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.verticalLayout_13.addWidget(self.openGLWidget)

        self.stackedWidget.addWidget(self.diplay_page)
        self.log_page = QWidget()
        self.log_page.setObjectName(u"log_page")
        self.verticalLayout_5 = QVBoxLayout(self.log_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.log_page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.listWidget = QListWidget(self.groupBox)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_7.addWidget(self.listWidget)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.stackedWidget.addWidget(self.log_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_8 = QVBoxLayout(self.home_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setMargin(25)
        self.label.setOpenExternalLinks(True)

        self.verticalLayout_8.addWidget(self.label)

        self.stackedWidget.addWidget(self.home_page)
        self.filter_page = QWidget()
        self.filter_page.setObjectName(u"filter_page")
        self.verticalLayout_9 = QVBoxLayout(self.filter_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget = QWidget(self.filter_page)
        self.widget.setObjectName(u"widget")
        font7 = QFont()
        font7.setBold(False)
        font7.setItalic(False)
        self.widget.setFont(font7)
        self.verticalLayout_14 = QVBoxLayout(self.widget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.splitter = QSplitter(self.widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget1 = QWidget(self.splitter)
        self.widget1.setObjectName(u"widget1")
        self.verticalLayout_10 = QVBoxLayout(self.widget1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.widget1)
        self.checkBox.setObjectName(u"checkBox")
        font8 = QFont()
        font8.setFamilies([u"MS Shell Dlg 2"])
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        self.checkBox.setFont(font8)
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget1)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font8)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_2.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox_2)

        self.checkBox_6 = QCheckBox(self.widget1)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font8)
        self.checkBox_6.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.widget1)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font8)
        self.checkBox_7.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_7.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox_7)

        self.checkBox_3 = QCheckBox(self.widget1)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font8)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_3.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox_3)

        self.checkBox_8 = QCheckBox(self.widget1)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font8)
        self.checkBox_8.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_8.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox_8)

        self.checkBox_5 = QCheckBox(self.widget1)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font8)
        self.checkBox_5.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_5.setChecked(True)

        self.verticalLayout_10.addWidget(self.checkBox_5)

        self.splitter.addWidget(self.widget1)
        self.widget2 = QWidget(self.splitter)
        self.widget2.setObjectName(u"widget2")
        self.verticalLayout_11 = QVBoxLayout(self.widget2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBox_4 = QCheckBox(self.widget2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font8)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_4.setChecked(True)

        self.verticalLayout_11.addWidget(self.checkBox_4)

        self.checkBox_10 = QCheckBox(self.widget2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setFont(font8)
        self.checkBox_10.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_10.setChecked(True)

        self.verticalLayout_11.addWidget(self.checkBox_10)

        self.checkBox_9 = QCheckBox(self.widget2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setFont(font8)
        self.checkBox_9.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_9.setChecked(True)

        self.verticalLayout_11.addWidget(self.checkBox_9)

        self.checkBox_11 = QCheckBox(self.widget2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setFont(font8)
        self.checkBox_11.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_11.setChecked(True)

        self.verticalLayout_11.addWidget(self.checkBox_11)

        self.checkBox_13 = QCheckBox(self.widget2)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setFont(font8)
        self.checkBox_13.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.checkBox_13.setChecked(True)

        self.verticalLayout_11.addWidget(self.checkBox_13)

        self.checkBox_12 = QCheckBox(self.widget2)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setFont(font8)
        self.checkBox_12.setStyleSheet(u"QCheckBox {\n"
"	font: 50 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(0, 85, 127);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QCheckBox:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QCheckBox:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_11.addWidget(self.checkBox_12)

        self.splitter.addWidget(self.widget2)

        self.verticalLayout_12.addWidget(self.splitter)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	// background-image:url(:/16x16/icons/16x16/cil-home.png);\n"
"	background-position: left;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(52, 59, 72);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	padding: 1em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_12.addWidget(self.pushButton_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)


        self.verticalLayout_9.addWidget(self.widget)

        self.stackedWidget.addWidget(self.filter_page)

        self.horizontalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.frame_main.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"LiDAR Point Cloud Classifier", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Users\\user\\Desktop\\SPL3\\DATA", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open LiDAR", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.btnHome.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.btnClassify.setText(QCoreApplication.translate("MainWindow", u"Classify", None))
        self.btnSeg.setText(QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.btnFilter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.btnLog.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.label_user_icon.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Log Page", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Log will display here", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#16a0ff;\">LiDAR Point Cloud Classifier</span></p><p align=\"center\"><span style=\" color:#8590c8;\">A GUI Application for Classifying and segmenting large scale </span><a href=\"https://becominghuman.ai/whats-lidar-and-what-s-3d-point-cloud-1f4ccd998e7b/\"><span style=\" text-decoration: underline; color:#0264af;\">LiDAR Point Cloud</span></a><span style=\" color:#8590c8;\"> files. We can also Display and Save the Classified point Cloud objects in a efficient way by this app. The application created using </span><a href=\"https://www.python.org/\"><span style=\" text-decoration: underline; color:#0264af;\">Python</span></a><span style=\" color:#8590c8;\"> and </span><a href=\"https://pypi.org/project/PySide6/\"><span style=\" text-decoration: underline; color:#0264af;\">PySide6</span></a><span style=\" color:#8590c8;\">, </span><a href=\"https://pytorch.org/\"><span style=\" text-decoration: underline; color:#0264af;\">Pytorch</span>"
                        "</a><span style=\" color:#8590c8;\">,</span><a href=\"http://www.open3d.org/\"><span style=\" text-decoration: underline; color:#0264af;\">Open3D</span></a></p><p align=\"center\"><span style=\" color:#8590c8;\">MIT License</span></p><p align=\"center\"><span style=\" color:#16a0ff;\">Created by: </span><a href=\"https://github.com/bsse1009\"><span style=\" text-decoration: underline; color:#0264af;\">bsse1009@iit.du.ac.bd</span></a><span style=\" color:#16a0ff;\"> @GitHub</span></p><p align=\"center\"><br/></p><p align=\"right\"><a href=\"https://github.com/bsse1009/LiDAR-Data-Classification\"><span style=\" text-decoration: underline; color:#0264af;\">GitHub Repository</span></a></p><p align=\"right\"><a href=\"https://github.com/bsse1009/LiDAR-Data-Classification\"><span style=\" text-decoration: underline; color:#0264af;\">Releases</span></a></p><p align=\"right\"><a href=\"https://github.com/bsse1009/LiDAR-Data-Classification/issues/new\"><span style=\" text-decoration: underline; color:#0264af;\">Report "
                        "an issue</span></a></p><p align=\"right\"><br/></p><p align=\"center\"><br/></p></body></html> ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Ceiling", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"floor", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"wall", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"beam", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"column", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"window", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"door", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"table", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"chair", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"sofa", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"board", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"bookcase", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"clutter", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: Md Ibrahim Khalil", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

