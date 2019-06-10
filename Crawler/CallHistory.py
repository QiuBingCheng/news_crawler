# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from history import *
from PIL import Image

class HistoryWindow(QMainWindow, Ui_HistoryWindow):
    def __init__(self):
        super(HistoryWindow, self).__init__()
        self.setupUi(self)

    def show_picture(self):
        QMessageBox.about(self, "Title", str(self.tableWidget.currentRow()))
        img = QtGui.QPixmap('me.jpg').scaled(history_window.imglabel.width(),self.imglabel.height())
        self.imglabel.setPixmap(img)
      





  
   
   
