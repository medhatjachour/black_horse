# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_sizeDEGkKv.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import ( QMetaObject,  QSize, Qt)
from PySide6.QtGui import (QCursor, QFont)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)

from orm import services as _services
from orm import database as _database
class SizeAndColor(QFrame):
    def __init__(
        self,
        id,
        name,
        _type,
        _disc = None,
        _date = None,
    ):
        super().__init__()
        self._id = id
        self._name = name
        self._type = _type
        self.setObjectName("Form")
        self.resize(649, 48)
        self.setMaximumHeight(45)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame.setStyleSheet(u"\n"
"QFrame{ \n"
"background-color: rgb(255, 255, 255);\n"
# "border-top: 1px solid rgb(191, 191, 191);\n"
"border-bottom: 1px solid rgb(191, 191, 191);\n"
" }\n"
"\n"
"QFrame:hover{\n"
"\n"
"background-color: rgb(242, 248, 255);\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 0, 3)
        self.deleteItem = QPushButton(self.frame)
        self.deleteItem.setObjectName(u"deleteItem")
        self.deleteItem.setMinimumSize(QSize(99, 40))
        self.deleteItem.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.deleteItem.setFont(font)
        self.deleteItem.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteItem.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:0px;\n"
"	color: rgb(231, 47, 34);\n"
"	background-color:rgb(255, 255, 255);\n"
# "	border: 2px solid  rgb(231, 47, 34);\n"
"	border-radius:5px\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:0px;\n"
"	background-color:rgb(231, 47, 34);\n"
"	\n"
"	color: #fff;\n"
"}")

        self.horizontalLayout.addWidget(self.deleteItem)

        self.Change = QPushButton(self.frame)
        self.Change.setObjectName(u"Change")
        self.Change.setMinimumSize(QSize(99, 40))
        self.Change.setMaximumSize(QSize(200, 16777215))
        self.Change.setFont(font)
        self.Change.setCursor(QCursor(Qt.PointingHandCursor))
        self.Change.setStyleSheet(u"QPushButton\n"
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

        self.horizontalLayout.addWidget(self.Change)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 0))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 0))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"\n"
"background-color: transparent;\n"
"border:0px;/*\n"
"QLabel{\n"
"border:0px;\n"
"}\n"
"QLabel:hover{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"*/")
        self.label.setAlignment(Qt.AlignCenter)



        self.verticalLayout.addWidget(self.frame)



        self.label_disc = QLabel(self.frame)
        self.label_disc.setObjectName(u"label_disc")
        self.label_disc.setMinimumSize(QSize(200, 0))
        self.label_disc.setFont(font1)
        self.label_disc.setStyleSheet(u"\n"
"background-color: transparent;\n"
"border:0px;/*\n"
"QLabel{\n"
"border:0px;\n"
"}\n"
"QLabel:hover{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"*/")
        self.label_disc.setAlignment(Qt.AlignCenter)
        self.label_disc.setVisible(False)
        self.label_disc.setText(_disc)


        self.label_date = QLabel(self.frame)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMinimumSize(QSize(200, 0))
        self.label_date.setFont(font1)
        self.label_date.setStyleSheet(u"\n"
"background-color: transparent;\n"
"border:0px;/*\n"
"QLabel{\n"
"border:0px;\n"
"}\n"
"QLabel:hover{\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"*/")
        self.label_date.setAlignment(Qt.AlignCenter)
        self.label_date.setVisible(False)
        self.label_date.setText( str(_date) )


        self.horizontalLayout.addWidget(self.label_date)
        self.horizontalLayout.addWidget(self.label_disc)
        self.horizontalLayout.addWidget(self.label)

        self.label.setText(str(self._name))
        self.deleteItem.setText("حذف")

        QMetaObject.connectSlotsByName(self)
        if self._type == "size":
            self.deleteItem.clicked.connect(self.deleteSizeFun)
            self.Change.setVisible(False)
        if self._type == "color":
            self.Change.setVisible(False)
            self.deleteItem.clicked.connect(self.deleteColorFun)
        if self._type == "user":
            self.Change.setVisible(False)
            self.deleteItem.clicked.connect(self.deleteUserFun)
        if self._type == "output":
            self.Change.setVisible(False)
            self.deleteItem.setVisible(False)
            self.label_disc.setVisible(True)
            self.label_date.setVisible(True)
        if self._type == "cat":
            self.Change.setVisible(False)
            self.deleteItem.clicked.connect(self.deleteCatFun)
        if self._type == "store":
            self.Change.setVisible(False)
            self.label_disc.setVisible(True)
            self.label_date.setVisible(True)
            self.deleteItem.clicked.connect(self.deleteStoreFun)

    def deleteSizeFun(self):
        deleted_size = _services.delete_size( _database.SessionLocal(),self._id )
        # if deleted_size:
        self.setVisible(False)
    def deleteColorFun(self):
        deleted_color = _services.delete_color( _database.SessionLocal(),self._id )
        # if deleted_color:
        self.setVisible(False)
    def deleteUserFun(self):
        deleted_user = _services.delete_user( _database.SessionLocal(),self._id )
        # if deleted_user:
        self.setVisible(False)
    def deleteCatFun(self):
        deleted_user = _services.delete_cat( _database.SessionLocal(),self._id )
        # if deleted_user:
        self.setVisible(False)
    def deleteStoreFun(self):
        deleted_user = _services.delete_store( _database.SessionLocal(),self._id )
        # if deleted_user:
        self.setVisible(False)



    # setupUi

