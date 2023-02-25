# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'childUQHYKA.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QPushButton, QSizePolicy, QWidget)
class PY_TreeChild(QFrame):
    def __init__(
        self,
        # id,
        data,
        data_b,
        type=None,
    ):
        super().__init__()
        # self._id = id
        self._data = data
        self._data_b = data_b
        self.resize(395, 35)
        self.setMinimumSize(QSize(0, 30))
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setStyleSheet(u"QFrame{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QFrame::hover{\n"
"\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(8, 0, 8, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border:none;")

        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border:none;")
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 12))
        self.pushButton_3.setMaximumSize(QSize(12, 12))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border:none;\n"
"background-color: rgb(68, 203, 99);")

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)



        self.pushButton.setText("properties")
        self.pushButton_2.setText("name")
        self.isChecked = False
        QMetaObject.connectSlotsByName(self)
        if type == 1:
            self.setStyleSheet("padding-left:25px;\n")
            self.pushButton_2.setText(str(self._data))
            self.pushButton.setText(str(self._data_b))
        if type == 2:
            self.setStyleSheet("padding-left:50px;\n")
        if type == 0:
            self.setStyleSheet("padding-left:0px;\n")
            self.pushButton_3.setVisible(False)
        self.pushButton_3.clicked.connect(self.checkIt)
        self.pushButton_2.clicked.connect(self.checkIt)
        self.pushButton.clicked.connect(self.checkIt)
    def isActivated(self):
        return self.isChecked
    def checkIt(self):
        
        if self.isChecked:
            self.setStyleSheet("padding-left:50px;\n")
            self.frame.setStyleSheet(u"QFrame{\n"
                "border:2px solid transparent;\n"
                "border-radius: 8px;\n"
                "background-color: rgb(242, 248, 255);\n"
                "}\n"
                "QFrame::hover{\n"
                "\n"
                "	border: 2px solid rgb(103, 222, 255);\n"
                "}\n"
                )
        else:

            self.setStyleSheet("padding-left:0px;\n")
            self.frame.setStyleSheet(u"QFrame{\n"
                "border:2px solid transparent;\n"
                "border-radius: 8px;\n"
                "	border: 2px solid rgb(103, 222, 255);\n"
                "background-color: rgb(242, 248, 255);\n"
                "}\n"
                "QFrame::hover{\n"
                "\n"
                "	border: 2px solid rgb(103, 222, 255);\n"
                "}\n"
                )
        self.isChecked = not self.isChecked