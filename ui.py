# Form implementation generated from reading ui file 'os.ui'
# Created by: PyQt5 UI code generator 5.12.1

from PyQt5 import QtCore, QtGui, QtWidgets

import machine


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fcfs_b = QtWidgets.QPushButton(self.centralwidget)
        self.fcfs_b.setGeometry(QtCore.QRect(110, 449, 61, 25))
        self.fcfs_b.setObjectName("fcfs_b")
        self.io_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.io_1.setGeometry(QtCore.QRect(460, 100, 92, 23))
        self.io_1.setChecked(False)
        self.io_1.setObjectName("io_1")
        self.bt2_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt2_1.setEnabled(False)
        self.bt2_1.setGeometry(QtCore.QRect(390, 100, 48, 26))
        self.bt2_1.setMaximum(999)
        self.bt2_1.setObjectName("bt2_1")
        self.iot_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.iot_1.setEnabled(False)
        self.iot_1.setGeometry(QtCore.QRect(330, 100, 48, 26))
        self.iot_1.setMaximum(999)
        self.iot_1.setObjectName("iot_1")
        self.bt1_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt1_1.setEnabled(True)
        self.bt1_1.setGeometry(QtCore.QRect(270, 100, 48, 26))
        self.bt1_1.setMaximum(999)
        self.bt1_1.setObjectName("bt1_1")
        self.at_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.at_1.setGeometry(QtCore.QRect(200, 100, 48, 26))
        self.at_1.setMaximum(999)
        self.at_1.setObjectName("at_1")
        self.io_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.io_2.setGeometry(QtCore.QRect(460, 150, 92, 23))
        self.io_2.setChecked(False)
        self.io_2.setObjectName("io_2")
        self.bt1_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt1_2.setEnabled(True)
        self.bt1_2.setGeometry(QtCore.QRect(270, 150, 48, 26))
        self.bt1_2.setMaximum(999)
        self.bt1_2.setObjectName("bt1_2")
        self.iot_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.iot_2.setEnabled(False)
        self.iot_2.setGeometry(QtCore.QRect(330, 150, 48, 26))
        self.iot_2.setMaximum(999)
        self.iot_2.setObjectName("iot_2")
        self.bt2_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt2_2.setEnabled(False)
        self.bt2_2.setGeometry(QtCore.QRect(390, 150, 48, 26))
        self.bt2_2.setMaximum(999)
        self.bt2_2.setObjectName("bt2_2")
        self.at_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.at_2.setGeometry(QtCore.QRect(200, 150, 48, 26))
        self.at_2.setMaximum(999)
        self.at_2.setObjectName("at_2")
        self.at_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.at_3.setGeometry(QtCore.QRect(200, 200, 48, 26))
        self.at_3.setMaximum(999)
        self.at_3.setObjectName("at_3")
        self.bt1_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt1_3.setEnabled(True)
        self.bt1_3.setGeometry(QtCore.QRect(270, 200, 48, 26))
        self.bt1_3.setMaximum(999)
        self.bt1_3.setObjectName("bt1_3")
        self.iot_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.iot_3.setEnabled(False)
        self.iot_3.setGeometry(QtCore.QRect(330, 200, 48, 26))
        self.iot_3.setMaximum(999)
        self.iot_3.setObjectName("iot_3")
        self.bt2_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt2_3.setEnabled(False)
        self.bt2_3.setGeometry(QtCore.QRect(390, 200, 48, 26))
        self.bt2_3.setMaximum(999)
        self.bt2_3.setObjectName("bt2_3")
        self.io_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.io_3.setGeometry(QtCore.QRect(460, 200, 92, 23))
        self.io_3.setChecked(False)
        self.io_3.setObjectName("io_3")
        self.io_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.io_5.setEnabled(False)
        self.io_5.setGeometry(QtCore.QRect(460, 300, 92, 23))
        self.io_5.setChecked(False)
        self.io_5.setObjectName("io_5")
        self.at_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.at_4.setGeometry(QtCore.QRect(200, 250, 48, 26))
        self.at_4.setMaximum(999)
        self.at_4.setObjectName("at_4")
        self.iot_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.iot_5.setEnabled(False)
        self.iot_5.setGeometry(QtCore.QRect(330, 300, 48, 26))
        self.iot_5.setMaximum(999)
        self.iot_5.setObjectName("iot_5")
        self.bt2_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt2_5.setEnabled(False)
        self.bt2_5.setGeometry(QtCore.QRect(390, 300, 48, 26))
        self.bt2_5.setMaximum(999)
        self.bt2_5.setObjectName("bt2_5")
        self.bt1_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt1_4.setEnabled(True)
        self.bt1_4.setGeometry(QtCore.QRect(270, 250, 48, 26))
        self.bt1_4.setMaximum(999)
        self.bt1_4.setObjectName("bt1_4")
        self.iot_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.iot_4.setEnabled(False)
        self.iot_4.setGeometry(QtCore.QRect(330, 250, 48, 26))
        self.iot_4.setMaximum(999)
        self.iot_4.setObjectName("iot_4")
        self.bt2_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt2_4.setEnabled(False)
        self.bt2_4.setGeometry(QtCore.QRect(390, 250, 48, 26))
        self.bt2_4.setMaximum(999)
        self.bt2_4.setObjectName("bt2_4")
        self.bt1_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.bt1_5.setEnabled(False)
        self.bt1_5.setGeometry(QtCore.QRect(270, 300, 48, 26))
        self.bt1_5.setMaximum(999)
        self.bt1_5.setObjectName("bt1_5")
        self.io_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.io_4.setGeometry(QtCore.QRect(460, 250, 92, 23))
        self.io_4.setChecked(False)
        self.io_4.setObjectName("io_4")
        self.at_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.at_5.setEnabled(False)
        self.at_5.setGeometry(QtCore.QRect(200, 300, 48, 26))
        self.at_5.setMaximum(999)
        self.at_5.setObjectName("at_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 60, 51, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 60, 51, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 60, 51, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 60, 51, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.prsId1 = QtWidgets.QLineEdit(self.centralwidget)
        self.prsId1.setGeometry(QtCore.QRect(110, 100, 71, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.prsId1.setFont(font)
        self.prsId1.setMaxLength(15)
        self.prsId1.setObjectName("prsId1")
        self.prsId2 = QtWidgets.QLineEdit(self.centralwidget)
        self.prsId2.setGeometry(QtCore.QRect(110, 150, 71, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.prsId2.setFont(font)
        self.prsId2.setMaxLength(15)
        self.prsId2.setObjectName("prsId2")
        self.prsId3 = QtWidgets.QLineEdit(self.centralwidget)
        self.prsId3.setGeometry(QtCore.QRect(110, 200, 71, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.prsId3.setFont(font)
        self.prsId3.setMaxLength(15)
        self.prsId3.setObjectName("prsId3")
        self.prsId4 = QtWidgets.QLineEdit(self.centralwidget)
        self.prsId4.setGeometry(QtCore.QRect(110, 250, 71, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.prsId4.setFont(font)
        self.prsId4.setMaxLength(15)
        self.prsId4.setObjectName("prsId4")
        self.prsId5 = QtWidgets.QLineEdit(self.centralwidget)
        self.prsId5.setEnabled(False)
        self.prsId5.setGeometry(QtCore.QRect(110, 300, 71, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.prsId5.setFont(font)
        self.prsId5.setMaxLength(15)
        self.prsId5.setObjectName("prsId5")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setEnabled(True)
        self.checkBox_1.setGeometry(QtCore.QRect(70, 100, 41, 23))
        self.checkBox_1.setTabletTracking(False)
        self.checkBox_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/red.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.checkBox_1.setIcon(icon)
        self.checkBox_1.setCheckable(True)
        self.checkBox_1.setChecked(True)
        self.checkBox_1.setObjectName("checkBox_1")
        self.spn_b = QtWidgets.QPushButton(self.centralwidget)
        self.spn_b.setGeometry(QtCore.QRect(190, 449, 61, 25))
        self.spn_b.setObjectName("spn_b")
        self.rr_b = QtWidgets.QPushButton(self.centralwidget)
        self.rr_b.setGeometry(QtCore.QRect(270, 449, 61, 25))
        self.rr_b.setObjectName("rr_b")
        self.srt_b = QtWidgets.QPushButton(self.centralwidget)
        self.srt_b.setGeometry(QtCore.QRect(350, 449, 61, 25))
        self.srt_b.setObjectName("srt_b")
        self.all_b = QtWidgets.QPushButton(self.centralwidget)
        self.all_b.setGeometry(QtCore.QRect(230, 489, 61, 25))
        self.all_b.setObjectName("all_b")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 530, 481, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 60, 67, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 150, 41, 23))
        self.checkBox_2.setTabletTracking(False)
        self.checkBox_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_2.setIcon(icon1)
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setEnabled(True)
        self.checkBox_3.setGeometry(QtCore.QRect(70, 200, 41, 23))
        self.checkBox_3.setTabletTracking(False)
        self.checkBox_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_3.setIcon(icon2)
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setGeometry(QtCore.QRect(70, 250, 41, 23))
        self.checkBox_4.setTabletTracking(False)
        self.checkBox_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/yellow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_4.setIcon(icon3)
        self.checkBox_4.setCheckable(True)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setEnabled(True)
        self.checkBox_5.setGeometry(QtCore.QRect(70, 300, 41, 23))
        self.checkBox_5.setTabletTracking(False)
        self.checkBox_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_5.setIcon(icon4)
        self.checkBox_5.setCheckable(True)
        self.checkBox_5.setChecked(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.setData = QtWidgets.QRadioButton(self.centralwidget)
        self.setData.setGeometry(QtCore.QRect(10, 30, 112, 23))
        self.setData.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setData.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setData.setChecked(True)
        self.setData.setObjectName("setData")
        self.LoadData = QtWidgets.QRadioButton(self.centralwidget)
        self.LoadData.setGeometry(QtCore.QRect(10, 350, 141, 23))
        self.LoadData.setObjectName("LoadData")
        self.csvPath = QtWidgets.QLineEdit(self.centralwidget)
        self.csvPath.setEnabled(False)
        self.csvPath.setGeometry(QtCore.QRect(110, 380, 231, 31))
        self.csvPath.setText("")
        self.csvPath.setObjectName("csvPath")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 386, 41, 21))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.fcfs_b.clicked.connect(call_fcfs)
        self.spn_b.clicked.connect(call_spn)
        self.rr_b.clicked.connect(call_rr)
        self.srt_b.clicked.connect(call_srt)
        self.all_b.clicked.connect(call_all)
        self.io_1.toggled['bool'].connect(io_1)
        self.io_2.toggled['bool'].connect(io_2)
        self.io_3.toggled['bool'].connect(io_3)
        self.io_4.toggled['bool'].connect(io_4)
        self.io_5.toggled['bool'].connect(io_5)
        self.checkBox_1.toggled['bool'].connect(active_prs_1)
        self.checkBox_2.toggled['bool'].connect(active_prs_2)
        self.checkBox_3.toggled['bool'].connect(active_prs_3)
        self.checkBox_4.toggled['bool'].connect(active_prs_4)
        self.checkBox_5.toggled['bool'].connect(active_prs_5)
        self.setData.toggled['bool'].connect(set_data)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPU scheduling machine"))
        self.fcfs_b.setText(_translate("MainWindow", "FCFS"))
        self.io_1.setText(_translate("MainWindow", "I/O"))
        self.io_2.setText(_translate("MainWindow", "I/O"))
        self.io_3.setText(_translate("MainWindow", "I/O"))
        self.io_5.setText(_translate("MainWindow", "I/O"))
        self.io_4.setText(_translate("MainWindow", "I/O"))
        self.label.setText(_translate("MainWindow", "Arrival\n"
                                                    "time"))
        self.label_2.setText(_translate("MainWindow", "CPU\n"
                                                      "burst"))
        self.label_3.setText(_translate("MainWindow", "I/O\n"
                                                      "time"))
        self.label_4.setText(_translate("MainWindow", "CPU\n"
                                                      "burst"))
        self.prsId1.setText(_translate("MainWindow", "p_1"))
        self.prsId2.setText(_translate("MainWindow", "p_2"))
        self.prsId3.setText(_translate("MainWindow", "p_3"))
        self.prsId4.setText(_translate("MainWindow", "p_4"))
        self.prsId5.setText(_translate("MainWindow", "p_5"))
        self.spn_b.setText(_translate("MainWindow", "SPN"))
        self.rr_b.setText(_translate("MainWindow", "RR"))
        self.srt_b.setText(_translate("MainWindow", "SRT"))
        self.all_b.setText(_translate("MainWindow", "ALL"))
        self.label_5.setText(_translate("MainWindow", "Process\n"
                                                      "ID"))
        self.setData.setText(_translate("MainWindow", "Set data"))
        self.LoadData.setText(_translate("MainWindow", "Load from csv file"))
        self.label_6.setText(_translate("MainWindow", "Path"))


def make_csv():
    data = 'id_process,arrival time,CPU burst1,I/O time,CPU burst2\n'
    if ui.checkBox_1.isChecked():
        data += f'{ui.prsId1.text()},{ui.at_1.text()},{ui.bt1_1.text()}'
        if ui.io_1.isChecked():
            data += f',{ui.iot_1.text()},{ui.bt2_1.text()}\n'
        else:
            data += ',0,0\n'
    if ui.checkBox_2.isChecked():
        data += f'{ui.prsId2.text()},{ui.at_2.text()},{ui.bt1_2.text()}'
        if ui.io_2.isChecked():
            data += f',{ui.iot_2.text()},{ui.bt2_2.text()}\n'
        else:
            data += ',0,0\n'
    if ui.checkBox_3.isChecked():
        data += f'{ui.prsId3.text()},{ui.at_3.text()},{ui.bt1_3.text()}'
        if ui.io_3.isChecked():
            data += f',{ui.iot_3.text()},{ui.bt2_3.text()}\n'
        else:
            data += ',0,0\n'
    if ui.checkBox_4.isChecked():
        data += f'{ui.prsId4.text()},{ui.at_4.text()},{ui.bt1_4.text()}'
        if ui.io_4.isChecked():
            data += f',{ui.iot_4.text()},{ui.bt2_4.text()}\n'
        else:
            data += ',0,0\n'
    if ui.checkBox_5.isChecked():
        data += f'{ui.prsId5.text()},{ui.at_5.text()},{ui.bt1_5.text()}'
        if ui.io_5.isChecked():
            data += f',{ui.iot_5.text()},{ui.bt2_5.text()}\n'
        else:
            data += ',0,0\n'
    with open('.temp.csv', 'w') as file:
        file.write(data)


def call_fcfs(status):
    pass


def call_spn(status):
    pass


def call_rr(status):
    pass


def call_srt(status):
    pass


def call_all(status):
    make_csv()


def io_1(checked):
    ui.iot_1.setEnabled(checked)
    ui.bt2_1.setEnabled(checked)


def io_2(checked):
    ui.iot_2.setEnabled(checked)
    ui.bt2_2.setEnabled(checked)


def io_3(checked):
    ui.iot_3.setEnabled(checked)
    ui.bt2_3.setEnabled(checked)


def io_4(checked):
    ui.iot_4.setEnabled(checked)
    ui.bt2_4.setEnabled(checked)


def io_5(checked):
    ui.iot_5.setEnabled(checked)
    ui.bt2_5.setEnabled(checked)


def active_prs_1(checked):
    ui.prsId1.setEnabled(checked)
    ui.at_1.setEnabled(checked)
    ui.bt1_1.setEnabled(checked)
    ui.io_1.setEnabled(checked)
    enable = checked and ui.io_1.isChecked()
    ui.iot_1.setEnabled(enable)
    ui.bt2_1.setEnabled(enable)


def active_prs_2(checked):
    ui.prsId2.setEnabled(checked)
    ui.at_2.setEnabled(checked)
    ui.bt1_2.setEnabled(checked)
    ui.io_2.setEnabled(checked)
    enable = checked and ui.io_2.isChecked()
    ui.iot_2.setEnabled(enable)
    ui.bt2_2.setEnabled(enable)


def active_prs_3(checked):
    ui.prsId3.setEnabled(checked)
    ui.at_3.setEnabled(checked)
    ui.bt1_3.setEnabled(checked)
    ui.io_3.setEnabled(checked)
    enable = checked and ui.io_3.isChecked()
    ui.iot_3.setEnabled(enable)
    ui.bt2_3.setEnabled(enable)


def active_prs_4(checked):
    ui.prsId4.setEnabled(checked)
    ui.at_4.setEnabled(checked)
    ui.bt1_4.setEnabled(checked)
    ui.io_4.setEnabled(checked)
    enable = checked and ui.io_4.isChecked()
    ui.iot_4.setEnabled(enable)
    ui.bt2_4.setEnabled(enable)


def active_prs_5(checked):
    ui.prsId5.setEnabled(checked)
    ui.at_5.setEnabled(checked)
    ui.bt1_5.setEnabled(checked)
    ui.io_5.setEnabled(checked)
    enable = checked and ui.io_5.isChecked()
    ui.iot_5.setEnabled(enable)
    ui.bt2_5.setEnabled(enable)


def set_data(checked):
    check_boxes = [ui.checkBox_1, ui.checkBox_2, ui.checkBox_3, ui.checkBox_3, ui.checkBox_4, ui.checkBox_5]
    for cb in check_boxes:
        cb.setEnabled(checked)
    active_prs_1(ui.checkBox_1.isEnabled() and ui.checkBox_1.isChecked())
    active_prs_2(ui.checkBox_2.isEnabled() and ui.checkBox_2.isChecked())
    active_prs_3(ui.checkBox_3.isEnabled() and ui.checkBox_3.isChecked())
    active_prs_4(ui.checkBox_4.isEnabled() and ui.checkBox_4.isChecked())
    active_prs_5(ui.checkBox_5.isEnabled() and ui.checkBox_5.isChecked())
    ui.csvPath.setEnabled(not checked)


if __name__ == "__main__":
    import sys

    sm = machine.Machine()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
