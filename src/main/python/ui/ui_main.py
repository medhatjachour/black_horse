# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainljqaDF.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1293, 843)
        MainWindow.setMinimumSize(QSize(1000, 640))
        MainWindow.setStyleSheet(u"border:1px;\n"
"border-color: rgb(85, 255, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #F2F8FF;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(600, 336))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_42 = QFrame(self.frame_13)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setGeometry(QRect(20, 30, 560, 60))
        self.frame_42.setMinimumSize(QSize(560, 60))
        self.frame_42.setMaximumSize(QSize(560, 60))
        self.frame_42.setStyleSheet(u"border:2px solid rgb(47, 50, 55);\n"
"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_33.setSpacing(13)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(18, 0, 18, 0)
        self.label_23 = QLabel(self.frame_42)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"background : transparent;\n"
"border:0px;")
        self.label_23.setPixmap(QPixmap(u":/image/user.svg"))

        self.horizontalLayout_33.addWidget(self.label_23)

        self.username_3 = QLineEdit(self.frame_42)
        self.username_3.setObjectName(u"username_3")
        self.username_3.setMinimumSize(QSize(0, 55))
        self.username_3.setStyleSheet(u"font-family: Poppins;\n"
"font-size: 18px;\n"
"font-weight: 400;\n"
"line-height: 27px;\n"
"letter-spacing: 0.1em;\n"
"text-align: left;\n"
"border:0px;\n"
"color:rgb(0, 0, 0);")

        self.horizontalLayout_33.addWidget(self.username_3)

        self.frame_44 = QFrame(self.frame_13)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(20, 110, 560, 60))
        self.frame_44.setMinimumSize(QSize(0, 27))
        self.frame_44.setStyleSheet(u"border:2px solid rgb(47, 50, 55);\n"
"border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_34.setSpacing(13)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(18, 0, 18, 0)
        self.label_24 = QLabel(self.frame_44)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"background : transparent;\n"
"border:0px;")
        self.label_24.setPixmap(QPixmap(u":/image/lock.svg"))

        self.horizontalLayout_34.addWidget(self.label_24)

        self.password_3 = QLineEdit(self.frame_44)
        self.password_3.setObjectName(u"password_3")
        self.password_3.setMinimumSize(QSize(0, 55))
        self.password_3.setStyleSheet(u"font-family: Poppins;\n"
"font-size: 18px;\n"
"font-weight: 400;\n"
"line-height: 27px;\n"
"letter-spacing: 0.1em;\n"
"text-align: left;\n"
"border:0px;\n"
"color:rgb(0, 0, 0);")

        self.horizontalLayout_34.addWidget(self.password_3)

        self.signIn = QPushButton(self.frame_13)
        self.signIn.setObjectName(u"signIn")
        self.signIn.setGeometry(QRect(20, 220, 560, 60))
        self.signIn.setMinimumSize(QSize(560, 60))
        self.signIn.setMaximumSize(QSize(560, 60))
        self.signIn.setCursor(QCursor(Qt.PointingHandCursor))
        self.signIn.setStyleSheet(u"\n"
"font-family: Poppins;\n"
"font-size: 18px;\n"
"font-weight: 600;\n"
"line-height: 27px;\n"
"letter-spacing: 0em;\n"
"text-align: center;\n"
"border:2px solid #56E6B8;\n"
"color: #56E6B8;\n"
"border-radius:10px")

        self.gridLayout.addWidget(self.frame_13, 2, 1, 2, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(182, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(182, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 3, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 134, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 2, 1, 1)

        self.frame_30 = QFrame(self.page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 44))
        self.frame_30.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(892, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.pushButton_5 = QPushButton(self.frame_30)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(25, 40))
        font = QFont()
        font.setPointSize(29)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"color: rgb(0, 132, 198);")

        self.horizontalLayout_9.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_30)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(25, 40))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"color: rgb(0, 193, 0);")

        self.horizontalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_30)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(25, 40))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 25, 17);")

        self.horizontalLayout_9.addWidget(self.pushButton_3)


        self.gridLayout.addWidget(self.frame_30, 0, 0, 1, 4)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_4 = QVBoxLayout(self.page_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setStyleSheet(u"background-color: rgb(43, 47, 51);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 44))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../../../../../Downloads/Telegram Desktop/photo_2023-02-06_19-46-00.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(44, 44))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(220, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(400, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.button_patiensts_7 = QRadioButton(self.frame_7)
        self.button_patiensts_7.setObjectName(u"button_patiensts_7")
        self.button_patiensts_7.setMinimumSize(QSize(102, 38))
        self.button_patiensts_7.setMaximumSize(QSize(14566, 38))
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setBold(False)
        font2.setItalic(False)
        self.button_patiensts_7.setFont(font2)
        self.button_patiensts_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts_7.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts_7.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"padding-left : 0px;\n"
"color : white;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.1);\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts_7.setIconSize(QSize(30, 30))
        self.button_patiensts_7.setChecked(False)

        self.horizontalLayout_3.addWidget(self.button_patiensts_7)

        self.button_patiensts_6 = QRadioButton(self.frame_7)
        self.button_patiensts_6.setObjectName(u"button_patiensts_6")
        self.button_patiensts_6.setMinimumSize(QSize(100, 38))
        self.button_patiensts_6.setMaximumSize(QSize(14566, 38))
        self.button_patiensts_6.setFont(font2)
        self.button_patiensts_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts_6.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts_6.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"padding-left : 0px;\n"
"color : white;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.1);\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts_6.setIconSize(QSize(30, 30))
        self.button_patiensts_6.setChecked(False)

        self.horizontalLayout_3.addWidget(self.button_patiensts_6)

        self.button_patiensts_2 = QRadioButton(self.frame_7)
        self.button_patiensts_2.setObjectName(u"button_patiensts_2")
        self.button_patiensts_2.setMinimumSize(QSize(102, 38))
        self.button_patiensts_2.setMaximumSize(QSize(14566, 38))
        self.button_patiensts_2.setFont(font2)
        self.button_patiensts_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts_2.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts_2.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"padding-left : 0px;\n"
"color : white;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.1);\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts_2.setIconSize(QSize(30, 30))
        self.button_patiensts_2.setChecked(False)

        self.horizontalLayout_3.addWidget(self.button_patiensts_2)

        self.button_patiensts_3 = QRadioButton(self.frame_7)
        self.button_patiensts_3.setObjectName(u"button_patiensts_3")
        self.button_patiensts_3.setMinimumSize(QSize(100, 38))
        self.button_patiensts_3.setMaximumSize(QSize(14566, 38))
        self.button_patiensts_3.setFont(font2)
        self.button_patiensts_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts_3.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts_3.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"padding-left : 0px;\n"
"color : white;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.1);\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts_3.setIconSize(QSize(30, 30))
        self.button_patiensts_3.setChecked(False)

        self.horizontalLayout_3.addWidget(self.button_patiensts_3)

        self.button_patiensts = QRadioButton(self.frame_7)
        self.button_patiensts.setObjectName(u"button_patiensts")
        self.button_patiensts.setMinimumSize(QSize(100, 38))
        self.button_patiensts.setMaximumSize(QSize(14566, 38))
        self.button_patiensts.setFont(font2)
        self.button_patiensts.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"padding-left : 0px;\n"
"color : white;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.1);\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts.setIconSize(QSize(0, 0))
        self.button_patiensts.setChecked(True)

        self.horizontalLayout_3.addWidget(self.button_patiensts)


        self.horizontalLayout_2.addWidget(self.frame_7)

        self.horizontalSpacer_3 = QSpacerItem(220, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_9 = QPushButton(self.frame_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/image/Sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.frame_34 = QFrame(self.frame_5)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(50, 0))
        self.frame_34.setMaximumSize(QSize(50, 16777215))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_34)

        self.frame_29 = QFrame(self.frame_5)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(103, 0))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 7, 0)
        self.pushButton_8 = QPushButton(self.frame_29)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(25, 40))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"color: rgb(0, 132, 198);")

        self.horizontalLayout_10.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.frame_29)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(25, 40))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"color: rgb(0, 193, 0);")

        self.horizontalLayout_10.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_29)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(25, 40))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"color: rgb(255, 25, 17);")

        self.horizontalLayout_10.addWidget(self.pushButton_7)


        self.horizontalLayout_2.addWidget(self.frame_29)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 31))
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 20px;\n"
"border-top-left-radius: 20px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.frame_3)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 20)
        self.frame_9 = QFrame(self.page_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 80))
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 25))
        font3 = QFont()
        font3.setPointSize(11)
        self.label_10.setFont(font3)

        self.gridLayout_3.addWidget(self.label_10, 0, 8, 1, 1)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_12, 1, 1, 1, 1)

        self.procut_sell = QLineEdit(self.frame_9)
        self.procut_sell.setObjectName(u"procut_sell")
        self.procut_sell.setMinimumSize(QSize(0, 40))
        self.procut_sell.setMaximumSize(QSize(400, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        self.procut_sell.setFont(font4)
        self.procut_sell.setLayoutDirection(Qt.LeftToRight)
        self.procut_sell.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.procut_sell.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.procut_sell, 1, 8, 1, 1)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout_3.addWidget(self.label_5, 0, 3, 1, 1)

        self.price_sell = QLineEdit(self.frame_9)
        self.price_sell.setObjectName(u"price_sell")
        self.price_sell.setMinimumSize(QSize(0, 40))
        self.price_sell.setMaximumSize(QSize(100, 16777215))
        self.price_sell.setFont(font3)
        self.price_sell.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.price_sell.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.price_sell, 1, 2, 1, 1)

        self.num_sell = QLineEdit(self.frame_9)
        self.num_sell.setObjectName(u"num_sell")
        self.num_sell.setMinimumSize(QSize(0, 40))
        self.num_sell.setMaximumSize(QSize(100, 16777215))
        self.num_sell.setFont(font3)
        self.num_sell.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.num_sell.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.num_sell, 1, 3, 1, 1)

        self.addToCart = QPushButton(self.frame_9)
        self.addToCart.setObjectName(u"addToCart")
        self.addToCart.setMinimumSize(QSize(99, 40))
        self.addToCart.setMaximumSize(QSize(200, 16777215))
        self.addToCart.setFont(font1)
        self.addToCart.setCursor(QCursor(Qt.PointingHandCursor))
        self.addToCart.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(230, 126, 34);\n"
