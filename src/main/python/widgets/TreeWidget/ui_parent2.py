# -*- coding: utf-8 -*-

################################################################################
## self generated from reading UI file 'parentBLCiTO.ui'
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
    QPalette, QPixmap, QRadialGradient)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from ui_child import PY_TreeChild
class PY_TreeParent2(QFrame):
    def __init__(
        self,
        theId,
        data,
    ):
        super().__init__()
        self._id = theId
        self._data = data

        self.resize(395, 30)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setStyleSheet(u"QFrame{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding-left: 25px;\n"
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
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(8, 0, 8, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border:none; ")
        icon = QIcon()
        icon.addFile(u"close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border:none;text-align:left;")
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        QMetaObject.connectSlotsByName(self)
        
        self.theKey = [*self._data.keys()][self._id]
        self.pushButton_2.setText(str(self.theKey))
        
        self.isShown = True
        self.pushButton.clicked.connect(self.showChild)
        self.pushButton_2.clicked.connect(self.showChild)
        self.childs = []
        # self.showChild()
    # /////////////////////////////////////////////////////////// clearing taps

    def clear_tab_except_first(self, layout):
        for i in range(layout.count() - 1):
            child = layout.takeAt(1)
            if child.widget():
                child.widget().deleteLater()
        self.childs = []

    def showChild(self):
        self.clear_tab_except_first(self.verticalLayout)
        if self.isShown:
            for i in self._data[self.theKey]:
                if type(self._data[self.theKey][i]) == str:
                    self.child = PY_TreeChild(self._data[self.theKey][i],"bb",2)
                    self.childs.append(self.child)
                    self.verticalLayout.addWidget(self.child)
                elif type(self._data[self.theKey][i]) == dict:
                    pass
            icon = QIcon()
            icon.addFile(u"close.png", QSize(), QIcon.Normal, QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QSize(30, 30))
        else:
            icon = QIcon()
            icon.addFile(u"open.png", QSize(), QIcon.Normal, QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QSize(30, 30))
        self.isShown = not self.isShown