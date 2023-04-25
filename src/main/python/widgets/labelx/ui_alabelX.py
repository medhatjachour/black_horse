# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'alabeluvXAoTM.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy,QHBoxLayout, QVBoxLayout, QWidget)
# from app import MainWindow as main
class aLabelX(QFrame):
    def __init__(
        self,
        text,
        _type,
        _date = "",
    ):
        super().__init__()
        self._text = text
        self._type = _type
        self._date = _date

        self.resize(94, 22)
        self.setMinimumSize(QSize(0, 21))
        self.setMaximumSize(QSize(16777215, 22))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 22))
        self.frame_34.setMaximumSize(QSize(16777215, 30))
        self.frame_34.setStyleSheet(u"border-bottom:1px solid  rgb(195, 195, 195);\n"
"background-color: rgb(242, 248, 255);")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_34)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 0, 3)
        self.label_19 = QLabel(self.frame_34)
        self.label_19.setObjectName(u"label_19")
        # self.label_19.setGeometry(QRect(0, 0, 120, 20))
        self.label_19.setStyleSheet(u"border:0px;")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.pushButton_9 = QPushButton(self.frame_34)
        self.pushButton_9.setObjectName(u"pushButton_9")
        # self.pushButton_9.setGeometry(QRect(-2, -2, 15, 15))
        self.pushButton_9.setGeometry(QRect(0, 0, 0, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"border:none")

        self.verticalLayout.addWidget(self.frame_34)

        self.label_199 = QLabel(self.frame_34)
        self.label_199.setObjectName(u"label_199")
        # self.label_199.setGeometry(QRect(0, 0, 120, 20))
        self.label_199.setStyleSheet(u"border:0px;")
        self.label_199.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label_199)
        self.label_199.setVisible(False)

        QMetaObject.connectSlotsByName(self)
        self.horizontalLayout.addWidget(self.label_19)
        self.label_19.setText(str(self._text))
        if self._type == "check":

            self.label_199.setVisible(True)
            self.label_199.setText(str(self._date))

        # self.pushButton_9.setText("X")
    #     if self._type == "color":
    #         self.pushButton_9.clicked.connect(self.removeColor)
    #     if self._type == "size":
    #         self.pushButton_9.clicked.connect(self.removeSize)
    # def removeColor(self):
    #     self.setVisible(False)
    #     return self._type, self._text
    #     # main.removeColorAndWidgets(main,self._type, self._text)
    # def removeSize(self):
    #     self.setVisible(False)
    #     return self._type, self._text
        # main.removeColorAndWidgets(main,self._type, self._text)