"	border: 2px solid  rgb(230, 126, 34);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color:rgb(230, 126, 34);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.gridLayout_3.addWidget(self.addToCart, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_3.addWidget(self.label_3, 0, 5, 1, 1)

        self.size_sell = QComboBox(self.frame_9)
        self.size_sell.setObjectName(u"size_sell")
        self.size_sell.setMinimumSize(QSize(100, 40))
        self.size_sell.setMaximumSize(QSize(200, 16777215))
        self.size_sell.setFont(font3)
        self.size_sell.setCursor(QCursor(Qt.PointingHandCursor))
        self.size_sell.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #ced4da;\n"
"	border-radius:4px;\n"
"	padding-left:10px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/image/down.png);\n"
"	width:12;\n"
"	height12;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"QComboBox QListView{\n"
"	font-size:12;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding :5px;\n"
"	background-color:#ffffff;\n"
"	outline:0px;\n"
"}\n"
"QComboBox QListView::item{\n"
"	padding-left :10px;\n"
"	background-color:#ffffff;\n"
"	\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"	background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"	background-color:#1e90ff;\n"
"}")

        self.gridLayout_3.addWidget(self.size_sell, 1, 6, 1, 1)

        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.gridLayout_3.addWidget(self.label_4, 0, 6, 1, 1)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)

        self.color_sell = QComboBox(self.frame_9)
        self.color_sell.setObjectName(u"color_sell")
        self.color_sell.setMinimumSize(QSize(100, 40))
        self.color_sell.setMaximumSize(QSize(200, 16777215))
        self.color_sell.setFont(font3)
        self.color_sell.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_sell.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #ced4da;\n"
