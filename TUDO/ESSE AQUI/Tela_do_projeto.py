from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os
import sys

class Ui_TeladoProjeto(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 600))
        MainWindow.setStyleSheet("background-color: rgb(116, 116, 116);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1081, 581))
        self.frame.setStyleSheet("background-color: rgb(144, 216, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.FotoFundoCarros = QtWidgets.QLabel(self.frame)
        self.FotoFundoCarros.setGeometry(QtCore.QRect(10, 10, 1061, 561))
        self.FotoFundoCarros.setText("")
        self.FotoFundoCarros.setPixmap(QtGui.QPixmap("Ícones do Proj/fotor carro.jpg"))
        self.FotoFundoCarros.setScaledContents(True)
        self.FotoFundoCarros.setAlignment(QtCore.Qt.AlignCenter)
        self.FotoFundoCarros.setObjectName("FotoFundoCarros")
        self.widget_Logo = QtWidgets.QWidget(self.frame)
        self.widget_Logo.setGeometry(QtCore.QRect(340, 20, 391, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_Logo.sizePolicy().hasHeightForWidth())
        self.widget_Logo.setSizePolicy(sizePolicy)
        self.widget_Logo.setMinimumSize(QtCore.QSize(391, 81))
        self.widget_Logo.setMaximumSize(QtCore.QSize(391, 81))
        self.widget_Logo.setMouseTracking(True)
        self.widget_Logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_Logo.setAutoFillBackground(False)
        self.widget_Logo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_Logo.setObjectName("widget_Logo")
        self.label_logoTOPO = QtWidgets.QLabel(self.widget_Logo)
        self.label_logoTOPO.setEnabled(True)
        self.label_logoTOPO.setGeometry(QtCore.QRect(0, 10, 381, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logoTOPO.sizePolicy().hasHeightForWidth())
        self.label_logoTOPO.setSizePolicy(sizePolicy)
        self.label_logoTOPO.setMinimumSize(QtCore.QSize(381, 71))
        self.label_logoTOPO.setMaximumSize(QtCore.QSize(381, 71))
        self.label_logoTOPO.setMouseTracking(True)
        self.label_logoTOPO.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_logoTOPO.setText("")
        self.label_logoTOPO.setPixmap(QtGui.QPixmap("Ícones do Proj/LOGO VW Locadora - Carros .png"))
        self.label_logoTOPO.setScaledContents(True)
        self.label_logoTOPO.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logoTOPO.setObjectName("label_logoTOPO")
        self.tituloveiculo = QtWidgets.QLabel(self.frame)
        self.tituloveiculo.setGeometry(QtCore.QRect(90, 90, 141, 41))
        self.tituloveiculo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.tituloveiculo.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloveiculo.setObjectName("tituloveiculo")
        self.subtituloveiculo = QtWidgets.QLabel(self.frame)
        self.subtituloveiculo.setGeometry(QtCore.QRect(30, 150, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.subtituloveiculo.setFont(font)
        self.subtituloveiculo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtituloveiculo.setAlignment(QtCore.Qt.AlignCenter)
        self.subtituloveiculo.setObjectName("subtituloveiculo")
        self.ListaCarros = QtWidgets.QComboBox(self.frame)
        self.ListaCarros.setGeometry(QtCore.QRect(120, 150, 211, 22))
        self.ListaCarros.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"background-color: rgb(189, 189, 189);")
        self.ListaCarros.setObjectName("ListaCarros")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.ListaCarros.addItem("")
        self.BotaoVersaoSimples = QtWidgets.QRadioButton(self.frame)
        self.BotaoVersaoSimples.setGeometry(QtCore.QRect(30, 180, 111, 51))
        self.BotaoVersaoSimples.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BotaoVersaoSimples.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.BotaoVersaoSimples.setObjectName("BotaoVersaoSimples")
        self.BotaoVersaoCompleto = QtWidgets.QRadioButton(self.frame)
        self.BotaoVersaoCompleto.setGeometry(QtCore.QRect(150, 180, 131, 51))
        self.BotaoVersaoCompleto.setStyleSheet("font: 10pt \"Comic Sans MS\";")
        self.BotaoVersaoCompleto.setObjectName("BotaoVersaoCompleto")
        self.subtituloacessorios = QtWidgets.QLabel(self.frame)
        self.subtituloacessorios.setGeometry(QtCore.QRect(100, 240, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.subtituloacessorios.setFont(font)
        self.subtituloacessorios.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.subtituloacessorios.setAlignment(QtCore.Qt.AlignCenter)
        self.subtituloacessorios.setObjectName("subtituloacessorios")
        self.checkBox_suporte2bike = QtWidgets.QCheckBox(self.frame)
        self.checkBox_suporte2bike.setGeometry(QtCore.QRect(30, 290, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.checkBox_suporte2bike.setFont(font)
        self.checkBox_suporte2bike.setObjectName("checkBox_suporte2bike")
        self.checkBox_Bagageiro = QtWidgets.QCheckBox(self.frame)
        self.checkBox_Bagageiro.setGeometry(QtCore.QRect(30, 320, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.checkBox_Bagageiro.setFont(font)
        self.checkBox_Bagageiro.setObjectName("checkBox_Bagageiro")
        self.checkBox_SuporteGuincho = QtWidgets.QCheckBox(self.frame)
        self.checkBox_SuporteGuincho.setGeometry(QtCore.QRect(30, 350, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.checkBox_SuporteGuincho.setFont(font)
        self.checkBox_SuporteGuincho.setObjectName("checkBox_SuporteGuincho")
        self.checkBox_Multimidia = QtWidgets.QCheckBox(self.frame)
        self.checkBox_Multimidia.setGeometry(QtCore.QRect(30, 380, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.checkBox_Multimidia.setFont(font)
        self.checkBox_Multimidia.setObjectName("checkBox_Multimidia")
        self.checkBox_Carretinha = QtWidgets.QCheckBox(self.frame)
        self.checkBox_Carretinha.setGeometry(QtCore.QRect(30, 410, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.checkBox_Carretinha.setFont(font)
        self.checkBox_Carretinha.setStyleSheet("background-color: rgb(144, 216, 255);")
        self.checkBox_Carretinha.setObjectName("checkBox_Carretinha")
        self.dateEdit_DataRetirada = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_DataRetirada.setGeometry(QtCore.QRect(150, 451, 121, 31))
        self.dateEdit_DataRetirada.setStyleSheet("font: 11pt \"Comic Sans MS\";\n"
"background-color: rgb(189, 189, 189);")
        self.dateEdit_DataRetirada.setObjectName("dateEdit_DataRetirada")
        self.label_DatadeRetirada = QtWidgets.QLabel(self.frame)
        self.label_DatadeRetirada.setGeometry(QtCore.QRect(56, 440, 81, 51))
        self.label_DatadeRetirada.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"background-color: rgb(250, 250, 250);")
        self.label_DatadeRetirada.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DatadeRetirada.setObjectName("label_DatadeRetirada")
        self.label_DatadeDevolucao = QtWidgets.QLabel(self.frame)
        self.label_DatadeDevolucao.setGeometry(QtCore.QRect(50, 500, 91, 51))
        self.label_DatadeDevolucao.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"background-color: rgb(250, 250, 250);")
        self.label_DatadeDevolucao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DatadeDevolucao.setObjectName("label_DatadeDevolucao")
        self.dateEdit_DataDevolucao = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_DataDevolucao.setGeometry(QtCore.QRect(150, 510, 121, 31))
        self.dateEdit_DataDevolucao.setStyleSheet("font: 11pt \"Comic Sans MS\";\n"
"background-color: rgb(189, 189, 189);")
        self.dateEdit_DataDevolucao.setObjectName("dateEdit_DataDevolucao")
        self.tituloSeusDados = QtWidgets.QLabel(self.frame)
        self.tituloSeusDados.setGeometry(QtCore.QRect(560, 150, 181, 31))
        self.tituloSeusDados.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.tituloSeusDados.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloSeusDados.setObjectName("tituloSeusDados")
        self.lineEdit_NomeCompleto = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_NomeCompleto.setGeometry(QtCore.QRect(540, 210, 451, 21))
        self.lineEdit_NomeCompleto.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_NomeCompleto.setObjectName("lineEdit_NomeCompleto")
        self.subtitulo_NomeCompleto = QtWidgets.QLabel(self.frame)
        self.subtitulo_NomeCompleto.setGeometry(QtCore.QRect(410, 210, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.subtitulo_NomeCompleto.setFont(font)
        self.subtitulo_NomeCompleto.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtitulo_NomeCompleto.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo_NomeCompleto.setObjectName("subtitulo_NomeCompleto")
        self.subtitulo_Celular = QtWidgets.QLabel(self.frame)
        self.subtitulo_Celular.setGeometry(QtCore.QRect(410, 290, 61, 16))
        self.subtitulo_Celular.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtitulo_Celular.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo_Celular.setObjectName("subtitulo_Celular")
        self.subtitulo_CPF = QtWidgets.QLabel(self.frame)
        self.subtitulo_CPF.setGeometry(QtCore.QRect(640, 290, 47, 20))
        self.subtitulo_CPF.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtitulo_CPF.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo_CPF.setObjectName("subtitulo_CPF")
        self.subtitulo_Renach = QtWidgets.QLabel(self.frame)
        self.subtitulo_Renach.setGeometry(QtCore.QRect(410, 330, 61, 21))
        self.subtitulo_Renach.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtitulo_Renach.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo_Renach.setObjectName("subtitulo_Renach")
        self.subtitulo_Pontuacao = QtWidgets.QLabel(self.frame)
        self.subtitulo_Pontuacao.setGeometry(QtCore.QRect(850, 290, 121, 21))
        self.subtitulo_Pontuacao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtitulo_Pontuacao.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo_Pontuacao.setObjectName("subtitulo_Pontuacao")
        self.subtitulo_Endereco = QtWidgets.QLabel(self.frame)
        self.subtitulo_Endereco.setGeometry(QtCore.QRect(410, 370, 81, 21))
        self.subtitulo_Endereco.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtitulo_Endereco.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo_Endereco.setObjectName("subtitulo_Endereco")
        self.lineEdit_Celular = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Celular.setGeometry(QtCore.QRect(480, 290, 141, 20))
        self.lineEdit_Celular.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Celular.setObjectName("lineEdit_Celular")
        self.lineEdit_CPF = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_CPF.setGeometry(QtCore.QRect(700, 290, 131, 20))
        self.lineEdit_CPF.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_CPF.setObjectName("lineEdit_CPF")
        self.lineEdit_Renach = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Renach.setGeometry(QtCore.QRect(480, 330, 131, 20))
        self.lineEdit_Renach.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Renach.setObjectName("lineEdit_Renach")
        self.lineEdit_Endereco = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Endereco.setGeometry(QtCore.QRect(500, 370, 521, 20))
        self.lineEdit_Endereco.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Endereco.setObjectName("lineEdit_Endereco")
        self.selec_Pontuacao = QtWidgets.QSpinBox(self.frame)
        self.selec_Pontuacao.setGeometry(QtCore.QRect(980, 290, 42, 22))
        self.selec_Pontuacao.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.selec_Pontuacao.setMaximum(20)
        self.selec_Pontuacao.setSingleStep(1)
        self.selec_Pontuacao.setObjectName("selec_Pontuacao")

        self.pushButton_EnviarDados.setGeometry(QtCore.QRect(490, 460, 101, 31))
        self.pushButton_EnviarDados.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_EnviarDados.setObjectName("pushButton_EnviarDados")
        self.pushButton_LimparDados = QtWidgets.QPushButton(self.frame)
        self.pushButton_LimparDados.setGeometry(QtCore.QRect(630, 460, 101, 31))
        self.pushButton_LimparDados.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_LimparDados.setObjectName("pushButton_LimparDados")
        self.subtitulo_CEP = QtWidgets.QLabel(self.frame)
        self.subtitulo_CEP.setGeometry(QtCore.QRect(410, 410, 81, 21))
        self.subtitulo_CEP.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtitulo_CEP.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo_CEP.setObjectName("subtitulo_CEP")
        self.lineEdit_CEP = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_CEP.setGeometry(QtCore.QRect(500, 410, 101, 20))
        self.lineEdit_CEP.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_CEP.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_CEP.setObjectName("lineEdit_CEP")
        self.subtitulo_email = QtWidgets.QLabel(self.frame)
        self.subtitulo_email.setGeometry(QtCore.QRect(410, 250, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.subtitulo_email.setFont(font)
        self.subtitulo_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.subtitulo_email.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitulo_email.setObjectName("subtitulo_email")
        self.lineEdit_email = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_email.setGeometry(QtCore.QRect(540, 250, 451, 21))
        self.lineEdit_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Comic Sans MS\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VW Locadora"))
        self.tituloveiculo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Veículo e Locação</p></body></html>"))
        self.subtituloveiculo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Veículo:</p></body></html>"))
        self.ListaCarros.setItemText(0, _translate("MainWindow", "Selecione (carro/modelo)"))
        self.ListaCarros.setItemText(1, _translate("MainWindow", "Fiat Mobi Easy"))
        self.ListaCarros.setItemText(2, _translate("MainWindow", "Reanult Kwid Life"))
        self.ListaCarros.setItemText(3, _translate("MainWindow", "Fiat Uno"))
        self.ListaCarros.setItemText(4, _translate("MainWindow", "Chevrolet Onix"))
        self.ListaCarros.setItemText(5, _translate("MainWindow", "Volkswagen Gol Trend"))
        self.ListaCarros.setItemText(6, _translate("MainWindow", "Hyundai HB20"))
        self.ListaCarros.setItemText(7, _translate("MainWindow", "Ford Ka"))
        self.ListaCarros.setItemText(8, _translate("MainWindow", "Toyota Etios"))
        self.ListaCarros.setItemText(9, _translate("MainWindow", "Nissan March"))
        self.BotaoVersaoSimples.setText(_translate("MainWindow", "Versão Simples\n"
"Lite\n"
"Joy"))
        self.BotaoVersaoCompleto.setText(_translate("MainWindow", "Versão Completa\n"
"ar/vidros e travas\n"
"elétricas/ABS"))
        self.subtituloacessorios.setText(_translate("MainWindow", "Acessórios"))
        self.checkBox_suporte2bike.setText(_translate("MainWindow", "Suporte para 2 Bike   (R$ 35,00)"))
        self.checkBox_Bagageiro.setText(_translate("MainWindow", "Bagageiro Baú para teto   (R$ 20,00)"))
        self.checkBox_SuporteGuincho.setText(_translate("MainWindow", "Suporte para Guincho   (R$ 10,00)"))
        self.checkBox_Multimidia.setText(_translate("MainWindow", "Central Multimídia   (R$ 12,00)"))
        self.checkBox_Carretinha.setText(_translate("MainWindow", "Carretinha para carga   (R$ 15,00)"))
        self.label_DatadeRetirada.setText(_translate("MainWindow", "Data de\n"
"Retirada"))
        self.label_DatadeDevolucao.setText(_translate("MainWindow", "Data de\n"
"Devolução"))
        self.tituloSeusDados.setText(_translate("MainWindow", "Seus Dados"))
        self.lineEdit_NomeCompleto.setPlaceholderText(_translate("MainWindow", "Insira seu nome completo"))
        self.subtitulo_NomeCompleto.setText(_translate("MainWindow", "Nome Completo:"))
        self.subtitulo_Celular.setText(_translate("MainWindow", "Celular:"))
        self.subtitulo_CPF.setText(_translate("MainWindow", "CPF:"))
        self.subtitulo_Renach.setText(_translate("MainWindow", "Renach:"))
        self.subtitulo_Pontuacao.setText(_translate("MainWindow", "Pontuação CNH:"))
        self.subtitulo_Endereco.setText(_translate("MainWindow", "Endereço:"))
        self.lineEdit_Celular.setPlaceholderText(_translate("MainWindow", "(99)9 9999-9999"))
        self.lineEdit_CPF.setPlaceholderText(_translate("MainWindow", "***.***.***-**"))
        self.lineEdit_Endereco.setPlaceholderText(_translate("MainWindow", "Logradouro, número, bairro - cidade/UF"))
        self.pushButton_EnviarDados.setText(_translate("MainWindow", "Enviar"))
        self.pushButton_LimparDados.setText(_translate("MainWindow", "Limpar"))
        self.subtitulo_CEP.setText(_translate("MainWindow", "CEP"))
        self.lineEdit_CEP.setPlaceholderText(_translate("MainWindow", "00000-000"))
        self.subtitulo_email.setText(_translate("MainWindow", "E-mail:"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "Insira seu nome completo"))
import imgprojeto


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TeladoProjeto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
