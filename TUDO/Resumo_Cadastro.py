from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os
import sys



class Ui_ResumoCadastro(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 9, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"border-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 221, 21))
        self.label_2.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.tabela_resumo = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela_resumo.setGeometry(QtCore.QRect(10, 60, 631, 311))
        self.tabela_resumo.setObjectName("tabela_resumo")
        self.tabela_resumo.setColumnCount(3)
        self.tabela_resumo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_resumo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_resumo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_resumo.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resumo do Cadastro"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Resumo da VW Locadora</span></p></body></html>"))
        item = self.tabela_resumo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tabela_resumo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Veículo Modelo"))
        item = self.tabela_resumo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Devolução"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ResumoCadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
