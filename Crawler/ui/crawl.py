# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crawl.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1050, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1050, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1050, 800))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tabCrawler = QtWidgets.QWidget()
        self.tabCrawler.setObjectName("tabCrawler")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabCrawler)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 961, 691))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setLineWidth(0)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setIndent(0)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.lineEdit_keyword.setFont(font)
        self.lineEdit_keyword.setText("")
        self.lineEdit_keyword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.verticalLayout_3.addWidget(self.lineEdit_keyword)
        self.spinBox_pages = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_pages.sizePolicy().hasHeightForWidth())
        self.spinBox_pages.setSizePolicy(sizePolicy)
        self.spinBox_pages.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.spinBox_pages.setFont(font)
        self.spinBox_pages.setMinimum(1)
        self.spinBox_pages.setMaximum(50)
        self.spinBox_pages.setObjectName("spinBox_pages")
        self.verticalLayout_3.addWidget(self.spinBox_pages)
        self.button_start = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.button_start.setFont(font)
        self.button_start.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_start.setObjectName("button_start")
        self.verticalLayout_3.addWidget(self.button_start)
        self.textBrowser_msg = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.textBrowser_msg.setFont(font)
        self.textBrowser_msg.setObjectName("textBrowser_msg")
        self.verticalLayout_3.addWidget(self.textBrowser_msg)
        self.tabWidget.addTab(self.tabCrawler, "")
        self.tabHistory = QtWidgets.QWidget()
        self.tabHistory.setObjectName("tabHistory")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabHistory)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 961, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_back = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(14)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.label_page = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_page.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_page.setFont(font)
        self.label_page.setScaledContents(True)
        self.label_page.setAlignment(QtCore.Qt.AlignCenter)
        self.label_page.setIndent(0)
        self.label_page.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_page.setObjectName("label_page")
        self.horizontalLayout.addWidget(self.label_page)
        self.pushButton_next = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.spinBox_page = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.spinBox_page.setFont(font)
        self.spinBox_page.setMinimum(1)
        self.spinBox_page.setProperty("value", 1)
        self.spinBox_page.setObjectName("spinBox_page")
        self.horizontalLayout.addWidget(self.spinBox_page)
        self.pushButton_go = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.pushButton_go.setFont(font)
        self.pushButton_go.setObjectName("pushButton_go")
        self.horizontalLayout.addWidget(self.pushButton_go)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.imglabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imglabel.sizePolicy().hasHeightForWidth())
        self.imglabel.setSizePolicy(sizePolicy)
        self.imglabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.imglabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.imglabel.setLineWidth(0)
        self.imglabel.setText("")
        self.imglabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.imglabel.setObjectName("imglabel")
        self.horizontalLayout_2.addWidget(self.imglabel)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tabHistory, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>新            聞          爬          蟲</p></body></html>"))
        self.lineEdit_keyword.setPlaceholderText(_translate("MainWindow", "輸入關鍵字"))
        self.spinBox_pages.setSuffix(_translate("MainWindow", "筆"))
        self.button_start.setText(_translate("MainWindow", "開始"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCrawler), _translate("MainWindow", "爬蟲"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>歷史紀錄</p></body></html>"))
        self.pushButton_back.setText(_translate("MainWindow", "前一頁"))
        self.label_page.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">1/100</span></p></body></html>"))
        self.pushButton_next.setText(_translate("MainWindow", "後一頁"))
        self.pushButton_go.setText(_translate("MainWindow", "頁面跳轉"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHistory), _translate("MainWindow", "歷史紀錄"))
