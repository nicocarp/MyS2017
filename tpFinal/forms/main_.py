# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Jun 16 16:38:11 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(531, 442)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 10, 401, 326))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.inputTiempoAtencion1 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.inputTiempoAtencion1.setObjectName(_fromUtf8("inputTiempoAtencion1"))
        self.gridLayout.addWidget(self.inputTiempoAtencion1, 6, 1, 1, 1)
        self.inputCantAnios = QtGui.QLineEdit(self.gridLayoutWidget)
        self.inputCantAnios.setObjectName(_fromUtf8("inputCantAnios"))
        self.gridLayout.addWidget(self.inputCantAnios, 0, 1, 1, 1)
        self.cantDiasAnios = QtGui.QLineEdit(self.gridLayoutWidget)
        self.cantDiasAnios.setObjectName(_fromUtf8("cantDiasAnios"))
        self.gridLayout.addWidget(self.cantDiasAnios, 2, 1, 1, 1)
        self.cantDiasProduccion = QtGui.QLineEdit(self.gridLayoutWidget)
        self.cantDiasProduccion.setObjectName(_fromUtf8("cantDiasProduccion"))
        self.gridLayout.addWidget(self.cantDiasProduccion, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.inputMesesAnio = QtGui.QLineEdit(self.gridLayoutWidget)
        self.inputMesesAnio.setObjectName(_fromUtf8("inputMesesAnio"))
        self.gridLayout.addWidget(self.inputMesesAnio, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.inputCantEmpleados = QtGui.QLineEdit(self.gridLayoutWidget)
        self.inputCantEmpleados.setObjectName(_fromUtf8("inputCantEmpleados"))
        self.gridLayout.addWidget(self.inputCantEmpleados, 5, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.cantHorasDia = QtGui.QLineEdit(self.gridLayoutWidget)
        self.cantHorasDia.setObjectName(_fromUtf8("cantHorasDia"))
        self.gridLayout.addWidget(self.cantHorasDia, 3, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inputTiempoAtencion2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.inputTiempoAtencion2.setObjectName(_fromUtf8("inputTiempoAtencion2"))
        self.gridLayout.addWidget(self.inputTiempoAtencion2, 7, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnDefecto = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnDefecto.setObjectName(_fromUtf8("btnDefecto"))
        self.horizontalLayout.addWidget(self.btnDefecto)
        self.btnIniciarSimulacion = QtGui.QPushButton(self.gridLayoutWidget)
        self.btnIniciarSimulacion.setObjectName(_fromUtf8("btnIniciarSimulacion"))
        self.horizontalLayout.addWidget(self.btnIniciarSimulacion)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_7.setText(_translate("MainWindow", "Tiempo atencion 2", None))
        self.label_2.setText(_translate("MainWindow", "Meses del año", None))
        self.label_5.setText(_translate("MainWindow", "Horas por dia", None))
        self.label_6.setText(_translate("MainWindow", "Tiempo atencion 1", None))
        self.label_4.setText(_translate("MainWindow", "Dias de  produccion", None))
        self.label_3.setText(_translate("MainWindow", "Dias del año", None))
        self.label_9.setText(_translate("MainWindow", "Cantidad Empleados", None))
        self.label.setText(_translate("MainWindow", "Cantidad de años", None))
        self.btnDefecto.setText(_translate("MainWindow", "Defecto", None))
        self.btnIniciarSimulacion.setText(_translate("MainWindow", "Iniciar", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