"	border-radius:4px;\n"
"	padding-left:10px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/image/down.png);\n"
"	width:12;\n"
"	height12;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"QComboBox QListView{\n"
"	font-size:12;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding :5px;\n"
"	background-color:#ffffff;\n"
"	outline:0px;\n"
"}\n"
"QComboBox QListView::item{\n"
"	padding-left :10px;\n"
"	background-color:#ffffff;\n"
"	\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"	background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"	background-color:#1e90ff;\n"
"}")

        self.gridLayout_3.addWidget(self.color_sell, 1, 5, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.page_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_10)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1023, 528))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.page_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 100))
        self.frame_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(0)
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_2.addWidget(self.label_7, 0, 3, 1, 1)

        self.phone = QLineEdit(self.frame_11)
        self.phone.setObjectName(u"phone")
        self.phone.setMinimumSize(QSize(0, 40))
        self.phone.setMaximumSize(QSize(116, 16777215))
        self.phone.setFont(font3)
        self.phone.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.phone.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.phone, 1, 3, 1, 1)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setFont(font3)

        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)

        self.Link = QLineEdit(self.frame_11)
        self.Link.setObjectName(u"Link")
        self.Link.setMinimumSize(QSize(0, 40))
        self.Link.setMaximumSize(QSize(112, 16777215))
        self.Link.setFont(font3)
        self.Link.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.Link.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Link, 1, 2, 1, 1)

        self.final_price = QLabel(self.frame_11)
        self.final_price.setObjectName(u"final_price")
        font5 = QFont()
        font5.setPointSize(20)
        self.final_price.setFont(font5)
        self.final_price.setCursor(QCursor(Qt.CrossCursor))
        self.final_price.setStyleSheet(u"color: rgb(168, 37, 37);")
        self.final_price.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.final_price, 1, 1, 1, 1)

        self.clientname = QLineEdit(self.frame_11)
        self.clientname.setObjectName(u"clientname")
        self.clientname.setMinimumSize(QSize(0, 40))
        self.clientname.setMaximumSize(QSize(250, 16777215))
        self.clientname.setFont(font3)
        self.clientname.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.clientname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.clientname, 1, 4, 1, 1)

        self.done_sell = QPushButton(self.frame_11)
        self.done_sell.setObjectName(u"done_sell")
        self.done_sell.setMinimumSize(QSize(99, 40))
        self.done_sell.setMaximumSize(QSize(200, 16777215))
        self.done_sell.setFont(font1)
        self.done_sell.setCursor(QCursor(Qt.PointingHandCursor))
        self.done_sell.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.gridLayout_2.addWidget(self.done_sell, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 20)
        self.frame_14 = QFrame(self.page_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 99))
        self.frame_14.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_14)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(9, 9, -1, 9)
        self.add_p_out = QLineEdit(self.frame_14)
        self.add_p_out.setObjectName(u"add_p_out")
        self.add_p_out.setMinimumSize(QSize(0, 40))
        self.add_p_out.setMaximumSize(QSize(100, 16777215))
        self.add_p_out.setFont(font3)
        self.add_p_out.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.add_p_out.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.add_p_out, 3, 5, 1, 1)

        self.add_product = QLineEdit(self.frame_14)
        self.add_product.setObjectName(u"add_product")
        self.add_product.setMinimumSize(QSize(100, 40))
        self.add_product.setMaximumSize(QSize(511, 16777215))
        self.add_product.setFont(font3)
        self.add_product.setCursor(QCursor(Qt.IBeamCursor))
        self.add_product.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.add_product.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.add_product, 3, 10, 1, 1)

        self.enter_store = QPushButton(self.frame_14)
        self.enter_store.setObjectName(u"enter_store")
        self.enter_store.setMinimumSize(QSize(99, 40))
        self.enter_store.setMaximumSize(QSize(200, 16777215))
        self.enter_store.setFont(font1)
        self.enter_store.setCursor(QCursor(Qt.PointingHandCursor))
        self.enter_store.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.gridLayout_5.addWidget(self.enter_store, 3, 1, 1, 1)

        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 25))
        self.label_14.setFont(font3)

        self.gridLayout_5.addWidget(self.label_14, 2, 10, 1, 1)

        self.frame_22 = QFrame(self.frame_14)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_22)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.color_sell_3 = QComboBox(self.frame_22)
        self.color_sell_3.setObjectName(u"color_sell_3")
        self.color_sell_3.setMinimumSize(QSize(100, 40))
        self.color_sell_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_sell_3.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #ced4da;\n"
"	border-radius:4px;\n"
"	padding-left:10px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/image/down.png);\n"
"	width:12;\n"
"	height12;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"QComboBox QListView{\n"
"	font-size:12;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding :5px;\n"
"	background-color:#ffffff;\n"
"	outline:0px;\n"
"}\n"
"QComboBox QListView::item{\n"
"	padding-left :10px;\n"
"	background-color:#ffffff;\n"
"	\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"	background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"	background-color:#1e90ff;\n"
"}")

        self.verticalLayout_9.addWidget(self.color_sell_3)


        self.gridLayout_5.addWidget(self.frame_22, 3, 9, 1, 1)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_15, 3, 2, 1, 1)

        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.gridLayout_5.addWidget(self.label_15, 2, 5, 1, 1)

        self.label_16 = QLabel(self.frame_14)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.gridLayout_5.addWidget(self.label_16, 2, 6, 1, 1)

        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.gridLayout_5.addWidget(self.label_13, 2, 7, 1, 1)

        self.frame_23 = QFrame(self.frame_14)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_23)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.color_sell_4 = QComboBox(self.frame_23)
        self.color_sell_4.setObjectName(u"color_sell_4")
        self.color_sell_4.setMinimumSize(QSize(100, 40))
        self.color_sell_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_sell_4.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #ced4da;\n"
"	border-radius:4px;\n"
"	padding-left:10px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/image/down.png);\n"
"	width:12;\n"
"	height12;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"QComboBox QListView{\n"
"	font-size:12;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding :5px;\n"
"	background-color:#ffffff;\n"
"	outline:0px;\n"
"}\n"
"QComboBox QListView::item{\n"
"	padding-left :10px;\n"
"	background-color:#ffffff;\n"
"	\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"	background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"	background-color:#1e90ff;\n"
"}")

        self.verticalLayout_10.addWidget(self.color_sell_4)


        self.gridLayout_5.addWidget(self.frame_23, 3, 8, 1, 1)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.gridLayout_5.addWidget(self.label_11, 2, 9, 1, 1)

        self.add_num = QLineEdit(self.frame_14)
        self.add_num.setObjectName(u"add_num")
        self.add_num.setMinimumSize(QSize(0, 40))
        self.add_num.setMaximumSize(QSize(100, 16777215))
        self.add_num.setFont(font3)
        self.add_num.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.add_num.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.add_num, 3, 7, 1, 1)

        self.pushButton = QPushButton(self.frame_14)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(195, 23, 23);\n"
"border: 1px solid rgb(195, 23, 23);\n"
"border-radius:4px;")

        self.gridLayout_5.addWidget(self.pushButton, 1, 10, 1, 1)

        self.add_p_in = QLineEdit(self.frame_14)
        self.add_p_in.setObjectName(u"add_p_in")
        self.add_p_in.setMinimumSize(QSize(0, 40))
        self.add_p_in.setMaximumSize(QSize(100, 16777215))
        self.add_p_in.setFont(font3)
        self.add_p_in.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.add_p_in.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.add_p_in, 3, 6, 1, 1)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.gridLayout_5.addWidget(self.label_12, 2, 8, 1, 1)

        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)

        self.gridLayout_5.addWidget(self.label_19, 2, 4, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_14)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(40, 40))
        self.pushButton_14.setMaximumSize(QSize(40, 40))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../../../../../Downloads/Telegram Desktop/photo_2023-01-28_22-38-42.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QSize(40, 40))

        self.gridLayout_5.addWidget(self.pushButton_14, 3, 4, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.scrollArea_2 = QScrollArea(self.page_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_8 = QVBoxLayout(self.page_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_16 = QFrame(self.page_5)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 100))
        self.frame_16.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_16)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.color_sell_2 = QComboBox(self.frame_16)
        self.color_sell_2.setObjectName(u"color_sell_2")
        self.color_sell_2.setMinimumSize(QSize(100, 40))
        self.color_sell_2.setFont(font4)
        self.color_sell_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_sell_2.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #ced4da;\n"
