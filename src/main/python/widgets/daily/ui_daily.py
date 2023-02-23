# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dailyAEqncu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Daily(QFrame):
    def __init__(
        self,
        id,
        name,
        _type,
        _date ,
        _disc = None,
    ):
        super().__init__()
        self._id = id
        self._name = name
        self._type = _type
        self.resize(216, 43)
        self.setMaximumSize(QSize(231, 43))
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgb(33, 149, 79);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setMaximumWidth(100)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame)

        QMetaObject.connectSlotsByName(self)
        if self._type == "dailyOut":
            self.frame.setStyleSheet(u"color: #f00000;")
            self.label.setText(str(self._name))
            self.label_2.setText(str(_disc))
            self.label_3.setText(str(_date.strftime("%I:%M %p")))
        if self._type == "dailyIn":
            self.frame.setStyleSheet(u"color: #30af43;")
            self.label.setText(str(self._name))
            self.label_2.setText(str(_disc))
            self.label_3.setText(str(_date.strftime("%I:%M %p")))

    # retranslateUi

