# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random
from pathlib import Path

class Ui_PagesWindow(object):

    words_list = []
    direc = str(Path.cwd())
    print(direc)
    dir_list = direc.split('/')
    if dir_list[-1] == 'src':
        direc = direc[:-4]
    print(direc)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("%s/images/logo.png" % self.direc), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #A7CAD1, stop:1 #9196ba);\n"
"border-radius: 10px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setGeometry(QtCore.QRect(-1, 0, 130, 500))
        self.sidebar.setStyleSheet("background: rgb(118, 174, 150);\n"
"border-radius: 10px;\n"
"")
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.btn_test = QtWidgets.QPushButton(self.sidebar)
        self.btn_test.setGeometry(QtCore.QRect(30, 55, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_test.setFont(font)
        self.btn_test.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_test.setStyleSheet("QPushButton{\n"
"background: rgb(25, 106, 72);\n"
"color: #fff;\n"
"border-radius: 4px;\n"
"}")
        self.btn_test.setObjectName("btn_test")
        self.btn_setting = QtWidgets.QPushButton(self.sidebar)
        self.btn_setting.setGeometry(QtCore.QRect(30, 105, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_setting.setFont(font)
        self.btn_setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_setting.setStyleSheet("QPushButton{\n"
"background:rgb(211, 221, 221);\n"
"color: rgb(12, 39, 46);\n"
"border-radius: 4px;\n"
"}")
        self.btn_setting.setObjectName("btn_setting")
        self.btn_help = QtWidgets.QPushButton(self.sidebar)
        self.btn_help.setGeometry(QtCore.QRect(30, 155, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_help.setFont(font)
        self.btn_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_help.setStyleSheet("QPushButton{\n"
"background:rgb(211, 221, 221);\n"
"color: rgb(12, 39, 46);\n"
"border-radius: 4px;\n"
"}")
        self.btn_help.setObjectName("btn_help")
        self.label = QtWidgets.QLabel(self.sidebar)
        self.label.setGeometry(QtCore.QRect(10, 322, 111, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("%s/images/sidebar.png" % self.direc))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_about = QtWidgets.QPushButton(self.sidebar)
        self.btn_about.setGeometry(QtCore.QRect(30, 205, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_about.setFont(font)
        self.btn_about.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_about.setStyleSheet("QPushButton{\n"
"background:rgb(211, 221, 221);\n"
"color: rgb(12, 39, 46);\n"
"border-radius: 4px;\n"
"}")
        self.btn_about.setObjectName("btn_about")
        self.pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.pages.setGeometry(QtCore.QRect(150, 20, 721, 511))
        self.pages.setStyleSheet("background: rgba(0,0,0,0);")
        self.pages.setObjectName("pages")
        self.page_test = QtWidgets.QWidget()
        self.page_test.setStyleSheet("border-radius: 0;")
        self.page_test.setObjectName("page_test")
        self.typethis = QtWidgets.QLabel(self.page_test)
        self.typethis.setGeometry(QtCore.QRect(200, 60, 315, 45))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.typethis.setFont(font)
        self.typethis.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 8px;")
        self.typethis.setAlignment(QtCore.Qt.AlignCenter)
        self.typethis.setObjectName("typethis")
        self.label_3 = QtWidgets.QLabel(self.page_test)
        self.label_3.setGeometry(QtCore.QRect(65, 65, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.words = QtWidgets.QLabel(self.page_test)
        self.words.setGeometry(QtCore.QRect(35, 140, 641, 50))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.words.setFont(font)
        self.words.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 5px;\n"
"padding: 8px;")
        self.words.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.words.setObjectName("words")
        self.en = QtWidgets.QLineEdit(self.page_test)
        self.en.setGeometry(QtCore.QRect(35, 228, 522, 45))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.en.setFont(font)
        self.en.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 5px;\n"
"padding: 8px;")
        self.en.setObjectName("en")
        self.timer = QtWidgets.QLabel(self.page_test)
        self.timer.setGeometry(QtCore.QRect(575, 228, 45, 45))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        self.timer.setFont(font)
        self.timer.setStyleSheet("background: rgba(65, 140, 98, 0.5);\n"
"color: #000;\n"
"border-radius: 5px;")
        self.timer.setAlignment(QtCore.Qt.AlignCenter)
        self.timer.setObjectName("timer")
        self.restart = QtWidgets.QPushButton(self.page_test)
        self.restart.setGeometry(QtCore.QRect(635, 228, 45, 45))
        self.restart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.restart.setStyleSheet("background: none;")
        self.restart.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("%s/images/restart.png" % self.direc), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restart.setIcon(icon1)
        self.restart.setIconSize(QtCore.QSize(50, 50))
        self.restart.setObjectName("restart")
        self.label_6 = QtWidgets.QLabel(self.page_test)
        self.label_6.setGeometry(QtCore.QRect(35, 328, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_test)
        self.label_7.setGeometry(QtCore.QRect(230, 328, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_test)
        self.label_8.setGeometry(QtCore.QRect(35, 365, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_test)
        self.label_9.setGeometry(QtCore.QRect(230, 365, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.Cwords = QtWidgets.QLabel(self.page_test)
        self.Cwords.setGeometry(QtCore.QRect(131, 340, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.Cwords.setFont(font)
        self.Cwords.setStyleSheet("color: rgb(10, 58, 30);")
        self.Cwords.setObjectName("Cwords")
        self.Cletters = QtWidgets.QLabel(self.page_test)
        self.Cletters.setGeometry(QtCore.QRect(134, 370, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.Cletters.setFont(font)
        self.Cletters.setStyleSheet("color: rgb(10, 58, 30);")
        self.Cletters.setObjectName("Cletters")
        self.Wwords = QtWidgets.QLabel(self.page_test)
        self.Wwords.setGeometry(QtCore.QRect(321, 340, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.Wwords.setFont(font)
        self.Wwords.setStyleSheet("color: rgb(164, 0, 0);")
        self.Wwords.setObjectName("Wwords")
        self.frame_2 = QtWidgets.QFrame(self.page_test)
        self.frame_2.setGeometry(QtCore.QRect(429, 312, 191, 111))
        self.frame_2.setStyleSheet("background: rgba(65, 140, 98, 0.5);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(66, 7, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background: none;")
        self.label_14.setObjectName("label_14")
        self.result = QtWidgets.QLabel(self.frame_2)
        self.result.setGeometry(QtCore.QRect(36, 31, 231, 51))
        font = QtGui.QFont()
        font.setFamily("KacstDigital")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.result.setFont(font)
        self.result.setStyleSheet("color: rgb(53, 34, 94);\n"
"background: none;")
        self.result.setObjectName("result")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(44, 82, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background: none;")
        self.label_16.setObjectName("label_16")
        self.Wletters = QtWidgets.QLabel(self.page_test)
        self.Wletters.setGeometry(QtCore.QRect(323, 373, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        self.Wletters.setFont(font)
        self.Wletters.setStyleSheet("color: rgb(164, 0, 0);")
        self.Wletters.setObjectName("Wletters")
        self.pages.addWidget(self.page_test)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.label_2 = QtWidgets.QLabel(self.page_setting)
        self.label_2.setGeometry(QtCore.QRect(50, 137, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.page_setting)
        self.label_4.setGeometry(QtCore.QRect(50, 207, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_setting)
        self.label_5.setGeometry(QtCore.QRect(50, 277, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.timeset = QtWidgets.QComboBox(self.page_setting)
        self.timeset.setGeometry(QtCore.QRect(170, 131, 125, 30))
        self.timeset.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 5px;")
        self.timeset.setObjectName("timeset")
        self.timeset.addItem("")
        self.timeset.addItem("")
        self.timeset.addItem("")
        self.langset = QtWidgets.QComboBox(self.page_setting)
        self.langset.setGeometry(QtCore.QRect(170, 209, 125, 30))
        self.langset.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 5px;")
        self.langset.setObjectName("langset")
        self.langset.addItem("")
        self.langset.addItem("")
        self.difset = QtWidgets.QComboBox(self.page_setting)
        self.difset.setGeometry(QtCore.QRect(170, 282, 125, 30))
        self.difset.setStyleSheet("background: #E0E0E0;\n"
"border-radius: 5px;")
        self.difset.setObjectName("difset")
        self.difset.addItem("")
        self.difset.addItem("")
        self.difset.addItem("")
        self.label_10 = QtWidgets.QLabel(self.page_setting)
        self.label_10.setGeometry(QtCore.QRect(365, 72, 281, 321))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("%s/images/key-img.png" % self.direc))
        self.label_10.setObjectName("label_10")
        self.pages.addWidget(self.page_setting)
        self.page_help = QtWidgets.QWidget()
        self.page_help.setObjectName("page_help")
        self.label_12 = QtWidgets.QLabel(self.page_help)
        self.label_12.setGeometry(QtCore.QRect(210, 260, 67, 17))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.page_help)
        self.label_15.setGeometry(QtCore.QRect(134, 296, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.page_help)
        self.label_17.setGeometry(QtCore.QRect(40, 310, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(60, 80, 164)")
        self.label_17.setObjectName("label_17")
        self.label_11 = QtWidgets.QLabel(self.page_help)
        self.label_11.setGeometry(QtCore.QRect(40, 80, 641, 111))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.page_help)
        self.label_13.setGeometry(QtCore.QRect(40, 166, 581, 71))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pages.addWidget(self.page_help)
        self.page_about = QtWidgets.QWidget()
        self.page_about.setObjectName("page_about")
        self.label_18 = QtWidgets.QLabel(self.page_about)
        self.label_18.setGeometry(QtCore.QRect(40, 80, 611, 171))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page_about)
        self.label_19.setGeometry(QtCore.QRect(40, 40, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.page_about)
        self.label_20.setGeometry(QtCore.QRect(40, 265, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page_about)
        self.label_21.setGeometry(QtCore.QRect(40, 300, 611, 171))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.pages.addWidget(self.page_about)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(838, 11, 30, 30))
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setStyleSheet("background: #9196ba;\n"
"")
        self.btn_exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("%s/images/close.png" % self.direc), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon2)
        self.btn_exit.setIconSize(QtCore.QSize(20, 20))
        self.btn_exit.setObjectName("btn_exit")
        self.btn_min = QtWidgets.QPushButton(self.centralwidget)
        self.btn_min.setGeometry(QtCore.QRect(800, 12, 30, 30))
        self.btn_min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_min.setStyleSheet("background: none;\n"
"")
        self.btn_min.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("%s/images/minimize.png" % self.direc), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_min.setIcon(icon3)
        self.btn_min.setIconSize(QtCore.QSize(20, 20))
        self.btn_min.setObjectName("btn_min")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(0)
        self.btn_exit.clicked.connect(MainWindow.close)
        self.btn_min.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Typing Speed Test"))
        self.btn_test.setText(_translate("MainWindow", "Test"))
        self.btn_setting.setText(_translate("MainWindow", "Settings"))
        self.btn_help.setText(_translate("MainWindow", "Help"))
        self.btn_about.setText(_translate("MainWindow", "About"))
        self.typethis.setText(_translate("MainWindow", "Type This"))
        self.label_3.setText(_translate("MainWindow", "Type this word:"))
        self.words.setText(_translate("MainWindow", "These are some words that should be typed..."))
        self.en.setPlaceholderText(_translate("MainWindow", "Type Here..."))
        self.timer.setText(_translate("MainWindow", "60"))
        self.label_6.setText(_translate("MainWindow", "Correct Words:"))
        self.label_7.setText(_translate("MainWindow", "Wrong Words:"))
        self.label_8.setText(_translate("MainWindow", "Correct Letters:"))
        self.label_9.setText(_translate("MainWindow", "Wrong Letters:"))
        self.Cwords.setText(_translate("MainWindow", "10 words"))
        self.Cletters.setText(_translate("MainWindow", "10 letters"))
        self.Wwords.setText(_translate("MainWindow", "10 words"))
        self.label_14.setText(_translate("MainWindow", "Result:"))
        self.result.setText(_translate("MainWindow", "52 WPM"))
        self.label_16.setText(_translate("MainWindow", "(words per minute)"))
        self.Wletters.setText(_translate("MainWindow", "10 Letters"))
        self.label_2.setText(_translate("MainWindow", "Time:"))
        self.label_4.setText(_translate("MainWindow", "Language:"))
        self.label_5.setText(_translate("MainWindow", "Difficulty:"))
        self.timeset.setItemText(0, _translate("MainWindow", "1 Minute"))
        self.timeset.setItemText(1, _translate("MainWindow", "30 Seconds"))
        self.timeset.setItemText(2, _translate("MainWindow", "2 Minutes"))
        self.langset.setItemText(0, _translate("MainWindow", "English"))
        self.langset.setItemText(1, _translate("MainWindow", "Persian"))
        self.difset.setItemText(0, _translate("MainWindow", "Normal"))
        self.difset.setItemText(1, _translate("MainWindow", "Easy"))
        self.difset.setItemText(2, _translate("MainWindow", "Difficult"))
        self.label_15.setText(_translate("MainWindow", "for report a problem or ask a question."))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"mailto: m.matin.ardestani@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Send Email</span></a><span style=\" text-decoration: underline;\"><br/></span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "There is a button next to the timer.  When you press it, you\'r time starts\n"
"and you type as fast as you can!\n"
"You can also customize your test in Settings"))
        self.label_13.setText(_translate("MainWindow", "After typing each word, press Enter and go for the next word."))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>The Typing Test measures an individual\'s typing speed and accuracy. </p><p>The test generates three scores: </p><p>- Words per Minute (WPM)<br/>- Number of Errors<br/>- and Adjusted Words per Minute (WPM - Errors)</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "What is a Typing test?"))
        self.label_20.setText(_translate("MainWindow", "About Creator"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p>Matin Ardestani is an Iranian teenager who is keen on programming.</p><p>Email: <a href=\"mailto:m.matin.ardestani@gmail.com\">m.matin.ardestani@gmail.com</a> </p><p>GitHub: <a href=\"https://github.com/Matin-Ardestani/\">Matin-Ardestani</a></p></body></html>"))


        # my codes
        self.hard_words = ['certain', 'condition', 'president', 'professor', 'section', 'player', 'interest', 'almost', 'discussion', 'education', 'operation', 'present', 'determine', 'always', 'reason', 'campaign', 'senior', 'minute', 'husband', 'century', 'relate', 'generation', 'behind', 'special', 'analysis', 'remove', 'resource', 'happen', 'everything', 'hospital', 'whether', 'science', 'nature', 'commercial', 'expert', 'management', 'program', 'series', 'author', 'particular', 'across', 'machine', 'environmental', 'really', 'perform', 'design', 'establish', 'chance', 'material', 'million', 'anything', 'newspaper', 'administration', 'Democrat', 'meeting', 'finger', 'together', 'themselves', 'although', 'teacher', 'security', 'nothing', 'explain', 'memory', 'instead', 'investment', 'should', 'federal', 'development', 'purpose', 'others', 'responsibility', 'reduce', 'weight', 'current', 'production', 'strong', 'receive', 'contain', 'situation', 'Republican', 'artist', 'character', 'candidate', 'itself', 'recognize', 'period', 'market', 'activity', 'politics', 'system', 'soldier', 'organization', 'specific', 'disease', 'factor', 'western', 'create', 'report', 'yourself', 'individual', 'clearly', 'despite', 'window', 'entire', 'around', 'probably', 'evening', 'standard', 'prevent', 'majority', 'simply', 'expect', 'picture', 'account', 'listen', 'respond', 'approach', 'improve', 'already', 'private', 'forget', 'surface', 'magazine', 'whatever', 'research', 'father', 'worker', 'either', 'conference', 'source', 'before', 'appear', 'record', 'ground', 'choose', 'military', 'society', 'threat', 'student', 'without', 'continue', 'wonder', 'institution', 'billion', 'represent', 'between', 'quality', 'remember', 'government', 'camera', 'police', 'college', 'person', 'position', 'general', 'subject', 'national', 'nearly', 'necessary', 'common', 'movement', 'couple', 'through', 'reveal', 'debate', 'understand', 'herself', 'audience', 'develop', 'garden', 'though', 'future', 'performance', 'social', 'natural', 'indicate', 'imagine', 'environment', 'ability', 'number', 'against', 'challenge', 'training', 'shoulder', 'victim', 'process', 'direction', 'company', 'affect', 'identify', 'arrive']
        self.easy_words = ['sea', 'give', 'deal', 'let', 'walk', 'house', 'card', 'out', 'vote', 'home', 'seem', 'start', 'they', 'black', 'and', 'store', 'play', 'ready', 'time', 'sign', 'even', 'head', 'keep', 'food', 'your', 'wrong', 'thank', 'trade', 'name', 'spend', 'unit', 'more', 'sure', 'still', 'know', 'wall', 'light', 'girl', 'check', 'TV', 'power', 'floor', 'since', 'take', 'force', 'west', 'score', 'guess', 'offer', 'bed', 'media', 'sport', 'where', 'agent', 'hope', 'test', 'share', 'maybe', 'to', 'have', 'staff', 'model', 'boy', 'now', 'air', 'cover', 'month', 'good', 'nice', 'wait', 'idea', 'gun', 'none', 'ball', 'her', 'issue', 'treat', 'once', 'over', 'get', 'sound', 'leave', 'why', 'death', 'item', 'five', 'happy', 'move', 'or', 'laugh', 'under', 'such', 'if', 'along', 'third', 'admit', 'stage', 'young', 'edge', 'room', 'send', 'high', 'week', 'than', 'first', 'show', 'rest', 'meet', 'part', 'onto', 'might', 'open', 'team', 'price', 'fall', 'fly', 'carry', 'use', 'value', 'major', 'draw', 'man', 'drop', 'new', 'blue', 'argue', 'case', 'again', 'here', 'mouth', 'Mrs', 'note', 'build', 'hair', 'coach', 'adult', 'best', 'gas', 'right', 'fire', 'rule', 'old', 'worry', 'view', 'per', 'hard', 'bar', 'win', 'after', 'ok', 'live', 'end', 'but', 'owner', 'able', 'film', 'agree', 'trip', 'that', 'three', 'sing', 'only', 'bad', 'other', 'two', 'up', 'not', 'among', 'town', 'great', 'rise', 'skill', 'write', 'today', 'lose', 'tree', 'one', 'focus', 'red', 'watch', 'would', 'skin', 'arm', 'truth', 'local', 'paper', 'key', 'star', 'care', 'tough', 'come', 'nor', 'own', 'smile', 'tell', 'foot', 'space', 'cause', 'close', 'very', 'his', 'next', 'break', 'trial', 'wish', 'civil']
        self.normal_words = ['need', 'art', 'drop', 'police', 'study', 'deal', 'toward', 'position', 'cancer', 'use', 'fear', 'personal', 'anything', 'score', 'suddenly', 'conference', 'section', 'write', 'daughter', 'least', 'visit', 'theory', 'live', 'especially', 'yet', 'alone', 'public', 'news', 'training', 'machine', 'treatment', 'garden', 'money', 'entire', 'project', 'floor', 'bag', 'huge', 'join', 'disease', 'phone', 'street', 'third', 'bank', 'site', 'west', 'Republican', 'possible', 'south', 'light', 'he', 'hot', 'but', 'wind', 'for', 'rather', 'by', 'special', 'fail', 'major', 'main', 'over', 'shoot', 'trouble', 'die', 'kind', 'official', 'her', 'expect', 'college', 'attorney', 'three', 'may', 'food', 'quality', 'wear', 'weight', 'instead', 'fall', 'great', 'hundred', 'provide', 'goal', 'down', 'very', 'him', 'legal', 'manage', 'describe', 'human', 'continue', 'writer', 'child', 'dog', 'student', 'hope', 'cover', 'price', 'skin', 'many', 'health', 'TV', 'medical', 'clear', 'party', 'shot', 'impact', 'must', 'get', 'who', 'I', 'city', 'station', 'avoid', 'vote', 'important', 'girl', 'success', 'agree', 'sea', 'trade', 'yeah', 'investment', 'wrong', 'cup', 'loss', 'difference', 'spring', 'figure', 'upon', 'can', 'private', 'debate', 'participant', 'above', 'without', 'rate', 'you', 'radio', 'compare', 'leader', 'whose', 'stay', 'age', 'new', 'table', 'environment', 'man', 'sound', 'kitchen', 'tonight', 'certainly', 'candidate', 'love', 'address', 'brother', 'pressure', 'Mrs', 'material', 'language', 'heavy', 'PM', 'else', 'media', "n't", 'sing', 'land', 'almost', 'start', 'charge', 'hard', 'dream', 'see', 'face', 'hotel', 'today', 'look', 'friend', 'control', 'test', 'help', 'page', 'would', 'it', 'sort', 'forward', 'military', 'arrive', 'order', 'leg', 'the', 'smile', 'economy', 'since', 'some', 'reveal', 'through', 'development', 'seat', 'marriage', 'blue', 'voice', 'about', 'my', 'serve', 'pay', 'system', 'discuss', 'build', 'production', 'cut', 'usually', 'window', 'ever', 'manager', 'sister', 'knowledge', 'we'] 
        self.persian_words = ['گوش دادن', 'راه', 'اردوگاه', 'تک', 'قایق', 'لحظه ای', 'برق', 'بهار', 'ویژه', 'کمک', 'کودکان', 'بهترین', 'به عقب', 'مرد', 'نمره', 'پدر و مادر', 'معامله', 'کامیون', 'دقیق', 'خواهد شد', 'بوده', 'دلیل', 'می خواهم', 'رنگ', 'روستای', 'سیاه و سفید', 'اکسیژن', 'پوشش', 'شارژ', 'نوع', 'او', 'نشان می دهد', 'منطقه', 'صدا', 'معمول', 'که', 'برادر', 'درایو', 'روز', 'را', 'سه', 'هفته', 'فروشگاه', 'بعدی', 'آزمون', 'هزار', 'قرمز', 'پسر', 'کامل', 'جفت', 'صفحه', 'جستجو', 'ارسال', 'به', 'تصور کنید', 'بزودی', 'خوب', 'سرگرم', 'انتخاب کنید', 'به همین دلیل', 'مایع', 'I', 'قرار دادن', 'سبز', 'وحشی', 'چاپ', 'آن', 'باید', 'متفاوت ا', 'تخت', 'جمع کردن', 'تن', 'خاصیت', 'شان', 'برخی از', 'ملاقات', 'قند', 'جریان', 'همسر', 'خشک', 'نظر', 'سفید', 'به نظر می رسد', 'همیشه', 'چگونه', 'وارد شدن', 'بحث', 'برگزار شد', 'تغییر', 'کنند', 'دوره', 'ساخت', 'یافت', 'کراوات', 'رکورد', 'فوری', 'خود', 'مطبوعات', 'هیچ', 'فقط', 'دو', 'اسلحه', 'رایت', 'مربع', 'تقسیم', 'نیم', 'ترس', 'آهنگ', 'تمام', 'گسترش', 'عمومی', 'بزرگ', 'شود', 'حال', 'تجارت', 'ساعت', 'حرارت', 'انگشت', 'کت و ش', 'گاو', 'واقعی', 'آرزو', 'چهار', 'سرد', 'نقطه', 'دوست دارم', 'خط', 'برابر', 'داغ', 'چشم', 'توقف', 'در', 'اسب', 'ترک', 'شش', 'تپه', 'جمع آوری', 'مغناطیس', 'هر', 'نه', 'پا', 'انتظار', 'سهم', 'با', 'بودن', 'نور', 'شنا', 'بستگی دارد', 'موتور', 'هم', 'دست', 'قرار', 'فریاد', 'ممکن است', 'سیم', 'علاقه', 'بیت', 'کودک', 'دایره', 'نسبت به', 'دوم', 'کلاس', 'رودخانه', 'جدول', 'مثال', 'حیاط', 'بادبان', 'یک', 'تا', 'زنان', 'دفتر', 'فصل', 'دندانها', 'ب کنید', 'زمین', 'درست', 'ذخیره کردن', 'کافی', 'الگوی', 'اثر', 'زرد', 'شمال', 'پرواز', 'ذهن', 'خشم', 'عضویت', 'مناسب', 'صندلی', 'مشغول', 'زیادی', 'موج', 'تر', 'گوشه', 'کمی', 'نامونام', 'اتصال', 'گوش', 'بال', 'ستاره', 'اینچ', 'پر', 'هیئت مدیره', 'ساخته شده', 'مدرسه', 'چه']
        self.difset.currentTextChanged.connect(self.text_difficulty)



        self.en.returnPressed.connect(self.check)
        self.correct_words = 0
        self.wrong_words = 0
        self.correct_letters = 0
        self.wrong_letter = 0

        self.restart.clicked.connect(self.timming)
        self.en.setEnabled(False)
        self.en.setPlaceholderText('Type here...')

        self.Cwords.setText('')
        self.Wwords.setText('')
        self.Cletters.setText('')
        self.Wletters.setText('')
        self.result.setText('')

        self.text_difficulty()
        self.timeset.currentTextChanged.connect(self.time_managment)
        self.langset.currentTextChanged.connect(self.set_lang)

        self.last_time = '60'

    def get_result(self):
        if self.last_time == '30':
            result = (self.correct_letters / 5) / 0.5
        elif self.last_time == '60':
            result = (self.correct_letters / 5) / 1
        elif self.last_time == '120':
            result = (self.correct_letters / 5) / 2
        print('last time is : ' , self.last_time)
        return result

    def make_text(self):
        self.typing_words = ''
        for i in range(200):
            self.typing_words += self.words_list[random.randint(0 ,len(self.words_list) - 1)] + ' '
        
        self.tw_list = self.typing_words.split()
        self.words.setText(self.typing_words)
        self.typethis.setText(self.tw_list[0])


        
    def text_difficulty(self):
        if self.difset.currentText() == 'Normal':
            self.words_list = self.normal_words
            self.make_text()
        elif self.difset.currentText() == 'Easy':
            self.words_list = self.easy_words
            self.make_text()
        elif self.difset.currentText() == 'Difficult':
            self.words_list = self.hard_words
            self.make_text()



    def time_managment(self):
        if self.timeset.currentText() == '1 Minute':
            self.timer.setText(str(60))
            self.last_time = str(60)
        elif self.timeset.currentText() == '30 Seconds':
            self.timer.setText(str(30))
            self.last_time = str(30)
        elif self.timeset.currentText() == '2 Minutes':
            self.timer.setText(str(120))
            self.last_time = str(120)

    def set_lang(self):
        if self.langset.currentText() == 'Persian':
            self.words_list = self.persian_words
            self.difset.setEnabled(False)
            self.make_text()
        else:
            self.difset.setEnabled(True)
            self.text_difficulty()


    def check(self):
            def check_word():
                the_word = self.tw_list[0]
                en_word = self.en.text().strip()
                if en_word == the_word:
                    self.correct_words += 1
                    self.correct_letters += len(the_word)
                else:
                    self.wrong_words += 1
                    if len(en_word) == len(the_word):
                        counter = -1
                        for i in the_word:
                            counter += 1
                            if the_word[counter] == en_word[counter]:
                                self.correct_letters += 1
                            else:
                                self.wrong_letter += 1
                    else:
                        diff = abs(len(en_word) - len(the_word))
                        if len(en_word) > len(the_word):
                            counter = -1
                            for i in the_word:
                                counter += 1
                                if the_word[counter] == en_word[counter]:
                                    self.correct_letters += 1
                                else:
                                    self.wrong_letter += 1
                            self.wrong_letter += diff
                        else:
                            counter = -1
                            for i in en_word:
                                counter += 1
                                if the_word[counter] == en_word[counter]:
                                    self.correct_letters += 1
                                else:
                                    self.wrong_letter += 1

            check_word()

            if len(self.tw_list) > 1:
                self.tw_list.pop(0)
                counter = -1
                for this in self.typing_words:
                    counter += 1
                    if this == ' ':
                        self.typing_words = self.typing_words[(counter + 1):]
                        break
            else:
                self.typing_words = ''
                for i in range(200):
                    self.typing_words += self.words_list[random.randint(0 ,len(self.words_list) - 1)] + ' '
        
                self.tw_list = self.typing_words.split()

            self.words.setText(self.typing_words)
            self.typethis.setText(self.tw_list[0])

            self.en.setText('')
            print('cw: %s, ww: %s, cl: %s, wl: %s' %(self.correct_words, self.wrong_words , self.correct_letters, self.wrong_letter))

    def second(self):
        global counter
        self.timer.setText(str(counter))
        if counter == 0:
            self.time.stop()
            self.en.setEnabled(False)
            self.restart.setEnabled(True)
            if self.en.text() != '':
                self.check()

            counter = 0

            self.typethis.setText('')
            self.words.setText('')
            self.en.setText('')
            
            # results
            self.Cwords.setText('%s words' % self.correct_words)
            self.Wwords.setText('%s words' % self.wrong_words)
            self.Cletters.setText('%s letters' % self.correct_letters)
            self.Wletters.setText('%s letters' % self.wrong_letter)

            # formula = (characters / 5) / 1 min
            self.result.setText('%s WPM' % int(self.get_result()))

            self.correct_words = 0
            self.wrong_words = 0
            self.correct_letters = 0
            self.wrong_letter = 0

            self.timer.setText(self.last_time)

            self.typing_words = ''
            for i in range(200):
                self.typing_words += self.words_list[random.randint(0 ,len(self.words_list) - 1)] + ' '

            return 0
        counter -= 1


    def timming(self):
        self.tw_list = self.typing_words.split()
        self.words.setText(self.typing_words)
        self.typethis.setText(self.tw_list[0])
        self.Cwords.setText('')
        self.Wwords.setText('')
        self.Cletters.setText('')
        self.Wletters.setText('')
        self.result.setText('')
        self.restart.setEnabled(False)
        global counter
        counter = int(self.timer.text())
        self.en.setEnabled(True)
        self.en.setFocus(True)
        self.time = QtCore.QTimer()
        self.time.timeout.connect(self.second)
        self.time.start(1000)