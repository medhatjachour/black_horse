# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sales_mainfPCiFL.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QMetaObject,QSize, Qt)
from PySide6.QtGui import ( QCursor, QFont)
from PySide6.QtWidgets import (QFrame,QSizePolicy ,QApplication , QSpacerItem,QGridLayout, QHBoxLayout, QLabel, QPushButton, QVBoxLayout)

from datetime import datetime, timedelta


from orm import services as _services
from orm import database as _database

class SalesMain(QFrame):
    def __init__(
        self,
        sale,
        _type,
    ):
        super().__init__()
        self._sale = sale
        self.resize(876, 160)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 0, 9, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom:1px solid rgb(199, 199, 199)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"border-bottom:0px solid rgb(197, 197, 197);\n"
"background-color: rgb(241, 247, 254);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.showMore = QPushButton(self.frame_2)
        self.showMore.setObjectName(u"showMore")
        self.showMore.setMinimumSize(QSize(110, 38))
        self.showMore.setMaximumSize(QSize(120, 16777215))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.showMore.setFont(font)
        self.showMore.setCursor(QCursor(Qt.PointingHandCursor))
        self.showMore.setStyleSheet(u"\n"
"letter-spacing: 0em;\n"
"text-align: center;\n"
"border:2px solid rgb(43, 109, 189);\n"
"color:rgb(43, 109, 189);\n"
"background-color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout.addWidget(self.showMore)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.status = QPushButton(self.frame_2)
        self.status.setObjectName(u"status")
        self.status.setMinimumSize(QSize(100, 38))
        self.status.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.status.setFont(font1)
        self.status.setStyleSheet(u"border:0px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 148, 109);\n"
"/*background-color: rgb(46, 204, 113);*/\n"
"")

        self.horizontalLayout.addWidget(self.status)

        self.client_budget = QLabel(self.frame_2)
        self.client_budget.setObjectName(u"client_budget")
        self.client_budget.setMinimumSize(QSize(61, 0))
        self.client_budget.setMaximumSize(QSize(61, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.client_budget.setFont(font2)
        self.client_budget.setStyleSheet(u"border-bottom:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.client_budget.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.client_budget)

        self.client_date = QLabel(self.frame_2)
        self.client_date.setObjectName(u"client_date")
        self.client_date.setMinimumSize(QSize(180, 0))
        self.client_date.setMaximumSize(QSize(180, 16777215))
        self.client_date.setFont(font2)
        self.client_date.setStyleSheet(u"border-bottom:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.client_date.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.client_date)

        self.lineEdit_link = QPushButton(self.frame_2)
        self.lineEdit_link.setObjectName(u"lineEdit_link")
        self.lineEdit_link.setMinimumSize(QSize(70, 38))
        self.lineEdit_link.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_link.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_link.setStyleSheet(u"/*border: 1px solid #000000;*/\n"
"border:0px;\n"
"padding: 0px 8px;\n"
"background-color: rgb(242, 248, 255);\n"
"border-bottom:0px;")

        self.lineEdit_link_paid = QPushButton(self.frame_2)
        self.lineEdit_link_paid.setObjectName(u"lineEdit_link_paid")
        self.lineEdit_link_paid.setMinimumSize(QSize(0, 0))
        self.lineEdit_link_paid.setMaximumSize(QSize(70, 16777215))
        self.lineEdit_link_paid.setCursor(QCursor(Qt.PointingHandCursor))
        self.lineEdit_link_paid.setStyleSheet(u"/*border: 1px solid #000000;*/\n"
            "border:0px;\n"
            "padding: 0px 8px;\n"
            "background-color: rgb(242, 248, 255);\n"
            "color: red;\n"
            "border-bottom:0px;")

        self.horizontalLayout.addWidget(self.lineEdit_link_paid)
        self.horizontalLayout.addWidget(self.lineEdit_link)

        self.client_phone = QLabel(self.frame_2)
        self.client_phone.setObjectName(u"client_phone")
        self.client_phone.setMinimumSize(QSize(117, 0))
        self.client_phone.setMaximumSize(QSize(125, 16777215))
        self.client_phone.setFont(font2)
        self.client_phone.setStyleSheet(u"border-bottom:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.client_phone.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.client_phone)

        self.client_name = QLabel(self.frame_2)
        self.client_name.setObjectName(u"client_name")
        self.client_name.setMinimumSize(QSize(200, 0))
        self.client_name.setMaximumSize(QSize(20000, 16777215))
        self.client_name.setFont(font2)
        self.client_name.setStyleSheet(u"border-bottom:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.client_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.client_name)

        self.sale_number = QLabel(self.frame_2)
        self.sale_number.setObjectName(u"sale_number")
        self.sale_number.setMinimumSize(QSize(26, 0))
        self.sale_number.setMaximumSize(QSize(50, 16777215))
        self.sale_number.setFont(font1)
        self.sale_number.setStyleSheet(u"border-bottom:0px;\n"
"background-color: rgb(255, 255, 255);")
        self.sale_number.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.sale_number)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_3.setStyleSheet(u"background-color: rgb(242, 248, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)



        QMetaObject.connectSlotsByName(self)







        self.frame_3.setVisible(False)
        self.showMore.setText( "عرض التفاصيل")
        self.clicked = True
        
        if _type == "sales":
            self.showMore.clicked.connect(self.show_sale_detail)
            self.status.setText( str( self._sale.status))
            self.sale_number.setText( str( self._sale.id))

            if  str(self._sale.status) == "انتظار":
                
                self.status.setStyleSheet("border:0px;\n"
                "color: rgb(255, 255, 255);\n"
                "background-color:#ff8000;\n"
                "border-radius:5px;")
                self.status.setCursor(QCursor(Qt.PointingHandCursor))
                self.status.clicked.connect(self.refuseOrder)
                
            if  str(self._sale.status) == "مرفوض":
                self.status.setStyleSheet("border:0px;\n"
                "color:  rgb(255, 255, 255);\n"
                "background-color:#e80000;\n"
                "border-radius:5px;")
            self.client_budget.setText( str( self._sale.total))
            self.client_date.setText( self._sale.date.strftime("%e %b %Y at %I:%M %p"))
            if self._sale.link and self._sale.link != "" and self._sale.link != " ":
                self.lineEdit_link.setText("Copy")
            else:
                self.lineEdit_link.setEnabled(False)
                self.lineEdit_link.setText( "__")
            self.lineEdit_link.clicked.connect(self.copyLink)
            if self._sale.phone and self._sale.phone != "" and self._sale.phone != " ":
                self.client_phone.setText(str( self._sale.phone))
            else:
                self.client_phone.setText("__")
            if self._sale.name and self._sale.name != "" and self._sale.name != " ":
                self.client_name.setText(str( self._sale.name))
            else:
                self.client_name.setText("__")
            
            # self.retranslateUi(self)
            # QtCore.QMetaObject.connectSlotsByName(self)
            
            if self._sale.date < (datetime.now() - timedelta(days=20, hours=1)):
                if self._sale.status == "انتظار":
                    self.acceptOrder()
            self.clicked = True
    
    
        elif _type == "checks":
            self.showMore.clicked.connect(self.show_sale_detail_checks)
            # self.status.setText( str( self._sale.status))
            self.sale_number.setText( str( self._sale.id))
            self.status.setVisible(False)
            self.client_budget.setText( str( self._sale.address))
            self.client_budget.setMinimumSize(QSize(270, 38))
            self.client_date.setText( self._sale.date.strftime("%e %b %Y "))
            if self._sale.total and self._sale.total != "" and self._sale.total != " ":
                self.lineEdit_link.setText(str(self._sale.total))
                self.lineEdit_link_paid.setText(str( self._sale.paid))
                self.lineEdit_link_paid.setMinimumSize(QSize(70, 38))
            else:
                self.lineEdit_link.setEnabled(False)
                self.lineEdit_link.setText( "__")
            if self._sale.phone and self._sale.phone != "" and self._sale.phone != " ":
                self.client_phone.setText(str( self._sale.phone))
            else:
                self.client_phone.setText("__")
            if self._sale.name and self._sale.name != "" and self._sale.name != " ":
                self.client_name.setText(str( self._sale.name))
            else:
                self.client_name.setText("__")
            # self.retranslateUi(self)
            # QtCore.QMetaObject.connectSlotsByName(self)
            
      
    def clear_tab(self,layout):
        while layout.count():
            child =  layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater() 
    def show_sale_detail(self):
        from widgets.productWidget.ui_selling import ProductWidget
        self.clear_tab(self.verticalLayout_2)
        if self.clicked:
            self.frame_3.setVisible(True)
            w = 40
            salesItems = _services.get_sales_items( _database.SessionLocal(), self._sale.id)
            for i in salesItems:
                w = w + 40
                # try:
                theProduct = _services.get_product_by_id( _database.SessionLocal(),i.product_id)
                # except:
                #     theProduct = {
                #         "id":0,
                #         "name":"المنتج محذوف",
                #         "size":"المنتج محذوف",
                #         "color":"المنتج محذوف",
                #         "num_of_products":"المنتج محذوف",
                #         "price_in":"المنتج محذوف",
                #         "price_out":"المنتج محذوف"
                #     }
                if theProduct:
                    self.verticalLayout_2.addWidget(ProductWidget(i.id, theProduct.name, theProduct.size, theProduct.color, i.num_of_products, theProduct.price_out, i.price_out,"store_sales"))
                else:
                    theProduct = {
                        'id':0,
                        'name':'المنتج محذوف',
                        'size':'المنتج محذوف',
                        'color':'المنتج محذوف',
                        'num_of_products':'المنتج محذوف',
                        'price_in':'المنتج محذوف',
                        'price_out':'المنتج محذوف'
                    }
                    self.verticalLayout_2.addWidget(ProductWidget(i.id, theProduct["name"], theProduct["size"], theProduct["color"], i.num_of_products, theProduct["price_in"], i.price_out,"store_sales"))

            self.frame_3.setMinimumSize(850 ,w)
            self.setMinimumSize(850, w + 60)
            # self.pushButton.setVisible(False)
            self.showMore.setText("اخفاء")
            self.clicked = False
        else:
            self.frame_3.setMinimumSize(850 ,0)
            self.setMinimumSize(850, 60)
            self.frame_3.setVisible(False)
            self.showMore.setText("عرض التفاصيل")
            self.clicked = True
    
    def show_sale_detail_checks(self):
        from widgets.productWidget.ui_selling import ProductWidget
        self.clear_tab(self.verticalLayout_2)
        if self.clicked:
            self.frame_3.setVisible(True)
            w = 40
            checkItems = _services.get_check_items( _database.SessionLocal(), self._sale.id)
            for i in checkItems:
                w = w + 40
                self.verticalLayout_2.addWidget(ProductWidget(i.id, str(i.date), str( i.paying),"","","","","check"))

            self.frame_3.setMinimumSize(850 , w)
            self.setMinimumSize(850, w + 60)
            # self.pushButton.setVisible(False)
            self.showMore.setText("اخفاء")
            self.clicked = False
        else:
            self.frame_3.setMinimumSize(850 ,0)
            self.setMinimumSize(850, 60)
            self.frame_3.setVisible(False)
            self.showMore.setText("عرض التفاصيل")
            self.clicked = True
    
    def refuseOrder(self):
        from widgets.messageWidget.pyMessageBox import PyMessageBox

        PyMessageBox(
            323,
            176,
            " شاور نفسك",
            "تغير حالة الطلب",
            "بص يسطي اختار الحالة و لو ضغط Xف هيتحول ل مقيول لوحدة بعد فترة",
        )
        
        if PyMessageBox.theStateOfTheMessaheBox(self) == "False":
            theOrder = _services.change_sale_status(_database.SessionLocal(),self._sale.id,"مرفوض")
            if theOrder:
                theItems = _services.get_sales_items(_database.SessionLocal(), self._sale.id)
                if theItems:    
                    for item in theItems:
                        _services.update_refused_product_num(_database.SessionLocal(), item.product_id , item.num_of_products)
                self.status.setText( "مرفوض")
                self.status.setStyleSheet("border:0px;\n"
                "color:  rgb(255, 255, 255);\n"
                "background-color:#e80000;\n"
                "border-radius:5px;")
        if PyMessageBox.theStateOfTheMessaheBox(self) == True:
            self.acceptOrder()
    def acceptOrder(self):
        theOrder = _services.change_sale_status(_database.SessionLocal(),self._sale.id,"مقبول")
        if theOrder:
            self.status.setText("مقبول")
            self.status.setStyleSheet("border:0px;\n"
                "color: rgb(255, 255, 255);\n"
                "background-color: rgb(0, 148, 109);\n"
                "border-radius:5px;")


    def copyLink(self):
        w =  self._sale.link
        if len(w) > 0:
            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(
                w
            )






