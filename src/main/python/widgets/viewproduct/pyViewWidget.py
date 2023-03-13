# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designereNptSc.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QWidget)
class PyViewBox(QDialog):
    def __init__(
        self,
        width = 500,
        height = 306,
        icon = None,
        name= "  "
    ):
        super().__init__()
        self.resize(width, height)
        self.setMaximumSize(1080,720)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.imagelabel = QLabel(self)
        self.imagelabel.setObjectName(u"imagelabel")
        if icon:
            self.imagelabel.setPixmap(QPixmap(icon))
            self.imagelabel.setScaledContents(True)

        self.gridLayout.addWidget(self.imagelabel, 1, 0, 1, 1)

        self.name = QLabel(self)
        self.name.setObjectName(u"name")
        self.name.setMaximumSize(QSize(16777215, 50))
        self.name.setText(name)
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)

        self.imagelabel.setMaximumSize(1080,720)
        QMetaObject.connectSlotsByName(self)
        self.exec_()
    # setupUi