"	border-radius:4px;\n"
"	padding-left:10px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/image/down.png);\n"
"	width:12;\n"
"	height12;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"QComboBox QListView{\n"
"	font-size:12;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding :5px;\n"
"	background-color:#ffffff;\n"
"	outline:0px;\n"
"}\n"
"QComboBox QListView::item{\n"
"	padding-left :10px;\n"
"	background-color:#ffffff;\n"
"	\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"	background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"	background-color:#1e90ff;\n"
"}")

        self.gridLayout_9.addWidget(self.color_sell_2, 1, 3, 1, 1)

        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.gridLayout_9.addWidget(self.label_18, 0, 3, 1, 1)

        self.search = QPushButton(self.frame_16)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(111, 40))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.search.setFont(font6)
        self.search.setCursor(QCursor(Qt.PointingHandCursor))
        self.search.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.gridLayout_9.addWidget(self.search, 1, 1, 1, 1)

        self.procut_sell_2 = QLineEdit(self.frame_16)
        self.procut_sell_2.setObjectName(u"procut_sell_2")
        self.procut_sell_2.setMinimumSize(QSize(0, 40))
        self.procut_sell_2.setMaximumSize(QSize(400, 16777215))
        self.procut_sell_2.setFont(font3)
        self.procut_sell_2.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.procut_sell_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.procut_sell_2, 1, 4, 1, 1)

        self.label_17 = QLabel(self.frame_16)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 25))
        self.label_17.setFont(font3)

        self.gridLayout_9.addWidget(self.label_17, 0, 4, 1, 1)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(300, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout_9.addWidget(self.frame_17, 1, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.scrollArea_3 = QScrollArea(self.page_5)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_8.addWidget(self.scrollArea_3)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_20 = QVBoxLayout(self.page_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_19 = QFrame(self.page_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(2, 200))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_19)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_25 = QLabel(self.frame_19)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)
        self.label_25.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_25)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 58))
        self.frame_20.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_color_btn = QPushButton(self.frame_20)
        self.add_color_btn.setObjectName(u"add_color_btn")
        self.add_color_btn.setMinimumSize(QSize(0, 40))
        self.add_color_btn.setMaximumSize(QSize(134, 16777215))
        self.add_color_btn.setFont(font6)
        self.add_color_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_color_btn.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_6.addWidget(self.add_color_btn)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_24)

        self.add_color_line = QLineEdit(self.frame_20)
        self.add_color_line.setObjectName(u"add_color_line")
        self.add_color_line.setMinimumSize(QSize(0, 40))
        self.add_color_line.setMaximumSize(QSize(350, 16777215))
        self.add_color_line.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.add_color_line)


        self.verticalLayout_16.addWidget(self.frame_20)

        self.scrollArea_5 = QScrollArea(self.frame_19)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1007, 139))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_16.addWidget(self.scrollArea_5)


        self.verticalLayout_20.addWidget(self.frame_19)

        self.frame_25 = QFrame(self.page_6)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 200))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_25)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_26 = QLabel(self.frame_25)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font3)
        self.label_26.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.label_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 58))
        self.frame_27.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.add_size_bn = QPushButton(self.frame_27)
        self.add_size_bn.setObjectName(u"add_size_bn")
        self.add_size_bn.setMinimumSize(QSize(0, 40))
        self.add_size_bn.setMaximumSize(QSize(134, 16777215))
        self.add_size_bn.setFont(font6)
        self.add_size_bn.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_size_bn.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_7.addWidget(self.add_size_bn)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_28)

        self.add_size_line = QLineEdit(self.frame_27)
        self.add_size_line.setObjectName(u"add_size_line")
        self.add_size_line.setMinimumSize(QSize(0, 40))
        self.add_size_line.setMaximumSize(QSize(350, 16777215))
        self.add_size_line.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")

        self.horizontalLayout_7.addWidget(self.add_size_line)


        self.verticalLayout_18.addWidget(self.frame_27)

        self.scrollArea_6 = QScrollArea(self.frame_25)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1007, 140))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_18.addWidget(self.scrollArea_6)


        self.verticalLayout_20.addWidget(self.frame_25)

        self.frame_18 = QFrame(self.page_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 200))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_18)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_27 = QLabel(self.frame_18)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)
        self.label_27.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_11.addWidget(self.label_27)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 58))
        self.frame_21.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.add_user = QPushButton(self.frame_21)
        self.add_user.setObjectName(u"add_user")
        self.add_user.setMinimumSize(QSize(134, 40))
        self.add_user.setMaximumSize(QSize(140, 16777215))
        self.add_user.setFont(font6)
        self.add_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_user.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_5.addWidget(self.add_user)

        self.frame_26 = QFrame(self.frame_21)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_26)

        self.checkBox = QCheckBox(self.frame_21)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(84, 32))
        self.checkBox.setMaximumSize(QSize(150, 16777215))
        self.checkBox.setFont(font3)
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.checkBox)

        self.add_pass = QLineEdit(self.frame_21)
        self.add_pass.setObjectName(u"add_pass")
        self.add_pass.setMinimumSize(QSize(100, 40))
        self.add_pass.setMaximumSize(QSize(350, 16777215))
        self.add_pass.setFont(font3)
        self.add_pass.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.add_pass)

        self.add_usr = QLineEdit(self.frame_21)
        self.add_usr.setObjectName(u"add_usr")
        self.add_usr.setMinimumSize(QSize(100, 40))
        self.add_usr.setMaximumSize(QSize(350, 16777215))
        self.add_usr.setFont(font3)
        self.add_usr.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.add_usr)


        self.verticalLayout_11.addWidget(self.frame_21)

        self.scrollArea_4 = QScrollArea(self.frame_18)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1007, 139))
        self.scrollAreaWidgetContents_4.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_11.addWidget(self.scrollArea_4)


        self.verticalLayout_20.addWidget(self.frame_18)

        self.stackedWidget_2.addWidget(self.page_6)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_25 = QVBoxLayout(self.page_9)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.page_9)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1043, 736))
        self.scrollAreaWidgetContents_8.setFont(font3)
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_35 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 200))
        self.frame_35.setMaximumSize(QSize(16777215, 200))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_35)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_72 = QFrame(self.frame_35)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMaximumSize(QSize(400, 120))
        self.frame_72.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_73 = QFrame(self.frame_72)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_73)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.label_60 = QLabel(self.frame_73)
        self.label_60.setObjectName(u"label_60")
        font7 = QFont()
        font7.setPointSize(13)
        self.label_60.setFont(font7)

        self.gridLayout_7.addWidget(self.label_60, 0, 1, 1, 1)

        self.label_56 = QLabel(self.frame_73)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font7)

        self.gridLayout_7.addWidget(self.label_56, 2, 1, 1, 1)

        self.label_57 = QLabel(self.frame_73)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)
        self.label_57.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.gridLayout_7.addWidget(self.label_57, 2, 0, 1, 1)

        self.label_61 = QLabel(self.frame_73)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font3)
        self.label_61.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.gridLayout_7.addWidget(self.label_61, 0, 0, 1, 1)


        self.horizontalLayout_31.addWidget(self.frame_73)


        self.gridLayout_17.addWidget(self.frame_72, 1, 1, 1, 1)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(400, 120))
        self.frame_37.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_37)
        self.frame_52.setObjectName(u"frame_52")
        font8 = QFont()
        font8.setPointSize(9)
        self.frame_52.setFont(font8)
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_52)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(9, 0, 9, 0)
        self.label_64 = QLabel(self.frame_52)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font7)

        self.gridLayout_8.addWidget(self.label_64, 2, 1, 1, 1)

        self.label_52 = QLabel(self.frame_52)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font7)

        self.gridLayout_8.addWidget(self.label_52, 0, 1, 1, 1)

        self.label_53 = QLabel(self.frame_52)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)
        self.label_53.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.gridLayout_8.addWidget(self.label_53, 0, 0, 1, 1)

        self.label_65 = QLabel(self.frame_52)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font3)
        self.label_65.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.gridLayout_8.addWidget(self.label_65, 2, 0, 1, 1)


        self.horizontalLayout_25.addWidget(self.frame_52)


        self.gridLayout_17.addWidget(self.frame_37, 1, 0, 1, 1)

        self.frame_76 = QFrame(self.frame_35)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_76)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 30))
        self.pushButton_10.setFont(font1)
        self.pushButton_10.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_10)

        self.frame_77 = QFrame(self.frame_76)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_37.addWidget(self.frame_77)


        self.gridLayout_17.addWidget(self.frame_76, 0, 0, 1, 1)

        self.frame_74 = QFrame(self.frame_35)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMaximumSize(QSize(400, 120))
        self.frame_74.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_75 = QFrame(self.frame_74)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_75)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.label_62 = QLabel(self.frame_75)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font7)

        self.gridLayout_6.addWidget(self.label_62, 0, 1, 1, 1)

        self.label_58 = QLabel(self.frame_75)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font7)

        self.gridLayout_6.addWidget(self.label_58, 2, 1, 1, 1)

        self.label_63 = QLabel(self.frame_75)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font3)
        self.label_63.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.gridLayout_6.addWidget(self.label_63, 0, 0, 1, 1)

        self.label_59 = QLabel(self.frame_75)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.gridLayout_6.addWidget(self.label_59, 2, 0, 1, 1)


        self.horizontalLayout_32.addWidget(self.frame_75)


        self.gridLayout_17.addWidget(self.frame_74, 1, 2, 1, 1)

        self.frame_84 = QFrame(self.frame_35)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMaximumSize(QSize(400, 120))
        self.frame_84.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:8px;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_85)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.label_67 = QLabel(self.frame_85)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font3)
        self.label_67.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.gridLayout_4.addWidget(self.label_67, 0, 0, 1, 1)

        self.label_66 = QLabel(self.frame_85)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font7)

        self.gridLayout_4.addWidget(self.label_66, 0, 1, 1, 1)

        self.label_73 = QLabel(self.frame_85)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font7)

        self.gridLayout_4.addWidget(self.label_73, 2, 1, 1, 1)

        self.label_74 = QLabel(self.frame_85)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font3)
        self.label_74.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.gridLayout_4.addWidget(self.label_74, 2, 0, 1, 1)


        self.horizontalLayout_38.addWidget(self.frame_85)


        self.gridLayout_17.addWidget(self.frame_84, 1, 3, 1, 1)

        self.label_68 = QLabel(self.frame_35)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(16777215, 25))
        font9 = QFont()
        font9.setFamilies([u"Simplified Arabic"])
        font9.setPointSize(15)
        font9.setBold(False)
        self.label_68.setFont(font9)

        self.gridLayout_17.addWidget(self.label_68, 0, 3, 1, 1)

        self.color_sell_5 = QComboBox(self.frame_35)
        self.color_sell_5.addItem("")
        self.color_sell_5.addItem("")
        self.color_sell_5.addItem("")
        self.color_sell_5.addItem("")
        self.color_sell_5.addItem("")
        self.color_sell_5.setObjectName(u"color_sell_5")
        self.color_sell_5.setMinimumSize(QSize(100, 40))
        self.color_sell_5.setFont(font4)
        self.color_sell_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_sell_5.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #ced4da;\n"
