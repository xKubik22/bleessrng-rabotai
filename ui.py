from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd + "\\ui files")
import main_root


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_root.Ui_MainWindow()
        self.ui.setupUi(self)
        self.hide_widgets()
        self.ui.att_as_box.toggled.connect(self.show_as_widgets)
        self.ui.att_vp_box.toggled.connect(self.show_vp_widgets)
        self.ui.di_pemin_box.toggled.connect(self.show_di_widgets)
        self.ui.di_nsd_box.toggled.connect(self.show_di_widgets)
        self.ui.done_button.clicked.connect(self.execute)

    def execute(self):
        states = {}

    def hide_widgets(self):
        self.ui.att_as_count_box.hide()
        self.ui.frame_vp.hide()
        self.ui.frame_di_pemin.hide()
        self.ui.frame_di_nsd.hide()

    def show_widgets(self):
        self.ui.att_as_count_box.show()
        self.ui.frame_vp.show()
        self.ui.frame_di_pemin.show()
        self.ui.frame_di_nsd.show()

    def disable_check_boxes(self):
        self.ui.att_vp_box.setEnabled(False)
        self.ui.att_as_box.setEnabled(False)
        self.ui.att_pdn_box.setEnabled(False)
        self.ui.di_pemin_box.setEnabled(False)
        self.ui.di_nsd_box.setEnabled(False)
        self.ui.test_box.setEnabled(False)
        self.ui.kp_box.setEnabled(False)

    def enable_check_boxes(self):
        self.ui.att_vp_box.setEnabled(True)
        self.ui.att_as_box.setEnabled(True)
        self.ui.att_pdn_box.setEnabled(True)
        self.ui.di_pemin_box.setEnabled(True)
        self.ui.di_nsd_box.setEnabled(True)
        self.ui.test_box.setEnabled(True)
        self.ui.kp_box.setEnabled(True)

    def show_as_widgets(self):
        if self.ui.att_as_box.isChecked():
            self.hide_widgets()
            self.ui.att_as_count_box.show()
            self.disable_check_boxes()
            self.ui.att_as_box.setEnabled(True)
        else:
            self.enable_check_boxes()
            self.ui.att_as_count_box.hide()

    def show_di_widgets(self):
        if self.ui.di_nsd_box.isChecked() or self.ui.di_pemin_box.isChecked():
            self.disable_check_boxes()
            self.ui.di_nsd_box.setEnabled(True)
            self.ui.di_pemin_box.setEnabled(True)
            self.ui.kp_box.setEnabled(True)
        else:
            self.enable_check_boxes()

        if self.ui.di_nsd_box.isChecked():
            self.ui.frame_di_nsd.show()
        else:
            self.ui.frame_di_nsd.hide()

        if self.ui.di_pemin_box.isChecked():
            self.ui.frame_di_pemin.show()
        else:
            self.ui.frame_di_pemin.hide()

    def show_vp_widgets(self):
        if self.ui.att_vp_box.isChecked():
            self.disable_check_boxes()
            self.ui.att_vp_box.setEnabled(True)
            self.hide_widgets()
            self.ui.frame_vp.show()
        else:
            self.enable_check_boxes()
            self.ui.frame_vp.hide()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = MainWindow()
    c.show()
    sys.exit(app.exec_())

