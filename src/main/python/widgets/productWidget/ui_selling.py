# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sellingAsBvAw.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,QRegularExpression,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,QRegularExpressionValidator,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from orm import services as _services
from orm import database as _database

class ProductWidget(QFrame):
    def __init__(
        self,
        _id,
        name,
        size,
        color,
        num,
        priceIn,
        priceOut,
        _type,
    ):
        super().__init__()
        self._id = _id
        self._name = name
        self._size = size
        self._color = color
        self._num = num
        self._priceIn = priceIn
        self._priceOut = priceOut
        self._type = _type
        self.setObjectName("self")
        self.resize(812, 50)
        self.setMaximumHeight(50)
        self.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
"	border: 2px solid  transparent;\n"
"	background-color: transparent;\n"
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
"	border: 2px solid  transparent;\n"
"	background-color: transparent;\n"
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

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_2)

        font1 = QFont()
        font1.setPointSize(11)

        self.num_sell_2 = QLineEdit(self.frame)
        self.num_sell_2.setObjectName(u"num_sell_2")
        self.num_sell_2.setMinimumSize(QSize(0, 40))
        self.num_sell_2.setMaximumSize(QSize(100, 16777215))
        self.num_sell_2.setFont(font1)
        self.num_sell_2.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
# "	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.num_sell_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.num_sell_2)

        self.num_sell = QLineEdit(self.frame)
        self.num_sell.setObjectName(u"num_sell")
        self.num_sell.setMinimumSize(QSize(0, 40))
        self.num_sell.setMaximumSize(QSize(100, 16777215))
        self.num_sell.setFont(font1)
        self.num_sell.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
# "	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.num_sell.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.num_sell)


        self.label_4 = QLineEdit(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 40))
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLineEdit{\n"
"border:2px solid transparent;\n"
"border-radius: 8px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
# "	border: 2px solid rgb(103, 222, 255);\n"
"}\n"
"QLineEdit::focus{\n"
"	border: 2px solid rgb(103, 222, 255);\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label_4)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
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

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)


        QMetaObject.connectSlotsByName(self)

        self.deleteItem.setText( "حذف")
        self.Change.setText( "تعديل")

        self.label_4.setText( self._priceIn)
        self.num_sell.setReadOnly(True)
        self.num_sell_2.setReadOnly(True)
        self.label_4.setReadOnly(True)
        if self._type == "store_sales":
            self.Change.setVisible(False)
            self.deleteItem.setVisible(False)
        #     self.label_4.setText( self._num)
        # else:
        #     self.label_4.setText("")
        # if self._type == "store" :
        #     self.label_4.setText( self._priceOut)
        #     self.num_sell_2.setText( self._priceIn)
            # self.num_sell.setText( self._priceIn)
        self.label_4.setText( self._num)
        self.num_sell.setText( self._priceIn)
        self.num_sell_2.setText( self._priceOut)
        self.label_2.setText( self._size)
        self.label_3.setText(self._color)
        self.label.setText( self._name)
        
        if self._type == "store":
            self.Change.clicked.connect(self.editItem)
            self.deleteItem.clicked.connect(self.removeItemInStore)
        if self._type == "sale":
            self.Change.setVisible(False)
            self.deleteItem.setVisible(False)
            # self.num_sell.setText("__ ")


        QMetaObject.connectSlotsByName(self)
        self.edit_state = True 
    def editItem(self):
        num = self.label_4.text()
        price_in = self.num_sell.text()
        price_out = self.num_sell_2.text()

        # validation for lineEdits
        onlyNum_specify  = QRegularExpression("[0-9]{15}")
        onlyNum_ = QRegularExpressionValidator(onlyNum_specify)
        if self.edit_state:
            self.Change.setText("حفظ التعديلات")
            self.label_4.setReadOnly(False)
            self.num_sell_2.setReadOnly(False)
            self.num_sell.setReadOnly(False)
            self.num_sell_2.setFocus()
            self.label_4.setFocus()
            self.label_4.setValidator(onlyNum_)
            self.num_sell.setValidator(onlyNum_)
            self.num_sell_2.setValidator(onlyNum_)
            self.edit_state = False
        else:
            if num and price_in and price_out and len(num) > 0 and len(price_in) > 0 and len(price_out) > 0 and num != " " and price_in != " " and price_out != " ":
                updatedProduct = _services.update_product(_database.SessionLocal(),self._id ,num,price_in, price_out)
                if updatedProduct:
                    self.num_sell.setStyleSheet("background-color:transparent;")
                    self.num_sell.setStyleSheet("background-color:transparent;")
                    self.num_sell_2.setStyleSheet("background-color:transparent;")
                    self.num_sell.setReadOnly(True)
                    self.num_sell_2.setReadOnly(True)
                    self.num_sell.setReadOnly(True)
                    
                    self.num_sell.setText( num )
                    self.num_sell.setText(price_in)
                    self.num_sell_2.setText(price_out)
                    self.edit_state = True
                    self.Change.setText( "تعديل")
    def removeItemInStore(self):
        from widgets.messageWidget.pyMessageBox import PyMessageBox

        PyMessageBox(
            323,
            176,
            " تحذير",
            "حذف المنتج",
            " اذا تم حذف منتج ف هذا قد يؤثر علي بعض العمليات المرتبطة به " ,
            "الغاء",
            "حذف"
        )
        
        if PyMessageBox.theStateOfTheMessaheBox(self) == "False":
            deleted_product = _services.delete_product( _database.SessionLocal(),self._id )
            # if deleted_product:
            self.setVisible(False)


