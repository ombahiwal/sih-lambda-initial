# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabeldummy.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(length,breadth)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, length-70, breadth-90))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScrollMargin(10)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setObjectName("tableWidget")
        item = self.tableWidget.setRowCount(rowlen)
#        item = QtWidgets.QTableWidgetItem()
#        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
#       self.tableWidget.setHorizontalHeaderItem(1, item)
#
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, length, 40))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 192, 244, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        for i in range(columnlen):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", list1[0][i]))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(rowlen-1):
            for j in range(columnlen):
                item = self.tableWidget.item(i, j)
                item.setText(_translate("MainWindow", list1[i+1][j]))
        self.label.setText(_translate("MainWindow", "Genysis Network Analysis Tool"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    rect = screen.availableGeometry()
    length = size.width()
    breadth = size.height()
    list1=[["Sr no","IP Address","Foriegn IP","Country"],[1,4654654,"gsgesrgdfgfd","ewraf5a4ewf6"],[2,894654654,"fsadfsdfadsf","dfasd6f465ds"]]
    rowlen=len(list1)-1
    columnlen=len(list1[0])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
