from PyQt5.QtWidgets import QApplication
from PyQt5.QWidgets import QWidget
from PyQt5.QWidgets import QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os
import sys










app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = TeladoProjeto()
    window.show()
sys.exit(app.exec())