"	border-radius:4px;\n"
"	padding-left:10px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/image/down.png);\n"
"	width:12;\n"
"	height12;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"QComboBox QListView{\n"
"	font-size:12;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding :5px;\n"
"	background-color:#ffffff;\n"
"	outline:0px;\n"
"}\n"
"QComboBox QListView::item{\n"
"	padding-left :10px;\n"
"	background-color:#ffffff;\n"
"	\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"	background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"	background-color:#1e90ff;\n"
"}")

        self.gridLayout_17.addWidget(self.color_sell_5, 0, 2, 1, 1)

        self.frame_38 = QFrame(self.frame_35)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(12, 0, 12, 0)
        self.label_21 = QLabel(self.frame_38)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font7)
        self.label_21.setStyleSheet(u"color: rgb(35, 158, 86);")

        self.horizontalLayout_11.addWidget(self.label_21)

        self.label_20 = QLabel(self.frame_38)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font7)

        self.horizontalLayout_11.addWidget(self.label_20)


        self.gridLayout_17.addWidget(self.frame_38, 0, 1, 1, 1)


        self.verticalLayout_23.addWidget(self.frame_35)

        self.frame_56 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(0, 30))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(770, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_8)

        self.frame_60 = QFrame(self.frame_56)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(16777215, 40))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.button_patiensts_8 = QRadioButton(self.frame_60)
        self.button_patiensts_8.setObjectName(u"button_patiensts_8")
        self.button_patiensts_8.setMinimumSize(QSize(115, 38))
        self.button_patiensts_8.setMaximumSize(QSize(14566, 38))
        self.button_patiensts_8.setFont(font2)
        self.button_patiensts_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts_8.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts_8.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"\n"
"border : none ;\n"
"padding-left : 0px;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.8);\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton:checked{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"background-color :  rgb(0, 0, 0);\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts_8.setIconSize(QSize(30, 30))
        self.button_patiensts_8.setChecked(True)

        self.horizontalLayout_26.addWidget(self.button_patiensts_8)

        self.button_patiensts_9 = QRadioButton(self.frame_60)
        self.button_patiensts_9.setObjectName(u"button_patiensts_9")
        self.button_patiensts_9.setMinimumSize(QSize(115, 38))
        self.button_patiensts_9.setMaximumSize(QSize(14566, 38))
        self.button_patiensts_9.setFont(font2)
        self.button_patiensts_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts_9.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts_9.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"border : none ;\n"
