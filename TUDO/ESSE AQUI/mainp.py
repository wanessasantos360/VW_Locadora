from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QComboBox

from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys

from Tela_do_projeto import Ui_TeladoProjeto

class Tela_do_projeto(QDialog):
    def __init__(self,*args,**argvs):
        super(Tela_do_projeto, self).__init__(*args, **argvs)
        self.ui = Ui_TeladoProjeto()
        self.ui.setupUi(self)
        ''' 
        Aqui vai toda programação da telado
        projeto (a que tem foto do carro)
        '''
def salvar():
    print("Salvar")



Tela_do_projeto.acctionSalvar.triggered.connect(salvar())
app = QApplication(sys.argv)
Tela_do_projeto = uic.loadUi("")

if (QDialog.Accepted == True):
    window = Tela_do_projeto()
    window.show()
sys.exit(app.exec_())

