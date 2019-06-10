# -*- coding: utf-8 -*-

import sys 
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from crawl import *
from class_crawl import Crawler
from history import *
#from CallHistory import HistoryWindow
import datetime
import sqlite3
import os
import math
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

class MyMainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.display_NewsCrawler_form()
        self.cursor = self.textBrowser_msg.textCursor()
        self.textBrowser_msg.textChanged.connect(self.moveCursor)
        self.showMaximized()

    def display_NewsCrawler_form(self):
        self.setupUi(self)
        self.showMaximized()
        self.actioner_history.triggered.connect(self.display_history_form)
        self.actioner_NewsCrawler.triggered.connect(self.display_NewsCrawler_form)

     
        self.button_start.clicked.connect(self.crawl)
        self.thread = WorkThread() # This is the thread object
        # Connect the signal from the thread to the finished method
        self.thread.update_msg_signal.connect(self.msgUpdate)
        self.thread.finished_singnal.connect(self.finished)
       

    def display_history_form(self):
        self.showMaximized()
        self.history_window = HistoryWindow()
        self.history_window.initUI()
        self.form_widget = self.history_window.centralwidget_history
        self.setCentralWidget(self.form_widget)
    

 
    
       



    def finished(self):
        self.button_start.setEnabled(True)  # Enable the pushButton

    def crawl(self):
        if self.lineEdit_keyword.text() != '':
            self.button_start.setEnabled(False)
            self.thread.start() 
        else:
             QMessageBox.information(self,'注意', "關鍵字不可空白！", QMessageBox.Yes)  

    def moveCursor(self):
        self.textBrowser_msg.moveCursor(self.cursor.End)

    def msgUpdate(self,msg):
         self.textBrowser_msg.append(msg)
    




class WorkThread(QThread):
    #透過類別成員物件定義訊號
    update_msg_signal = pyqtSignal(str)
    finished_singnal = pyqtSignal()
    def run(self):
        keyword = myWin.lineEdit_keyword.text()
        pages   = int(myWin.spinBox_pages.text())
        self.update_msg_signal.emit("===============建立Crawl物件==============" )

        crawler = Crawler(keyword,pages,self)
        #crawler = Crawl(keyword,pages,myWin.textBrowser_msg)
        self.update_msg_signal.emit("===============爬蟲開始===================")
        crawler.crawl()
        self.update_msg_signal.emit("==============共爬取 {} 筆紀錄=============".format(len(crawler.content_list)))

        
        #reply = QMessageBox.information(myWin, "標題", "是否儲存本次爬取結果?", QMessageBox.Yes | QMessageBox.No ,QMessageBox.Yes )  
        #if reply == 16384:
        #reply = self.msg.exec_()

        crawler.content_to_wordcolud2()
        #紀錄在資料庫
        conn = sqlite3.connect(r'D:\user\PyQt5\Crawler\crawler_db.db')
        c = conn.cursor()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO news_record VALUES (?, ?, ?, ?,?)",(now,keyword,pages,len(crawler.content_list),crawler.fig_name));
        conn.commit()
        self.update_msg_signal.emit("===========爬取結果成功儲存在資料庫！=============");
        conn.close()
        self.finished_singnal.emit()
         



class HistoryWindow(QMainWindow, Ui_HistoryWindow):
    def __init__(self):
        super(HistoryWindow, self).__init__()
        self.setupUi(self)

    def initUI(self):
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 900, 50))
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 1525, 780 ))
        self.imglabel.setGeometry(QtCore.QRect(0,0, 800, 750))
        
        #4欄*10列表格
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setShowGrid(True)

        #self.history_window.tableWidget.setFrameShape(QFrame.NoFrame)   ##设置无表格的外框
        self.tableWidget.horizontalHeader().setFixedHeight(50)        #表頭高度
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150) #欄位寬度
        self.tableWidget.horizontalHeader().setSectionsClickable(False) #禁止點表頭
        self.tableWidget.setColumnWidth(0,230);                       #日期欄位
        self.tableWidget.verticalHeader().setDefaultSectionSize(70)
        

        self.tableWidget.setHorizontalHeaderLabels(['日期','關鍵字','頁數','筆數'])
        # 将表格变为禁止编辑  
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格为整行选择
        self.tableWidget.setSelectionBehavior( QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.clicked.connect(self.show_picture)


        self.conn = sqlite3.connect(r'D:\user\PyQt5\Crawler\crawler_db.db')
        c = self.conn.cursor()
        result = c.execute("select count(*) from news_record")
        self.total_page = math.ceil(result.fetchone()[0]/10) #總頁數
        self.now_page = 1 #目前頁數
        self.spinBox_page.setMaximum(self.total_page)
        self.fig_folder_path = "D:\\user\\PyQt5\\Crawler\\news_WordCloud"
        self.pushButton_back.setEnabled(False)
        self.pushButton_back.clicked.connect(self.to_previous_page)
        self.pushButton_next.clicked.connect(self.to_next_page)
        self.pushButton_go.clicked.connect(self.to_any_page)
        self.set_table_content()
        
           
    def set_table_content(self):
        self.label_page.setText(str(self.now_page)+"/100")
        self.updateStatus() #按鈕狀態 (enable/disable)
        c = self.conn.cursor()
        table_content = c.execute("SELECT crawl_date, keyword, pages, records  from news_record  LIMIT 10 OFFSET ?"
                                  ,( (self.now_page-1)*10,))

        for i,row in enumerate(table_content):
            for j,cell in enumerate(row) :
                newItem = QTableWidgetItem(str(cell))
                self.tableWidget.setItem(i,j,newItem) 
      

       

    def to_next_page(self):
        self.now_page += 1
        self.tableWidget.clearContents()
        self.set_table_content()

    def to_previous_page(self):
        self.now_page -= 1
        self.tableWidget.clearContents()
        self.set_table_content()

    def to_any_page(self):
        self.now_page = int(self.spinBox_page.text())
        self.tableWidget.clearContents()
        self.set_table_content()

    def updateStatus(self):
        if self.now_page == self.total_page:
             self.pushButton_next.setEnabled(False)
        else:
            self.pushButton_next.setEnabled(True)

        if self.now_page == 1:
             self.pushButton_back.setEnabled(False)
        else :
            self.pushButton_back.setEnabled(True)

    def show_picture(self):
        row_no = self.tableWidget.currentRow()
        date_item = self.tableWidget.item(row_no,0)
        if date_item == None:
            return
        crawl_date = date_item.text()
        c = self.conn.cursor()
        result = c.execute(" SELECT fig_name FROM news_record WHERE crawl_date = ?", (crawl_date,))
        imgName = result.fetchone()[0]
        fig_path =  self.fig_folder_path+'\\'+imgName
        #判斷照片是否存在
        if os.path.isfile(fig_path):
            img = QtGui.QPixmap(fig_path).scaled(800,750)
            self.imglabel.setPixmap(img)  


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    # setup stylesheet
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())  
    myWin = MyMainWindow()  
    myWin.show() 
    sys.exit(app.exec_())  