"padding-left : 0px;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.8);\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton:checked{\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"background-color :  rgb(0, 0, 0);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts_9.setIconSize(QSize(30, 30))
        self.button_patiensts_9.setChecked(False)

        self.horizontalLayout_26.addWidget(self.button_patiensts_9)


        self.horizontalLayout_27.addWidget(self.frame_60)


        self.verticalLayout_23.addWidget(self.frame_56)

        self.stackedWidget_4 = QStackedWidget(self.scrollAreaWidgetContents_8)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_34 = QVBoxLayout(self.page_10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.color_sell_6 = QComboBox(self.page_10)
        self.color_sell_6.addItem("")
        self.color_sell_6.addItem("")
        self.color_sell_6.addItem("")
        self.color_sell_6.addItem("")
        self.color_sell_6.setObjectName(u"color_sell_6")
        self.color_sell_6.setMinimumSize(QSize(100, 40))
        self.color_sell_6.setMaximumSize(QSize(300, 16777215))
        self.color_sell_6.setFont(font4)
        self.color_sell_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.color_sell_6.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid #ced4da;\n"
"	border-radius:4px;\n"
"	padding-left:10px;\n"
"}\n"
"QComboBox::drop-down{\n"
"	border:0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"	image: url(:/image/down.png);\n"
"	width:12;\n"
"	height12;\n"
"	margin-right:15px;\n"
"}\n"
"\n"
"QComboBox:on{\n"
"	border: 4px solid #c2dbfe;\n"
"}\n"
"QComboBox QListView{\n"
"	font-size:12;\n"
"	border:1px solid rgba(0,0,0,10%);\n"
"	padding :5px;\n"
"	background-color:#ffffff;\n"
"	outline:0px;\n"
"}\n"
"QComboBox QListView::item{\n"
"	padding-left :10px;\n"
"	background-color:#ffffff;\n"
"	\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"	background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"	background-color:#1e90ff;\n"
"}")

        self.verticalLayout_34.addWidget(self.color_sell_6)

        self.frame_36 = QFrame(self.page_10)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_36)
        self.gridLayout_19.setObjectName(u"gridLayout_19")

        self.verticalLayout_34.addWidget(self.frame_36)

        self.stackedWidget_4.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_43 = QVBoxLayout(self.page_11)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_64 = QFrame(self.page_11)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(2, 200))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_64)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_67 = QFrame(self.frame_64)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(0, 25))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_87 = QLabel(self.frame_67)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font3)
        self.label_87.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_29.addWidget(self.label_87)

        self.label_86 = QLabel(self.frame_67)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMaximumSize(QSize(137, 16777215))
        self.label_86.setFont(font3)
        self.label_86.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_29.addWidget(self.label_86)


        self.verticalLayout_35.addWidget(self.frame_67)

        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(0, 58))
        self.frame_65.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.add_color_btn_2 = QPushButton(self.frame_65)
        self.add_color_btn_2.setObjectName(u"add_color_btn_2")
        self.add_color_btn_2.setMinimumSize(QSize(0, 40))
        self.add_color_btn_2.setMaximumSize(QSize(134, 16777215))
        self.add_color_btn_2.setFont(font6)
        self.add_color_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_color_btn_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color:rgb(202, 39, 24);\n"
