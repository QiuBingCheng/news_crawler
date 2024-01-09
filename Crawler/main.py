# -*- coding: utf-8 -*-

import configparser
import sys
import qdarkstyle
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QAbstractItemView, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from ui.crawl import Ui_MainWindow
from lib.crawler import Crawler
from lib.word_func import process_to_image, process_to_word
from lib import db_func
import datetime
import sqlite3
import os
import math

config = configparser.ConfigParser()
config.read('config.ini')


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        # setup basic ui layout
        self.setupUi(self)

        # set up crawl tab
        self.set_up_crawl_fun()

        # set up the history tab
        self.set_up_history_fun()
        self.set_up_history_table_ui()
        self.set_up_history_table_content()

        # trigger binding
        self.tabWidget.currentChanged.connect(self.refresh_records)

    def refresh_records(self, index):
        if index == 0:
            return

        self.set_up_history_table_content()

    def set_up_crawl_fun(self):
        self.cursor = self.textBrowser_msg.textCursor()
        self.textBrowser_msg.textChanged.connect(self.moveCursor)
        self.button_start.clicked.connect(self.crawl)

        # set workthread
        self.thread = WorkThread()
        self.thread.update_msg_signal.connect(self.msgUpdate)
        self.thread.finished_singnal.connect(self.finished)

    def finished(self):
        self.button_start.setEnabled(True)  # Enable the pushButton

    def crawl(self):
        if self.lineEdit_keyword.text() == '':
            QMessageBox.information(self, '注意', "關鍵字不可空白！", QMessageBox.Yes)

        self.button_start.setEnabled(False)
        self.thread.start()

    def moveCursor(self):
        self.textBrowser_msg.moveCursor(self.cursor.End)

    def msgUpdate(self, msg):
        self.textBrowser_msg.append(msg)

    def set_up_history_table_content(self):

        # set up table content
        table_content = db_func.select_records(
            limit=10, offset=(self.current_page-1)*10)

        for i, row in enumerate(table_content):
            for j, cell in enumerate(row):
                newItem = QTableWidgetItem(str(cell))
                self.tableWidget.setItem(i, j, newItem)

        self.imglabel_size = (self.imglabel.width(), self.imglabel.height())

    def set_up_history_table_ui(self):

        # set up table UI
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setShowGrid(True)

        self.tableWidget.horizontalHeader().setFixedHeight(45)  # 表頭高度
        self.tableWidget.horizontalHeader().setDefaultSectionSize(60)  # 欄位寬度
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionsClickable(False)
        self.tableWidget.setColumnWidth(0, 210)  # 日期欄位
        self.tableWidget.setColumnWidth(1, 80)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)

        self.tableWidget.setHorizontalHeaderLabels(['日期', '關鍵字', '筆數'])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setVisible(False)

        vertical_header_font = QtGui.QFont()
        vertical_header_font.setPointSize(12)  # Adjust the font size as needed
        self.tableWidget.verticalHeader().setFont(vertical_header_font)

        # trigger event
        self.tableWidget.clicked.connect(self.show_picture)

    def set_up_history_fun(self):
        # init image
        self.img_folder = config["result"]["image"]

        # set
        count = db_func.total_count()
        self.total_page = math.ceil(count/10)  # 總頁數
        self.current_page = 1
        self.spinBox_page.setMaximum(self.total_page)

        self.updateStatus()

        # trigger event
        self.pushButton_back.clicked.connect(self.to_previous_page)
        self.pushButton_next.clicked.connect(self.to_next_page)
        self.pushButton_go.clicked.connect(self.to_any_page)

    def show_picture(self):
        row_no = self.tableWidget.currentRow()
        date_item = self.tableWidget.item(row_no, 0)
        if date_item is None:
            return

        crawl_date = date_item.text()
        filename = db_func.select_filename(crawl_date)
        fig_path = f"{self.img_folder}\\{filename}.png"

        if os.path.isfile(fig_path):
            img = QtGui.QPixmap(fig_path).scaled(*self.imglabel_size)
            self.imglabel.setPixmap(img)

    def to_next_page(self):
        self.current_page += 1
        self.tableWidget.clearContents()
        self.set_up_history_table_content()

    def to_previous_page(self):
        self.current_page -= 1
        self.tableWidget.clearContents()
        self.set_up_history_table_content()

    def to_any_page(self):
        self.current_page = int(self.spinBox_page.text())
        self.tableWidget.clearContents()
        self.set_up_history_table_content()

    def updateStatus(self):
        # udpate page number label and button status

        self.label_page.setText(str(self.current_page)+"/100")

        if self.current_page == 1:
            self.pushButton_back.setEnabled(False)
        else:
            self.pushButton_back.setEnabled(True)

        if self.current_page < self.total_page:
            self.pushButton_back.setEnabled(True)
        else:
            self.pushButton_next.setEnabled(False)


class WorkThread(QThread):
    update_msg_signal = pyqtSignal(str)
    finished_singnal = pyqtSignal()

    def run(self):
        keyword = myWin.lineEdit_keyword.text()
        nums = int(myWin.spinBox_pages.value())
        self.update_msg_signal.emit("=============== 建立Crawl物件 ==============")

        crawler = Crawler(keyword, nums, self.update_msg_signal.emit)
        self.update_msg_signal.emit("=============== 爬蟲開始 ===================")
        news_infos = crawler.crawl()
        self.update_msg_signal.emit(
            f"============== 共爬取 {len(news_infos)} 筆紀錄=============")

        now = datetime.datetime.now()
        filename = f"{now.strftime('%Y%m%d_%H%M%S')}_{keyword}"

        try:
            process_to_image(news_infos, filename)
            self.update_msg_signal.emit(
                f"============== 成功儲存文字雲 {filename}.png ...=============")

            db_func.insert_one_record(now.strftime("%Y-%m-%d %H:%M:%S"),
                                      keyword, len(news_infos), filename)
            self.update_msg_signal.emit(
                "=========== 爬取結果成功儲存在資料庫！============")

        except Exception as e:
            print(news_infos)
            self.update_msg_signal.emit(str(e))

        finally:
            self.finished_singnal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
