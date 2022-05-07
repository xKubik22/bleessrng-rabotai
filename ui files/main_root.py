# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.obj_name_label = QtWidgets.QLabel(self.centralwidget)
        self.obj_name_label.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.obj_name_label.setObjectName("obj_name_label")
        self.obj_name_entery = QtWidgets.QLineEdit(self.centralwidget)
        self.obj_name_entery.setGeometry(QtCore.QRect(10, 40, 331, 20))
        self.obj_name_entery.setObjectName("obj_name_entery")
        self.att_as_box = QtWidgets.QCheckBox(self.centralwidget)
        self.att_as_box.setGeometry(QtCore.QRect(10, 70, 101, 17))
        self.att_as_box.setObjectName("att_as_box")
        self.att_vp_box = QtWidgets.QCheckBox(self.centralwidget)
        self.att_vp_box.setGeometry(QtCore.QRect(10, 90, 101, 17))
        self.att_vp_box.setObjectName("att_vp_box")
        self.att_pdn_box = QtWidgets.QCheckBox(self.centralwidget)
        self.att_pdn_box.setGeometry(QtCore.QRect(10, 110, 141, 17))
        self.att_pdn_box.setObjectName("att_pdn_box")
        self.kp_box = QtWidgets.QCheckBox(self.centralwidget)
        self.kp_box.setGeometry(QtCore.QRect(10, 130, 121, 17))
        self.kp_box.setObjectName("kp_box")
        self.di_nsd_box = QtWidgets.QCheckBox(self.centralwidget)
        self.di_nsd_box.setGeometry(QtCore.QRect(10, 150, 121, 17))
        self.di_nsd_box.setObjectName("di_nsd_box")
        self.di__box = QtWidgets.QCheckBox(self.centralwidget)
        self.di__box.setGeometry(QtCore.QRect(10, 170, 121, 17))
        self.di__box.setObjectName("di__box")
        self.other_box = QtWidgets.QCheckBox(self.centralwidget)
        self.other_box.setGeometry(QtCore.QRect(10, 210, 121, 17))
        self.other_box.setObjectName("other_box")
        self.test_box = QtWidgets.QCheckBox(self.centralwidget)
        self.test_box.setGeometry(QtCore.QRect(10, 190, 121, 17))
        self.test_box.setObjectName("test_box")
        self.pelena_count_box = QtWidgets.QSpinBox(self.centralwidget)
        self.pelena_count_box.setGeometry(QtCore.QRect(360, 120, 42, 22))
        self.pelena_count_box.setMinimum(0)
        self.pelena_count_box.setProperty("value", 0)
        self.pelena_count_box.setObjectName("pelena_count_box")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 140, 101, 16))
        self.label_2.setObjectName("label_2")
        self.vsh_count_box = QtWidgets.QSpinBox(self.centralwidget)
        self.vsh_count_box.setGeometry(QtCore.QRect(360, 160, 42, 22))
        self.vsh_count_box.setMinimum(0)
        self.vsh_count_box.setProperty("value", 0)
        self.vsh_count_box.setObjectName("vsh_count_box")
        self.att_as_count_box = QtWidgets.QSpinBox(self.centralwidget)
        self.att_as_count_box.setGeometry(QtCore.QRect(270, 90, 42, 22))
        self.att_as_count_box.setMinimum(1)
        self.att_as_count_box.setObjectName("att_as_count_box")
        self.vibrik_count_box = QtWidgets.QSpinBox(self.centralwidget)
        self.vibrik_count_box.setGeometry(QtCore.QRect(360, 140, 42, 22))
        self.vibrik_count_box.setMinimum(0)
        self.vibrik_count_box.setProperty("value", 0)
        self.vibrik_count_box.setObjectName("vibrik_count_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 120, 101, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 160, 101, 16))
        self.label_3.setObjectName("label_3")
        self.di_nsd_win_count_box = QtWidgets.QSpinBox(self.centralwidget)
        self.di_nsd_win_count_box.setGeometry(QtCore.QRect(400, 200, 42, 22))
        self.di_nsd_win_count_box.setMinimum(1)
        self.di_nsd_win_count_box.setObjectName("di_nsd_win_count_box")
        self.di_nsd_savz_count_box = QtWidgets.QSpinBox(self.centralwidget)
        self.di_nsd_savz_count_box.setGeometry(QtCore.QRect(400, 230, 42, 22))
        self.di_nsd_savz_count_box.setMinimum(1)
        self.di_nsd_savz_count_box.setObjectName("di_nsd_savz_count_box")
        self.di_nsd_szi_count_box = QtWidgets.QSpinBox(self.centralwidget)
        self.di_nsd_szi_count_box.setGeometry(QtCore.QRect(400, 260, 42, 22))
        self.di_nsd_szi_count_box.setMinimum(1)
        self.di_nsd_szi_count_box.setObjectName("di_nsd_szi_count_box")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 260, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 230, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 200, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(270, 320, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(270, 290, 131, 16))
        self.label_8.setObjectName("label_8")
        self.di_nsd_adm_instruction_box = QtWidgets.QCheckBox(self.centralwidget)
        self.di_nsd_adm_instruction_box.setGeometry(QtCore.QRect(400, 290, 121, 17))
        self.di_nsd_adm_instruction_box.setObjectName("di_nsd_adm_instruction_box")
        self.di_nsd_polz_box = QtWidgets.QCheckBox(self.centralwidget)
        self.di_nsd_polz_box.setGeometry(QtCore.QRect(400, 320, 121, 17))
        self.di_nsd_polz_box.setObjectName("di_nsd_polz_box")
        self.di_nsd_savz_count_box_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.di_nsd_savz_count_box_2.setGeometry(QtCore.QRect(400, 410, 42, 22))
        self.di_nsd_savz_count_box_2.setMinimum(1)
        self.di_nsd_savz_count_box_2.setObjectName("di_nsd_savz_count_box_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 410, 131, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(270, 380, 101, 16))
        self.label_10.setObjectName("label_10")
        self.di_nsd_win_count_box_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.di_nsd_win_count_box_2.setGeometry(QtCore.QRect(400, 380, 42, 22))
        self.di_nsd_win_count_box_2.setMinimum(1)
        self.di_nsd_win_count_box_2.setObjectName("di_nsd_win_count_box_2")
        self.other_commentary = QtWidgets.QLineEdit(self.centralwidget)
        self.other_commentary.setGeometry(QtCore.QRect(10, 240, 251, 20))
        self.other_commentary.setObjectName("other_commentary")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Расчетка"))
        self.obj_name_label.setText(_translate("MainWindow", "Название объекта"))
        self.att_as_box.setText(_translate("MainWindow", "Аттестация АС"))
        self.att_vp_box.setText(_translate("MainWindow", "Аттестация ВП"))
        self.att_pdn_box.setText(_translate("MainWindow", "Аттестация ИСПДн"))
        self.kp_box.setText(_translate("MainWindow", "КП"))
        self.di_nsd_box.setText(_translate("MainWindow", "ДИ НСД"))
        self.di__box.setText(_translate("MainWindow", "ДИ ПЭМИН"))
        self.other_box.setText(_translate("MainWindow", "Другое"))
        self.test_box.setText(_translate("MainWindow", "Тестирование"))
        self.label_2.setText(_translate("MainWindow", "Монтаж вибрики"))
        self.label.setText(_translate("MainWindow", "Монтаж пелены"))
        self.label_3.setText(_translate("MainWindow", "Монтаж ВШ"))
        self.label_4.setText(_translate("MainWindow", "Установка НСД"))
        self.label_5.setText(_translate("MainWindow", "Установка антивируса"))
        self.label_6.setText(_translate("MainWindow", "Установка винды"))
        self.label_7.setText(_translate("MainWindow", "Разрешиловка"))
        self.label_8.setText(_translate("MainWindow", "Инструкция сис. админа"))
        self.di_nsd_adm_instruction_box.setText(_translate("MainWindow", "Есть"))
        self.di_nsd_polz_box.setText(_translate("MainWindow", "Есть"))
        self.label_9.setText(_translate("MainWindow", "Проведение СИ"))
        self.label_10.setText(_translate("MainWindow", "Установка Сонаты"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())