"	border: 2px solid  rgb(202, 39, 24);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(202, 39, 24);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout_28.addWidget(self.add_color_btn_2)

        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_28.addWidget(self.frame_66)

        self.add_color_line_3 = QLineEdit(self.frame_65)
        self.add_color_line_3.setObjectName(u"add_color_line_3")
        self.add_color_line_3.setMinimumSize(QSize(0, 40))
        self.add_color_line_3.setMaximumSize(QSize(523, 16777215))
        self.add_color_line_3.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")

        self.horizontalLayout_28.addWidget(self.add_color_line_3)

        self.add_color_line_2 = QLineEdit(self.frame_65)
        self.add_color_line_2.setObjectName(u"add_color_line_2")
        self.add_color_line_2.setMinimumSize(QSize(0, 40))
        self.add_color_line_2.setMaximumSize(QSize(120, 16777215))
        self.add_color_line_2.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")

        self.horizontalLayout_28.addWidget(self.add_color_line_2)


        self.verticalLayout_35.addWidget(self.frame_65)

        self.scrollArea_8 = QScrollArea(self.frame_64)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 989, 349))
        self.verticalLayout_42 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_35.addWidget(self.scrollArea_8)


        self.verticalLayout_43.addWidget(self.frame_64)

        self.stackedWidget_4.addWidget(self.page_11)

        self.verticalLayout_23.addWidget(self.stackedWidget_4)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_25.addWidget(self.scrollArea_7)

        self.stackedWidget_2.addWidget(self.page_9)

        self.horizontalLayout_4.addWidget(self.stackedWidget_2)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(250, 0))
        self.frame_8.setMaximumSize(QSize(250, 16777215))
        self.frame_8.setStyleSheet(u"background-color: rgb(43, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border:0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_8)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_8)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 40))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.button_patiensts_4 = QRadioButton(self.frame_31)
        self.button_patiensts_4.setObjectName(u"button_patiensts_4")
        self.button_patiensts_4.setMinimumSize(QSize(0, 38))
        self.button_patiensts_4.setMaximumSize(QSize(14566, 38))
        self.button_patiensts_4.setFont(font2)
        self.button_patiensts_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts_4.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts_4.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color :  transparent;\n"
"border : none ;\n"
"padding-left : 0px;\n"
"color : white;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.1);\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts_4.setIconSize(QSize(30, 30))
        self.button_patiensts_4.setChecked(False)

        self.horizontalLayout_8.addWidget(self.button_patiensts_4)

        self.button_patiensts_5 = QRadioButton(self.frame_31)
        self.button_patiensts_5.setObjectName(u"button_patiensts_5")
        self.button_patiensts_5.setMinimumSize(QSize(0, 38))
        self.button_patiensts_5.setMaximumSize(QSize(14566, 38))
        self.button_patiensts_5.setFont(font2)
        self.button_patiensts_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_patiensts_5.setLayoutDirection(Qt.LeftToRight)
        self.button_patiensts_5.setStyleSheet(u"\n"
"QRadioButton{ \n"
"background-color :  transparent;\n"
"border : 0px ;\n"
"padding-left : 0px;\n"
"color : white;\n"
"font-family: 'Poppins';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 18px;\n"
" }\n"
"\n"
"QRadioButton:hover{\n"
"background: rgba(0, 0, 0, 0.1);\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"background-color : rgb(255, 255, 255) ;\n"
"color: rgb(0, 0, 0);\n"
"border : 0px ;\n"
"border-bottom-right-radius: 20px;\n"
"\n"
"\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"width: 0px;\n"
"height: 0px;\n"
"border-radius: 0px;\n"
" }")
        self.button_patiensts_5.setIconSize(QSize(30, 30))
        self.button_patiensts_5.setChecked(True)

        self.horizontalLayout_8.addWidget(self.button_patiensts_5)


        self.verticalLayout_21.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_8)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_32)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.frame_32)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_38 = QVBoxLayout(self.page_7)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.frame_81 = QFrame(self.page_7)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_81)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.scrollArea_9 = QScrollArea(self.frame_81)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setStyleSheet(u"QScrollBar:vertical{\n"
"	border: none;\n"
"	background-color: rgb(181, 196, 232);\n"
"	width: 14px;	\n"
"	margin: 15px 0px 15px 0px;\n"
"	border-radius:0px;\n"
"}\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(145, 145, 145);\n"
"	min-height:30px;\n"
"	border-radius:7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-top-left-radius: 6px;\n"
"	border-top-right-radius: 6px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"\n"
"	border:none;\n"
"	background-color: rgb(194, 194, 194);\n"
"	height:14px;\n"
"	border-bottom"
                        "-left-radius: 6px;\n"
"	border-bottom-right-radius: 6px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin:margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"background-color: rgb(134, 134, 134);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"	background-color: rgb(1, 13, 89);\n"
"}\n"
"QScrollBar::up-arrow::vertical, QScrollBar::down-arrow:vertical{\n"
"	border:none\n"
"}\n"
"QScrollBar::add-page::vertical, QScrollBar::sub-page:vertical{\n"
"	border:none\n"
"}\n"
"")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 214, 406))
        self.verticalLayout_44 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_45.addWidget(self.scrollArea_9)

        self.pushButton_13 = QPushButton(self.frame_81)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMaximumSize(QSize(16777215, 30))
        self.pushButton_13.setFont(font7)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"color: rgb(230, 126, 34);")

        self.verticalLayout_45.addWidget(self.pushButton_13)


        self.verticalLayout_38.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.page_7)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMaximumSize(QSize(16777215, 250))
        font10 = QFont()
        font10.setPointSize(10)
        self.frame_82.setFont(font10)
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_82)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_83 = QLabel(self.frame_82)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font3)

        self.gridLayout_20.addWidget(self.label_83, 1, 2, 1, 1)

        self.label_85 = QLabel(self.frame_82)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font3)
        self.label_85.setCursor(QCursor(Qt.ArrowCursor))

        self.gridLayout_20.addWidget(self.label_85, 0, 2, 1, 1)

        self.label_82 = QLabel(self.frame_82)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font3)

        self.gridLayout_20.addWidget(self.label_82, 2, 1, 1, 1)

        self.label_54 = QLabel(self.frame_82)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font3)

        self.gridLayout_20.addWidget(self.label_54, 4, 1, 1, 1)

        self.label_55 = QLabel(self.frame_82)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)

        self.gridLayout_20.addWidget(self.label_55, 4, 2, 1, 1)

        self.label_81 = QLabel(self.frame_82)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font3)

        self.gridLayout_20.addWidget(self.label_81, 2, 2, 1, 1)

        self.label_75 = QLabel(self.frame_82)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font3)

        self.gridLayout_20.addWidget(self.label_75, 3, 2, 1, 1)

        self.label_80 = QLabel(self.frame_82)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font3)

        self.gridLayout_20.addWidget(self.label_80, 3, 1, 1, 1)

        self.label_84 = QLabel(self.frame_82)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font3)

        self.gridLayout_20.addWidget(self.label_84, 1, 1, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_82)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(16777215, 30))
        self.pushButton_11.setFont(font7)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"color: rgb(230, 126, 34);")

        self.gridLayout_20.addWidget(self.pushButton_11, 5, 1, 1, 2)


        self.verticalLayout_38.addWidget(self.frame_82)

        self.stackedWidget_3.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.gridLayout_21 = QGridLayout(self.page_8)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.frame_83 = QFrame(self.page_8)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.pushButton_12 = QPushButton(self.frame_83)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(10, 40, 101, 41))
        self.pushButton_12.setMinimumSize(QSize(0, 30))
        self.pushButton_12.setFont(font1)
        self.pushButton_12.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(35, 158, 86);\n"
"	border: 2px solid  rgb(35, 158, 86);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color: rgb(35, 158, 86);\n"
"	\n"
"	color: #fff;\n"
"}")
        self.addToCart_3 = QPushButton(self.frame_83)
        self.addToCart_3.setObjectName(u"addToCart_3")
        self.addToCart_3.setGeometry(QRect(130, 40, 99, 40))
        self.addToCart_3.setMinimumSize(QSize(99, 40))
        self.addToCart_3.setMaximumSize(QSize(200, 16777215))
        self.addToCart_3.setFont(font1)
        self.addToCart_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.addToCart_3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(230, 126, 34);\n"
"	border: 2px solid  rgb(230, 126, 34);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color:rgb(230, 126, 34);\n"
"	\n"
"	color: #fff;\n"
"}")
        self.label_88 = QLabel(self.frame_83)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(110, 10, 101, 18))
        self.label_88.setFont(font4)

        self.gridLayout_21.addWidget(self.frame_83, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_8)

        self.verticalLayout_22.addWidget(self.stackedWidget_3)

        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 50))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.addToCart_2 = QPushButton(self.frame_33)
        self.addToCart_2.setObjectName(u"addToCart_2")
        self.addToCart_2.setGeometry(QRect(60, 10, 141, 40))
        self.addToCart_2.setMinimumSize(QSize(99, 40))
        self.addToCart_2.setMaximumSize(QSize(200, 16777215))
        self.addToCart_2.setFont(font1)
        self.addToCart_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.addToCart_2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(255, 54, 28);\n"
