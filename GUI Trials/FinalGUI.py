# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinalGUI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import con_map
import con_graph
import rkhunter_scan


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #main window resized
        MainWindow.resize(length,breadth)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Abyssinica SIL")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon.fromTheme("Genysis")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0,30,length,breadth))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(7, 1, 44);\n"
"font: 88 11pt \"Ubuntu\";")
        self.tabWidget.setObjectName("tabWidget")
        self.Basic_View = QtWidgets.QWidget()
        self.Basic_View.setObjectName("Basic_View")
        self.Basic_View_Table = QtWidgets.QTableWidget(self.Basic_View)
        self.Basic_View_Table.setGeometry(QtCore.QRect(0, 0, length-66, breadth-150))
        self.Basic_View_Table.setAutoFillBackground(True)
        self.Basic_View_Table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Basic_View_Table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Basic_View_Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Basic_View_Table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Basic_View_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Basic_View_Table.setAlternatingRowColors(True)
        self.Basic_View_Table.setRowCount(0)
        self.Basic_View_Table.setColumnCount(0)
        self.Basic_View_Table.setObjectName("Basic_View_Table")
        self.Basic_View_Table.horizontalHeader().setDefaultSectionSize(190)
        self.Basic_View_Table.horizontalHeader().setMinimumSectionSize(120)
        self.Basic_View_Table.horizontalHeader().setStretchLastSection(True)
        self.Basic_Reload_List = QtWidgets.QPushButton(self.Basic_View)
        self.Basic_Reload_List.setGeometry(QtCore.QRect((length-66)/2-400,breadth-145,120,25))
        self.Basic_Reload_List.setObjectName("Basic_Reload_List")
        self.Basic_Network_Graph = QtWidgets.QPushButton(self.Basic_View)
        self.Basic_Network_Graph.setGeometry(QtCore.QRect( (length-66)/2+200, breadth-145,120,25))
        self.Basic_Network_Graph.setObjectName("Basic_Network_Graph")
        self.Basic_Network_Graph.clicked.connect(con_graph.map)

        self.Basic_Connection_Map = QtWidgets.QPushButton(self.Basic_View)
        self.Basic_Connection_Map.setGeometry(QtCore.QRect( (length-66)/2-100, breadth-145,120,25))
        self.Basic_Connection_Map.setObjectName("Basic_Connection_Map")
        self.Basic_Connection_Map.clicked.connect(con_map.calling)


        self.tabWidget.addTab(self.Basic_View, "")
        self.Detailed_View = QtWidgets.QWidget()
        self.Detailed_View.setObjectName("Detailed_View")
        self.Detaile_view_list = QtWidgets.QTableWidget(self.Detailed_View)
        self.Detaile_view_list.setGeometry(QtCore.QRect(0, 0, length-66, breadth-150))
        self.Detaile_view_list.setAutoFillBackground(True)
        self.Detaile_view_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Detaile_view_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Detaile_view_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Detaile_view_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Detaile_view_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Detaile_view_list.setAlternatingRowColors(True)
        self.Detaile_view_list.setRowCount(0)
        self.Detaile_view_list.setColumnCount(0)
        self.Detaile_view_list.setObjectName("Detaile_view_list")
        self.Detaile_view_list.horizontalHeader().setDefaultSectionSize(190)
        self.Detaile_view_list.horizontalHeader().setMinimumSectionSize(120)
        self.Detaile_view_list.horizontalHeader().setStretchLastSection(True)
        self.Detail_Network_Graph = QtWidgets.QPushButton(self.Detailed_View)
        self.Detail_Network_Graph.setGeometry(QtCore.QRect((length-66)/2+200, breadth-145,120,25))
        self.Detail_Network_Graph.setObjectName("Detail_Network_Graph")
        self.Detail_Network_Graph.clicked.connect(con_graph.map)
        self.Detail_Reload_List = QtWidgets.QPushButton(self.Detailed_View)
        self.Detail_Reload_List.setGeometry(QtCore.QRect((length-66)/2-400,breadth-145,120,25))
        self.Detail_Reload_List.setObjectName("Detail_Reload_List")
        self.Detail_Connection_Map = QtWidgets.QPushButton(self.Detailed_View)
        self.Detail_Connection_Map.setGeometry(QtCore.QRect((length-66)/2-100, breadth-145,120,25))
        self.Detail_Connection_Map.setObjectName("Detail_Connection_Map")
        self.Detail_Connection_Map.clicked.connect(con_map.calling)
        self.tabWidget.addTab(self.Detailed_View, "")
        self.System_Scan = QtWidgets.QWidget()
        self.System_Scan.setObjectName("System_Scan")
        self.Start_Scan = QtWidgets.QPushButton(self.System_Scan)
        self.Start_Scan.setGeometry(QtCore.QRect(350,breadth - 145, 120, 25 ))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)

        self.System_scan_list = QtWidgets.QTableWidget(self.System_Scan)
        self.System_scan_list.setGeometry(QtCore.QRect(0, 0, length-66, breadth-150))
        self.System_scan_list.setAutoFillBackground(True)
        self.System_scan_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.System_scan_list.setFrameShadow(QtWidgets.QFrame.Plain)
        self.System_scan_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.System_scan_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.System_scan_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.System_scan_list.setAlternatingRowColors(True)
        self.System_scan_list.setRowCount(0)
        self.System_scan_list.setColumnCount(0)
        self.System_scan_list.setObjectName("System_scan_list")
        self.System_scan_list.horizontalHeader().setDefaultSectionSize(190)
        self.System_scan_list.horizontalHeader().setMinimumSectionSize(120)
        self.System_scan_list.horizontalHeader().setStretchLastSection(True)
        self.Start_Scan.setFont(font)
        self.Start_Scan.setObjectName("Start_Scan")
        self.Stop_Scan = QtWidgets.QPushButton(self.System_Scan)
        self.Stop_Scan.setGeometry(QtCore.QRect(900-50, breadth - 145, 120, 25))
        self.Stop_Scan.setObjectName("Stop_Scan")
        '''self.pushButton = QtWidgets.QPushButton(self.System_Scan)
        self.pushButton.setGeometry(QtCore.QRect(650,breadth-145, 120, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.System_Scan)
        self.pushButton_2.setGeometry(QtCore.QRect(900, breadth - 145, 120, 25))
        self.pushButton_2.setObjectName("pushButton_2")'''

        self.tabWidget.addTab(self.System_Scan, "")


        self.Classification = QtWidgets.QWidget()
        self.Classification.setObjectName("Classification")
        self.Blacklist = QtWidgets.QTableWidget(self.Classification)
        self.Blacklist.setGeometry(QtCore.QRect(20,50,(length-106)/2-30,breadth-250))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.Blacklist.setFont(font)
        self.Blacklist.setAutoFillBackground(True)
        self.Blacklist.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.Blacklist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Blacklist.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Blacklist.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Blacklist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Blacklist.setProperty("showDropIndicator", False)
        self.Blacklist.setAlternatingRowColors(False)
        self.Blacklist.setObjectName("Blacklist")
        self.Blacklist.setColumnCount(2)
        self.Blacklist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Blacklist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Blacklist.setHorizontalHeaderItem(1, item)
        self.Blacklist.horizontalHeader().setMinimumSectionSize(200)
        self.Blacklist.horizontalHeader().setStretchLastSection(True)
        self.Blacklist_label = QtWidgets.QLabel(self.Classification)
        self.Blacklist_label.setGeometry(QtCore.QRect(20, 20, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.Blacklist_label.setFont(font)
        self.Blacklist_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Blacklist_label.setObjectName("Blacklist_label")
        self.Whitelist_Label = QtWidgets.QLabel(self.Classification)
        self.Whitelist_Label.setGeometry(QtCore.QRect(length-700,20,200,25))
        self.Whitelist_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Whitelist_Label.setObjectName("Whitelist_Label")
        self.Whitelist = QtWidgets.QTableWidget(self.Classification)
        self.Whitelist.setGeometry(QtCore.QRect((length-105)/2+30,50,(length-106)/2-10,breadth-250))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.Whitelist.setFont(font)
        self.Whitelist.setAutoFillBackground(True)
        self.Whitelist.setStyleSheet("background-color: rgb(115, 210, 22);")
        self.Whitelist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Whitelist.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Whitelist.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Whitelist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Whitelist.setProperty("showDropIndicator", False)
        self.Whitelist.setAlternatingRowColors(False)
        self.Whitelist.setObjectName("Whitelist")
        self.Whitelist.setColumnCount(2)
        self.Whitelist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Whitelist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Whitelist.setHorizontalHeaderItem(1, item)
        self.Whitelist.horizontalHeader().setMinimumSectionSize(200)
        self.Whitelist.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.Classification, "")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.About_text_frame = QtWidgets.QTextBrowser(self.About)
        self.About_text_frame.setGeometry(QtCore.QRect(0, 0, length-66, breadth-150))
        self.About_text_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.About_text_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.About_text_frame.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.About_text_frame.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.About_text_frame.setObjectName("About_text_frame")
        self.tabWidget.addTab(self.About, "")
        self.Gnat_Label = QtWidgets.QLabel(self.centralwidget)
        self.Gnat_Label.setGeometry(QtCore.QRect(0, 0, length,30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Gnat_Label.setFont(font)
        self.Gnat_Label.setAutoFillBackground(False)
        self.Gnat_Label.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"font: 14pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Gnat_Label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Gnat_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Gnat_Label.setWordWrap(True)
        self.Gnat_Label.setObjectName("Gnat_Label")
        MainWindow.setCentralWidget(self.centralwidget)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Genysis NAT"))
        self.Basic_View_Table.setSortingEnabled(True)
        self.Basic_Reload_List.setText(_translate("MainWindow", "Reload List"))
        self.Basic_Reload_List.clicked.connect(self.retranslateUi)

        self.Basic_Network_Graph.setText(_translate("MainWindow", "Network Graph"))
        self.Basic_Connection_Map.setText(_translate("MainWindow", "Connection Map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Basic_View), _translate("MainWindow", "Basic View"))
        self.Detaile_view_list.setSortingEnabled(True)
        self.Detail_Network_Graph.setText(_translate("MainWindow", "Network Graph"))
        self.Detail_Reload_List.setText(_translate("MainWindow", "Reload List"))
        self.Detail_Reload_List.clicked.connect(self.retranslateUi)
        self.Detail_Connection_Map.setText(_translate("MainWindow", "Connection Map"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Detailed_View), _translate("MainWindow", "Detailed View"))

        self.Start_Scan.setText(_translate("MainWindow", "Start Scan"))
        self.Start_Scan.clicked.connect(rkhunter_scan.rk_hunter)
        self.Stop_Scan.setText(_translate("MainWindow", "Stop Scan"))


        self.System_scan_list.setSortingEnabled(True)
        #self.pushButton.setText(_translate("MainWindow", "Copy"))
        #self.pushButton_2.setText(_translate("MainWindow", "Save As"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.System_Scan), _translate("MainWindow", "System Scan"))
        item = self.Blacklist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.Blacklist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Application Name"))
        self.Blacklist_label.setText(_translate("MainWindow", "BLACKLIST(Wall Of Shame)"))
        self.Whitelist_Label.setText(_translate("MainWindow", "WHITELIST(Wall Of Fame)"))
        item = self.Whitelist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.Whitelist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Application Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Classification),_translate("MainWindow", "Classification"))

        self.About_text_frame.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:88; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:400;\"><br /></p>\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600; color:#5c3566;\"><br /></p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#5c3566;\">Genysis Network Analysis Tool</span></p>\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; font-weight:600; text-decoration: underline; color:#5c3566;\"><br /></p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:400; color:#2e3436;\">GNAT is made by Team Lambda .</span></p>\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:400;\"><br /></p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:400; color:#000000;\">This tool helps in analysis of the onging processes going in the background and helps the user to  identify the type of access an process is trying to get without the information of user. The tool tell who is trying to access user\'s computer and identifies the rootkits that maliciously works on you computer which are responsible for stealing your data.</span></p>\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:400; color:#000000;\"><br /></p>\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:400; color:#000000;\">The various views (such as Map/Graph/Detailed) also gives a clear vision of the network connections and helps user to analyse the Network.  </span></p>\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:400;\"><br /></p>\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:400;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("MainWindow", "About"))
        self.Gnat_Label.setText(_translate("MainWindow", "Genysis Network Analysis Tool"))


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        translate = QtCore.QCoreApplication.translate
        listtemp = get_csv_to_list("../Integrated/main_output.csv")
        list1=[]
        for b in range(len(listtemp)):
            l3 = []
            l3.append(listtemp[b][6])
            l3.append(listtemp[b][4])
            l3.append(listtemp[b][10])
            l3.append(listtemp[b][9])
            l3.append(listtemp[b][8])
            list1.append(l3)
        print(list1)
        rowlen1 = len(list1)
        columnlen1 = len(list1[0])
        self.Basic_View_Table.setRowCount(rowlen1 - 1)
        self.Basic_View_Table.setColumnCount(columnlen1)
        self.Basic_View_Table.setObjectName("Basic_View_Table")
        for k in range(columnlen1):
            item = QtWidgets.QTableWidgetItem()
            self.Basic_View_Table.setHorizontalHeaderItem(k, item)
        item = QtWidgets.QTableWidgetItem()
        for i in range(rowlen1):
            for j in range(columnlen1):
                self.Basic_View_Table.setItem(i, j, item)
                item = QtWidgets.QTableWidgetItem()
        _translate = QtCore.QCoreApplication.translate
        for i in range(columnlen1):
            item = self.Basic_View_Table.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", list1[0][i]))
        for i in range(1, rowlen1):
            for j in range(columnlen1):
                item = self.Basic_View_Table.item(i - 1, j)
                item.setText(_translate("MainWindow", str(list1[i][j])))



        _translate = QtCore.QCoreApplication.translate
        list2 = get_csv_to_list("../Integrated/main_output.csv")
        #print(list2)
        rowlen2 = len(list2)
        columnlen2 = len(list2[0])
        self.Detaile_view_list.setRowCount(rowlen2 - 1)
        self.Detaile_view_list.setColumnCount(columnlen2)
        self.Detaile_view_list.setObjectName("Basic_View_Table")
        for k in range(columnlen2):
            item = QtWidgets.QTableWidgetItem()
            self.Detaile_view_list.setHorizontalHeaderItem(k, item)
        item = QtWidgets.QTableWidgetItem()
        for i in range(rowlen2):
            for j in range(columnlen2):
                self.Detaile_view_list.setItem(i, j, item)
                item = QtWidgets.QTableWidgetItem()
        _translate = QtCore.QCoreApplication.translate
        for i in range(columnlen2):
            item = self.Detaile_view_list.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", list2[0][i]))
        for i in range(1,rowlen2):
            for j in range(columnlen2):
                item = self.Detaile_view_list.item(i-1, j)
                item.setText(_translate("MainWindow",str(list2[i][j])))




        '''_translate = QtCore.QCoreApplication.translate
        list3 = get_csv_to_list("../Integrated/black_listed.csv")
        print(list3)
        rowlen3 = len(list3)
        columnlen3 = len(list2[0])
        self.Blacklist.setRowCount(rowlen3 - 1)
        self.Blacklist.setColumnCount(columnlen3)
        self.Blacklist.setObjectName("Blacklist")
        for k in range(columnlen3):
            item = QtWidgets.QTableWidgetItem()
            self.Blacklist.setHorizontalHeaderItem(k, item)
        item = QtWidgets.QTableWidgetItem()
        for i in range(rowlen3):
            for j in range(columnlen3):
                self.Blacklist.setItem(i, j, item)
                item = QtWidgets.QTableWidgetItem()
        _translate = QtCore.QCoreApplication.translate
        for i in range(columnlen3):
            item = self.Blacklist.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", list3[0][i]))
        for i in range(1,rowlen3):
            for j in range(columnlen3):
                item = self.Blacklist.item(i-1, j)
                item.setText(_translate("MainWindow",str(list3[i][j])))'''



#CSV Reading Function
def get_csv_to_list(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        f.close()
    return your_list[:-1]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    #Calculating Available Scree Size
    screen = app.primaryScreen()
    size = screen.size()
    rect = screen.availableGeometry()
    length = size.width()
    breadth = size.height()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
