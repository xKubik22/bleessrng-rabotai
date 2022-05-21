from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

from config import Config
from object import Object
from works_indexes import indexes
from write_works import WorksAdder
cwd = os.getcwd()
sys.path.append(cwd + "\\ui files")
import main_root


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_root.Ui_MainWindow()
        self.ui.setupUi(self)
        self.hide_widgets()
        self.ui.other_commentary.setEnabled(False)
        self.ui.att_as_box.toggled.connect(self.show_as_widgets)
        self.ui.att_vp_box.toggled.connect(self.show_vp_widgets)
        self.ui.di_pemin_box.toggled.connect(self.show_di_widgets)
        self.ui.di_nsd_box.toggled.connect(self.show_di_widgets)
        self.ui.other_box.toggled.connect(self.enable_commentary)
        self.ui.att_pdn_box.toggled.connect(self.show_pdn_widgets)
        self.ui.done_button.clicked.connect(self.execute)
        self.ui.file_path_button.triggered.connect(self.get_calc_file_path)

    def get_calc_file_path(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбор файла расчета')[0]
        if len(path) != 0:
            path = path.replace('/', '\\')
            Config.change_calc_file_path(path)

    def get_works(self):
            works = [0] * 19
            index = indexes

            if self.ui.att_as_box.isChecked() and self.ui.att_as_box.isEnabled():
                works[index['Аттестация АС']] = self.ui.att_as_count_box.value()

            if self.ui.att_vp_box.isChecked() and self.ui.att_vp_box.isEnabled():
                works[index['Аттестация Вп']] = 1
                works[index['Пелена']] = self.ui.pelena_count_box.value()
                works[index['ВШ']] = self.ui.vsh_count_box.value()
                works[index['Вибрики']] = self.ui.vibrik_count_box.value()

            if self.ui.att_pdn_box.isChecked() and self.ui.att_pdn_box.isEnabled():
                works[index['Аттестация ИСПДн']] = 1

            if self.ui.kp_box.isChecked() and self.ui.kp_box.isEnabled():
                works[index['КП']] = 1

            if self.ui.test_box.isChecked() and self.ui.test_box.isEnabled():
                works[index['Тестирование']] = 1

            if self.ui.di_nsd_box.isChecked() and self.ui.di_nsd_box.isEnabled():
                works[index['Винда']] = self.ui.di_nsd_win_count_box.value()
                works[index['САВЗ']] = self.ui.di_nsd_savz_count_box.value()
                works[index['СЗИ от НСД']] = self.ui.di_nsd_szi_count_box.value()

                if self.ui.di_nsd_adm_instruction_box.isChecked():
                    works[index['Сис Админ']] = 1

                if self.ui.di_nsd_polz_box.isChecked():
                    works[index['Разрешиловка']] = 1

            if self.ui.other_box.isChecked() and self.ui.other_commentary.isEnabled():
                works[index['Другое']] = self.ui.other_commentary.text()

            if self.ui.di_pemin_box.isChecked() and self.ui.di_pemin_box.isEnabled():
                works[index['СИ']] = self.ui.di_pemin_si_count_box.value()
                works[index['Соната']] = self.ui.di_pemin_szi_count_box.value()

            return works

    def execute(self):
        works = self.get_works()
        obj = Object(self.ui.obj_name_entery.text(), works)
        WorksAdder(obj)

    def show_pdn_widgets(self):
        if self.ui.att_pdn_box.isChecked():
            self.disable_check_boxes()
            self.ui.att_pdn_box.setEnabled(True)
        else:
            self.enable_check_boxes()

    def hide_widgets(self):
        self.ui.att_as_count_box.hide()
        self.ui.frame_vp.hide()
        self.ui.frame_di_pemin.hide()
        self.ui.frame_di_nsd.hide()

    def enable_commentary(self):
        if self.ui.other_box.isChecked():
            self.ui.other_commentary.setEnabled(True)
        else:
            self.ui.other_commentary.setEnabled(False)

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

