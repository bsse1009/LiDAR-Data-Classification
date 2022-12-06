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
from datasets.indoor3d_util import class2label


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
        self.res_dir = 'log/visual'
        self.w1 = gl.GLViewWidget()
        self.w1.setCameraPosition(distance=50)

        self.ui.verticalLayout_13.addWidget(self.w)
        # self.ui.classification_layout.addWidget(self.w1)
        # self.ui.stackedWidget.setCurrentWidget(self.ui.display_page)
        # Add a grid to the view
        self.g = gl.GLGridItem()
        self.g.scale(2, 2, 1)
        # draw grid after surfaces since they may be translucent
        self.g.setDepthValue(10)
        self.w.addItem(self.g)
        self.w1.addItem(self.g)
        self.pcd = o3d.geometry.PointCloud()
        self.ui.pushButton.clicked.connect(lambda: self.open_file())
        self.ui.btnSeg.clicked.connect(lambda: self.prediction())
        self.ui.btnClassify.clicked.connect(self.buttonClick)

        self.classes = ["ceiling", "floor", "column", "table", "door", "wall", "beam", "window", "sofa", "chair", "board",
                        "clutter", "bookcase"]
        self.filtered_classes = []
        self.ui.pushButton_2.clicked.connect(self.buttonClick)
        self.ui.btn_toggle_menu.clicked.connect(self.buttonClick)
        self.ui.btn_minimize.clicked.connect(self.buttonClick)
        self.ui.btn_maximize_restore.clicked.connect(self.buttonClick)
        self.ui.btn_close.clicked.connect(self.buttonClick)
        self.ui.btnHome.clicked.connect(self.buttonClick)
        self.ui.btnDisplay.clicked.connect(self.buttonClick)
        self.ui.btnFilter.clicked.connect(self.buttonClick)
        self.ui.btnLog.clicked.connect(self.buttonClick)
        self.checked_all_checkboxes()

    def open_file(self):
        # self.clear()
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c://Users//user//Desktop//SPL3//Project//LiDAR_Classification_APP//src//data', "Point cloud files (*.ply *.txt *.xyz *.pcd *.las *.laz *.obj *.off *.stl *.vtk *.bin *.pts *.csv *.asc *.npy)")
        self.path = fname[0]
        self.file = self.path.strip().split('/')[-1]
        self.ext = self.path.strip().split('.')[-1]
        self.log("Open file: %s" % self.file)
        if self.ext == 'off':
            with open(self.path, 'r') as f:
                points, _ = self.read_off(f)
                self.points = np.array(points)
        else:
            self.pcd = point_cloud_reader(self.path)
            self.points = self.pcd.points
            self.colors = self.pcd.colors
        self.log("Displaying raw point cloud")
        self.draw_raw()

    def read_off(self, file):
        if 'OFF' != file.readline().strip():
            raise('Not a valid OFF header')

        n_verts, n_faces, __ = tuple(
            [int(s) for s in file.readline().strip().split(' ')])
        # print(n_verts, n_faces, __)
        verts = [[float(s) for s in file.readline().strip().split(' ')]
                 for i_vert in range(n_verts)]
        faces = [[int(s) for s in file.readline().strip().split(' ')][1:]
                 for i_face in range(n_faces)]
        return verts, faces

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_toggle_menu":
            pass

        elif btnName == "btn_minimize":
            pass

        if btnName == "btn_maximize_restore":
            pass

        if btnName == "btn_close":
            self.clear()

        if btnName == "btnHome":
            self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

        elif btnName == "btnFilter":
            self.ui.stackedWidget.setCurrentWidget(self.ui.filter_page)

        elif btnName == "btnLog":
            self.ui.stackedWidget.setCurrentWidget(self.ui.log_page)

        elif btnName == "btnDisplay":
            self.ui.stackedWidget.setCurrentWidget(self.ui.diplay_page)

        elif btnName == "pushButton_2":
            tem = []
            widgets = (self.ui.verticalLayout_10.itemAt(i).widget()
                       for i in range(self.ui.verticalLayout_10.count()))
            for widget in widgets:
                if isinstance(widget, QCheckBox):
                    print("checkBox: %s  - %s" %
                          (widget.objectName(), widget.checkState()))
                    if widget.isChecked():
                        tem.append(class2label[widget.objectName()])

            widgets = (self.ui.verticalLayout_11.itemAt(i).widget()
                       for i in range(self.ui.verticalLayout_11.count()))
            for widget in widgets:
                if isinstance(widget, QCheckBox):
                    print("checkBox: %s  - %s" %
                          (widget.objectName(), widget.checkState()))
                    if widget.isChecked():
                        tem.append(class2label[widget.objectName()])
            print(tem)
            self.filtered_classes = tem

    def checked_all_checkboxes(self):
        self.ui.ceiling.setChecked(True)
        self.ui.floor.setChecked(True)
        self.ui.column.setChecked(True)
        self.ui.table.setChecked(True)
        self.ui.door.setChecked(True)
        self.ui.wall.setChecked(True)
        self.ui.beam.setChecked(True)
        self.ui.window.setChecked(True)
        self.ui.sofa.setChecked(True)
        self.ui.chair.setChecked(True)
        self.ui.board.setChecked(True)
        self.ui.clutter.setChecked(True)
        self.ui.bookcase.setChecked(True)

    def view_point_cloud(self, pcd_list):
        def rotate_view(vis):
            self.log("rotate_view")
            ctr = vis.get_view_control()
            ctr.rotate(10.0, 0.0)
            return False

        def change_background_to_black(vis):
            self.log("changed_background_to_black")
            opt = vis.get_render_option()
            opt.background_color = np.asarray([0, 0, 0])
            return False
        key_to_callback = {}
        key_to_callback[ord("K")] = change_background_to_black
        key_to_callback[ord("R")] = rotate_view

        o3d.visualization.draw_geometries_with_key_callbacks(
            pcd_list, key_to_callback)

    def log(self, txt: str) -> None:
        QListWidgetItem(txt, self.ui.listWidget)
        if int(self.ui.listWidget.count()) > 2000:
            itemtodel = self.ui.listWidget.item(0)
            self.ui.listWidget.takeItem(0)
            del itemtodel

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
        p2 = gl.GLScatterPlotItem(
            pos=self.points, color=(1, 1, 1, .4), size=0.5)
        self.w.addItem(p2)

    def prediction(self):
        self.log("Predicting.....")
        if self.has_predictions():
            print("Predictions are available")
            self.log("Predictions are available")
        else:
            predict({"file": self.file, "num_votes": 1,
                    "test_area": 5, "visual": True, "no_wall": False})
            self.log("predicting file: %s " % self.file)
        self.display_results()

    def has_predictions(self):
        dirs = os.listdir(self.res_dir)
        f = self.file.split('.')[0]+'_pred.obj'
        print(f)
        if f in dirs:
            return True
        return False

    def display_results(self):
        self.log("displaying results: \n")
        pred_f = os.path.join(
            self.res_dir, self.file.split('.')[0]+'_pred.obj')
        gt_f = os.path.join(self.res_dir, self.file.split('.')[0]+'_gt.obj')
        pcd_pred = point_cloud_reader(pred_f)
        pcd_gt = point_cloud_reader(gt_f)

        if self.filtered_classes and len(self.filtered_classes) < 13:
            label_f = os.path.join(
                self.res_dir, self.file.split('.')[0]+'.txt')
            labels = np.loadtxt(label_f)
            filterd_idx = [
                True if l in self.filtered_classes else False for l in labels]
            points_pred = np.asarray(pcd_pred.points)[filterd_idx]
            colors_pred = np.asarray(pcd_pred.colors)[filterd_idx]
            pcd_pred.points = o3d.utility.Vector3dVector(points_pred)
            pcd_pred.colors = o3d.utility.Vector3dVector(colors_pred)
            # print(points_pred.shape, colors_pred.shape)
            points_gt = np.asarray(pcd_gt.points)[filterd_idx]
            colors_gt = np.asarray(pcd_gt.colors)[filterd_idx]
            pcd_gt.points = o3d.utility.Vector3dVector(points_gt)
            pcd_gt.colors = o3d.utility.Vector3dVector(colors_gt)

        # points = np.asarray(pcd_pred.points)
        # points += [10, 10, 0]
        # pcd_pred.points = o3d.utility.Vector3dVector(points)
        pcd_pred.translate((2, 2, 0))
        pcd_gt.translate((15, 2, 0))

        bbox = pcd_pred.get_axis_aligned_bounding_box()
        bbox.color = (1.0, 0.5, 0.0)

        lines = open("log/single_eval.txt", "r").readlines()[-5:]
        print(lines)
        self.log(''.join(lines))
        self.view_point_cloud([pcd_gt, pcd_pred, bbox])

    def clear(self):
        self.w1.clear()
        self.w.clear()
        self.w.addItem(self.g)
        self.w1.addItem(self.g)


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
        self.timer.start(100)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText(
            "<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(300, lambda: self.ui.label_description.setText(
            "<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_description.setText(
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
        self.ui.progressBar.setValue(counter*4)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 20:
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
