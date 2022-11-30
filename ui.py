# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 275)
        MainWindow.setStyleSheet("font: 10pt \"Microsoft YaHei UI\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileLineEdit = QtWidgets.QLineEdit(self.widget)
        self.fileLineEdit.setObjectName("fileLineEdit")
        self.horizontalLayout_2.addWidget(self.fileLineEdit)
        self.chooseBtn = QtWidgets.QPushButton(self.widget)
        self.chooseBtn.setObjectName("chooseBtn")
        self.horizontalLayout_2.addWidget(self.chooseBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.startSpinBox = QtWidgets.QSpinBox(self.widget)
        self.startSpinBox.setMinimum(1)
        self.startSpinBox.setMaximum(9999)
        self.startSpinBox.setObjectName("startSpinBox")
        self.horizontalLayout.addWidget(self.startSpinBox)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.endSpinBox = QtWidgets.QSpinBox(self.widget)
        self.endSpinBox.setMinimum(0)
        self.endSpinBox.setMaximum(9999)
        self.endSpinBox.setProperty("value", 0)
        self.endSpinBox.setObjectName("endSpinBox")
        self.horizontalLayout.addWidget(self.endSpinBox)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.rotateComboBox = QtWidgets.QComboBox(self.widget)
        self.rotateComboBox.setObjectName("rotateComboBox")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.rotateComboBox.addItem("")
        self.horizontalLayout.addWidget(self.rotateComboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 108, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.startBtn = QtWidgets.QPushButton(self.widget)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_3.addWidget(self.startBtn)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.akLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.akLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.akLineEdit.setObjectName("akLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.akLineEdit)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.skLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.skLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.skLineEdit.setObjectName("skLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.skLineEdit)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.regionLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.regionLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.regionLineEdit.setObjectName("regionLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.regionLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(403, 123, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF 文件转 Excel 表格工具"))
        self.chooseBtn.setText(_translate("MainWindow", "选择文件"))
        self.label_4.setText(_translate("MainWindow", "起始页："))
        self.label_5.setText(_translate("MainWindow", "终止页："))
        self.label_6.setText(_translate("MainWindow", "旋转："))
        self.rotateComboBox.setItemText(0, _translate("MainWindow", "0"))
        self.rotateComboBox.setItemText(1, _translate("MainWindow", "90"))
        self.rotateComboBox.setItemText(2, _translate("MainWindow", "180"))
        self.rotateComboBox.setItemText(3, _translate("MainWindow", "270"))
        self.startBtn.setText(_translate("MainWindow", "开始转换"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "转换"))
        self.label.setText(_translate("MainWindow", "Access Key ID："))
        self.label_2.setText(_translate("MainWindow", "Secret Access Key："))
        self.label_3.setText(_translate("MainWindow", "Region："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "配置"))