"	border: 2px solid  rgb(255, 54, 28);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color:rgb(255, 54, 28);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.verticalLayout_22.addWidget(self.frame_33)


        self.verticalLayout_21.addWidget(self.frame_32)


        self.horizontalLayout_4.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 28))
        self.frame_4.setStyleSheet(u"background-color: rgb(43, 47, 51);\n"
"color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 5, 9, 6)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.feedback = QLabel(self.frame_4)
        self.feedback.setObjectName(u"feedback")

        self.horizontalLayout.addWidget(self.feedback)

        self.horizontalSpacer = QSpacerItem(0, 11, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_23.setText("")
        self.username_3.setText("")
        self.username_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_24.setText("")
        self.password_3.setText("")
        self.password_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signIn.setText(QCoreApplication.translate("MainWindow", u"SIGN IN", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.pushButton_2.setText("")
        self.button_patiensts_7.setText(QCoreApplication.translate("MainWindow", u"   \u0627\u062d\u0635\u0627\u0626\u064a\u0627\u062a", None))
        self.button_patiensts_6.setText(QCoreApplication.translate("MainWindow", u"    \u0627\u0644\u0627\u0639\u062f\u0627\u062f\u0627\u062a", None))
        self.button_patiensts_2.setText(QCoreApplication.translate("MainWindow", u"     \u0627\u0644\u0645\u0628\u064a\u0639\u0627\u062a", None))
        self.button_patiensts_3.setText(QCoreApplication.translate("MainWindow", u"    \u0627\u0644\u0645\u062e\u0632\u0646", None))
        self.button_patiensts.setText(QCoreApplication.translate("MainWindow", u"       \u0627\u0644\u0628\u064a\u0639", None))
        self.pushButton_9.setText("")
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b \u0627\u0644\u0627\u0633\u0645", None))
        self.procut_sell.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u062f\u062f", None))
        self.num_sell.setText("")
        self.addToCart.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062f\u062e\u0627\u0644", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0645\u0642\u0627\u0633", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0644\u0648\u0646", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0639\u0631 \u0627\u0644\u0642\u0637\u0639\u0629", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0631\u0627\u0628\u0637 (\u0627\u062e\u062a\u064a\u0627\u0631\u064a)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0642\u0645 \u0627\u0644\u062a\u064a\u0644\u0641\u0648\u0646 (\u0627\u062e\u062a\u064a\u0627\u0631\u064a)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0639\u0645\u064a\u0644 (\u0627\u062e\u062a\u064a\u0627\u0631\u064a)", None))
        self.final_price.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clientname.setText("")
        self.done_sell.setText(QCoreApplication.translate("MainWindow", u"  \u0627\u062a\u0645\u0627\u0645 \u0627\u0644\u0639\u0645\u0644\u064a\u0629  ", None))
        self.enter_store.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0633\u0645", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0639\u0631 \u0627\u0644\u0628\u064a\u0639 ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0633\u0639\u0631 \u0627\u0644\u0634\u0631\u0627\u0621", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0639\u062f\u062f", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0627\u0644\u0648\u0627\u0646", None))
        self.add_num.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0639\u0627\u062f\u0629 \u0627\u062f\u062e\u0627\u0644", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u0631 \u0627\u0644\u0645\u0642\u0627\u0633\u0627\u062a", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u0631 \u0635\u0648\u0631\u0629", None))
        self.pushButton_14.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0627\u062e\u062a\u0631 \u062e\u0627\u0646\u0629 \u0627\u0644\u0628\u062d\u062b", None))
        self.search.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0628\u062d\u062b", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"   \u0627\u0644\u0627\u0644\u0648\u0627\u0646  ", None))
        self.add_color_btn.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0647 \u0644\u0648\u0646", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"   \u0627\u0644\u0645\u0642\u0627\u0633\u0627\u062a", None))
        self.add_size_bn.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0645\u0642\u0627\u0633", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"   \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645\u0648\u0646", None))
        self.add_user.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 \u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.add_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0643\u0644\u0645\u0629 \u0627\u0644\u0645\u0631\u0648\u0631", None))
        self.add_usr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0633\u0645 \u0627\u0644\u0645\u0633\u062a\u062e\u062f\u0645", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0628\u064a\u0639 \u0627\u0644\u0641\u0639\u0644\u064a", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0643\u0633\u0628 \u0627\u0644\u0641\u0639\u0644\u064a", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0642\u0637\u0639", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u0648\u0631\u062f\u0627\u0631\u0627\u062a", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062d\u062f\u064a\u062b", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0628\u064a\u0639 \u0627\u0644\u0645\u062a\u0648\u0642\u0639", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0643\u0633\u0628 \u0627\u0644\u0645\u062a\u0648\u0642\u0639", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u062f\u0641\u0648\u0639 (\u0645\u0646 \u0631\u0627\u0633 \u0627\u0644\u0645\u0627\u0644):", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0635\u0631\u0648\u0641\u0627\u062a", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0627\u062d\u0635\u0627\u0621\u0627\u062a", None))
        self.color_sell_5.setItemText(0, QCoreApplication.translate("MainWindow", u"Today", None))
        self.color_sell_5.setItemText(1, QCoreApplication.translate("MainWindow", u"last 7 days", None))
        self.color_sell_5.setItemText(2, QCoreApplication.translate("MainWindow", u"last 30 days", None))
        self.color_sell_5.setItemText(3, QCoreApplication.translate("MainWindow", u"last year", None))
        self.color_sell_5.setItemText(4, QCoreApplication.translate("MainWindow", u"all the time", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0635\u0627\u0641\u064a \u0627\u0644\u0631\u0628\u062d", None))
        self.button_patiensts_8.setText(QCoreApplication.translate("MainWindow", u"    Charts", None))
        self.button_patiensts_9.setText(QCoreApplication.translate("MainWindow", u"  outCome", None))
        self.color_sell_6.setItemText(0, "")
        self.color_sell_6.setItemText(1, QCoreApplication.translate("MainWindow", u"Orders", None))
        self.color_sell_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Sales", None))
        self.color_sell_6.setItemText(3, QCoreApplication.translate("MainWindow", u"Income", None))

        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u0641\u064a\u0645\u0627 \u0635\u0631\u0641", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0635\u0631\u0648\u0641", None))
        self.add_color_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0636\u0627\u0641\u0629 ", None))
        self.button_patiensts_4.setText(QCoreApplication.translate("MainWindow", u"      \u0627\u0639\u062f\u0627\u062f\u0627\u062a", None))
        self.button_patiensts_5.setText(QCoreApplication.translate("MainWindow", u"  \u0627\u0644\u062c\u0631\u062f/\u0627\u0644\u064a\u0648\u0645\u064a\u0629", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062d\u062f\u064a\u062b", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"\u0639\u062f\u062f \u0627\u0644\u0642\u0637\u0639", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u062c\u0631\u062f.", None))
        self.label_82.setText("")
        self.label_54.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0645\u0643\u0633\u0628 \u0627\u0644\u0645\u062a\u0648\u0642\u0639", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0645\u0648\u0639 \u0633\u0639\u0631 \u0627\u0644\u0634\u0631\u0627\u0621", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u0645\u062c\u0645\u0648\u0639 \u0633\u0639\u0631 \u0627\u0644\u0628\u064a\u0639", None))
        self.label_80.setText("")
        self.label_84.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u062a\u062d\u062f\u064a\u062b", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Download ", None))
        self.addToCart_3.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u0642\u0627\u0639\u062f\u0629 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a", None))
        self.addToCart_2.setText(QCoreApplication.translate("MainWindow", u"\u062a\u0633\u062c\u064a\u0644 \u062e\u0631\u0648\u062c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Created by MgA", None))
        self.feedback.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Brova v 0.0.2", None))
    # retranslateUi

