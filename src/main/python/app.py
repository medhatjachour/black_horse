# lip 
import sys
import math
import os
import uuid
from datetime import datetime, timedelta
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QCompleter, \
    QPushButton
from PySide6.QtCore import Qt, QThreadPool, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator, QCursor
# widgets
from ui.ui_main import Ui_MainWindow
from widgets.worker.Worker import Worker
# orm
from orm import services as _services
from orm import database as _database
from up_down import upload_db, download_db
from fbs_runtime.application_context.PySide6 import ApplicationContext
from widgets.py_chart_line.py_line_chart import PyLineChart

app_context = ApplicationContext()
# os.environ["QT_FONT_DPI"] = "2"
_services.create_database()
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.lineChart = None
        self.vertical_spacer2 = None
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.show()      
        self.namingSearch = False
        self.threadpool = QThreadPool()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.frame_8.setVisible(False)
        self.rightFrame = False
        self.isAdmin = False
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        # validation for lineEdits
        only_num_specify = QRegularExpression("[0-9]{15}")
        only_num_ = QRegularExpressionValidator(only_num_specify)

        self.ui.add_num.setValidator(only_num_)
        self.ui.add_p_in.setValidator(only_num_)
        self.ui.add_p_out.setValidator(only_num_)
        self.ui.num_sell.setValidator(only_num_)
        self.ui.price_sell.setValidator(only_num_)

        self.ui.price_sell.setValidator(only_num_)
        self.ui.phone.setValidator(only_num_)
        self.ui.add_color_line_2.setValidator(only_num_)

        # top par
        self.toggle_full_screen()
        self.ui.pushButton_3.clicked.connect(self.close_fun)
        self.ui.pushButton_4.clicked.connect(self.toggle_full_screen)
        self.ui.pushButton_5.clicked.connect(self.showMinimized)
        self.ui.pushButton_7.clicked.connect(self.close_fun)
        self.ui.pushButton_6.clicked.connect(self.toggle_full_screen)
        self.ui.pushButton_8.clicked.connect(self.showMinimized)
        self.ui.frame_30.mouseMoveEvent = self.move_window1
        self.ui.frame_5.mouseMoveEvent = self.move_window2
        # login  
        self.ui.password_3.setEchoMode(QLineEdit.Password)
        self.ui.signIn.clicked.connect(self.login)
        self.ui.addToCart_2.clicked.connect(self.logout)
        self.ui.button_patiensts.clicked.connect(self.set_home)
        self.ui.button_patiensts_2.clicked.connect(self.set_sales)
        self.ui.button_patiensts_3.clicked.connect(self.set_store)
        self.ui.button_patiensts_6.clicked.connect(self.set_settings)
        self.ui.button_patiensts_7.clicked.connect(self.set_status)
        self.ui.pushButton_9.clicked.connect(self.right_menu)

        self.ui.button_patiensts_5.clicked.connect(self.set_daily)
        self.ui.button_patiensts_4.clicked.connect(self.set_right_settings)
        self.ui.addToCart_3.clicked.connect(self.upload_fun)
        self.ui.pushButton_12.clicked.connect(self.download)
        # operation Sale
        self.removeCart = QPushButton(self.ui.frame)
        self.removeCart.setObjectName(u"removeCart")
        self.removeCart.setCursor(QCursor(Qt.PointingHandCursor))
        self.removeCart.setVisible(False)
        self.removeCart.setText("افراغ السلة")
        self.removeCart.clicked.connect(self.removeCartFun)
        self.ui.gridLayout_3.addWidget(self.removeCart, 0, 0, 1, 1)

        self.productsCompleted = []
        self.main_completing()
        self.theSaleProductItem = None
        self.cart = []
        self.showTotal = 0
        self.ui.final_price.setText(str(self.showTotal))

        self.ui.color_sell.currentIndexChanged.connect(self.chose_size_sale)
        self.ui.size_sell.currentIndexChanged.connect(self.chose_color_sale)
        self.ui.addToCart.clicked.connect(self.addItemSale)
        self.ui.done_sell.clicked.connect(self.doneSellCart)
        # store
        self.ui.pushButton.setVisible(False)
        self.sizes = []
        self.colors = []
        self.ShowColorsInComboBox()
        self.ShowSizesInComboBox()
        self.showProductsInStore()
        self.ui.pushButton.clicked.connect(self.setDefaultStore)
        self.ui.enter_store.clicked.connect(self.enterStoreFun)
        self.ui.color_sell_3.currentIndexChanged.connect(self.addProductColors)
        self.ui.color_sell_4.currentIndexChanged.connect(self.addProductSizes)
        # salesStore
        self.ui.color_sell_2.addItem("")
        self.ui.color_sell_2.addItem("رقم العملية")
        self.ui.color_sell_2.addItem("اسم العميل")
        self.ui.color_sell_2.addItem("الحالة")
        self.ui.color_sell_2.addItem("رقم التيلفون")
        self.ui.color_sell_2.addItem("اللنك")
        self.showSalesInSalesStore()
        self.ui.search.clicked.connect(self.searchInSalesStore)
        # settings 
        self.ui.add_color_btn.clicked.connect(self.addColorFun)
        self.ui.add_color_line.returnPressed.connect(self.addColorFun)
        self.ui.add_size_bn.clicked.connect(self.addSizeFun)
        self.ui.add_size_line.returnPressed.connect(self.addSizeFun)
        self.ui.add_user.clicked.connect(self.addUserFun)
        self.ui.add_usr.returnPressed.connect(self.checkUserName)
        self.ui.add_pass.returnPressed.connect(self.addUserFun)
        self.showUsers()
        self.showColors()
        self.showSizes()
        # statics
        self.ChartData = [[]]
        self.SeriesNames = []
        self.duration = 1
        self.ui.color_sell_5.currentIndexChanged.connect(self.changeDuration)
        self.ui.color_sell_6.currentIndexChanged.connect(self.passDataToChart)
        self.ui.pushButton_10.clicked.connect(self.showStatics)
        self.ui.pushButton_11.clicked.connect(self.showGard)
        self.ui.pushButton_13.clicked.connect(self.show_daily)
        self.ui.button_patiensts_8.clicked.connect(self.showCharts)
        self.ui.button_patiensts_9.clicked.connect(self.showOutCome)
        self.ui.add_color_btn_2.clicked.connect(self.createOutPut)
        self.showOutPut()
        self.showGard()
        self.showStatics()
        self.show_daily()

    # ////////////////////////////////////////////////////////////  top par
    def showMinimized(self) -> None:
        return super().showMinimized()

    def toggle_full_screen(self):
        is_full = bool(self.windowState() == Qt.WindowFullScreen)
        if is_full:
            self.showNormal()
        else:
            self.showFullScreen()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def move_window1(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def move_window2(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def close_fun(self):
        from widgets.messageWidget.pyMessageBox import PyMessageBox
        PyMessageBox(
            323,
            176,
            " تنبيه",
            " نسخ احتياطي ",
            " سيتم استبدال ال داتا الموجودة علي السحابه ب احدث داتا الان",
            "رفع",
            "الغاء"
        )
        if PyMessageBox.theStateOfTheMessaheBox(self):
            path = app_context.get_resource('data/client_secret.json')
            # upload_db(path)

        self.close()

    # ////////////////////////////////////////////////////////////  main
    def set_home(self):
        self.ui.button_patiensts.setChecked(True)
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def set_sales(self):
        if self.isAdmin:
            self.ui.stackedWidget_2.setCurrentIndex(2)

    def set_store(self):
        if self.isAdmin:
            self.ui.stackedWidget_2.setCurrentIndex(1)

    def set_settings(self):
        if self.isAdmin:
            self.ui.button_patiensts.setChecked(False)
            self.ui.button_patiensts_2.setChecked(False)
            self.ui.button_patiensts_3.setChecked(False)
            self.ui.stackedWidget_2.setCurrentIndex(3)

    def set_status(self):
        if self.isAdmin:
            self.ui.button_patiensts.setChecked(False)
            self.ui.button_patiensts_2.setChecked(False)
            self.ui.button_patiensts_3.setChecked(False)
            # self.ui.stackedWidget_2.setCurrentIndex(3)
            self.ui.stackedWidget_2.setCurrentIndex(4)  # add a bottom to open it

    def right_menu(self):
        self.rightFrame = not self.rightFrame
        self.ui.frame_8.setVisible(self.rightFrame)

    def set_daily(self):
        self.ui.stackedWidget_3.setCurrentIndex(0)

    def set_right_settings(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)

    def show_daily(self):
        self.clear_tab(self.ui.verticalLayout_44)
        from widgets.daily.ui_daily import Daily
        outputs = _services.get_outputs(_database.SessionLocal())
        for i in (outputs[::-1]):
            if i.date.date() == datetime.today().date():
                self.ui.verticalLayout_44.addWidget(Daily(i.id, i.num, "dailyOut", i.date, i.disc))
        sales = _services.get_all_sales(_database.SessionLocal())
        for i in (sales[::-1]):
            if i.date.date() == datetime.today().date():
                self.ui.verticalLayout_44.addWidget(Daily(i.id, i.total, "dailyIn", i.date, ""))

        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.verticalLayout_44.addItem(self.vertical_spacer2)

    # /////////////////////////////////////////////////////////// clearing taps
    def clear_tab(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def clear_tab_except_first(self, layout):
        for i in range(layout.count() - 1):
            child = layout.takeAt(1)
            if child.widget():
                child.widget().deleteLater()

    # ////////////////////////////////////////////////////////////  login
    def login(self):
        self.ui.frame_8.setVisible(False)
        name = self.ui.username_3.text()
        password = self.ui.password_3.text()
        user_exist = _services.get_user(_database.SessionLocal(), str(name))
        if user_exist:
            if user_exist.password == password:
                self.isAdmin = user_exist.user_type
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.stackedWidget_2.setCurrentIndex(0)
                self.set_home()
                self.ui.feedback.setText(f"welcome {name}")
                self.ui.feedback.setStyleSheet(u"color: #00946d;")
                self.ui.username_3.setText("")
                self.ui.password_3.setText("")
            else:
                self.ui.feedback.setText("password is incorrect")
                self.ui.feedback.setStyleSheet(u"color: #ff0000;")
        else:
            self.ui.feedback.setText("user name  is incorrect")
            self.ui.feedback.setStyleSheet(u"color: #ff0000;")
        if str(name) == str(
                "ASD98465416!@#$$%DSAD@!#@!#54sd!@#484asd!@#6486@!$#@!545441!@#4541!@#@!#!4687415DSFsdfd!@#!54ASDAS"
                "!234ds14"):
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.stackedWidget_2.setCurrentIndex(3)

    def logout(self):
        self.ui.username_3.setText("")
        self.ui.password_3.setText("")
        self.ui.stackedWidget.setCurrentIndex(0)
        self.isAdmin = False

    def upload_fun(self):
        from widgets.messageWidget.pyMessageBox import PyMessageBox
        PyMessageBox(
            323,
            176,
            " تنبيه",
            " نسخ احتياطي ",
            " سيتم استبدال ال داتا الموجودة علي السحابه ب احدث داتا الان",
            "رفع",
            "الغاء"
        )

        if PyMessageBox.theStateOfTheMessaheBox(self):
            path = app_context.get_resource('data/client_secret.json')
            # upload_db(path)
            self.ui.feedback.setText("uploaded successfully")
            self.ui.feedback.setStyleSheet(u"color: #10e205;")

    def download(self):
        from widgets.messageWidget.pyMessageBox import PyMessageBox
        PyMessageBox(
            323,
            176,
            " تنبيه",
            " استرجاع ",
            " سيتم استبدال ال داتا الموجودة علي الجهاز ب احدث داتا موجودة علي السحابة",
            "تحميل",
            "الغاء"
        )

        if PyMessageBox.theStateOfTheMessaheBox(self):
            path = app_context.get_resource('data/client_secret.json')
            # download_db(path)
            self.ui.feedback.setText("downloaded successfully")
            self.ui.feedback.setStyleSheet(u"color: #10e205;")

    # ///////////////////////////////////////////////////////////
    def main_completing(self):
        the_products = _services.get_products(_database.SessionLocal())
        if the_products:
            for i in the_products:
                if i.name in self.productsCompleted:
                    pass
                else:
                    self.productsCompleted.append(i.name)
            completer = QCompleter(self.productsCompleted)

            completer.activated.connect(self.onActivatedChosenProduct)
            self.ui.procut_sell.setCompleter(completer)
            self.ui.add_product.setCompleter(completer)

    def onActivatedChosenProduct(self):
        self.ui.color_sell.clear()
        self.ui.size_sell.clear()
        self.ui.num_sell.setText("")
        self.ui.price_sell.setText("")
        product = self.ui.procut_sell.text()
        the_products = _services.get_products_by_name(_database.SessionLocal(), product)
        if the_products:
            sizes = []
            self.ui.color_sell.addItem("")
            for i in the_products:
                if i.size in sizes:
                    pass
                else:
                    sizes.append(i.size)
            for x in sizes:
                self.ui.color_sell.addItem(x)

    def chose_size_sale(self):
        self.ui.size_sell.clear()
        name = self.ui.procut_sell.text()
        size = self.ui.color_sell.currentText()
        the_products = _services.get_products_by_name_and_size(_database.SessionLocal(), name, size)
        if the_products:
            colors = []
            self.ui.size_sell.addItem("")
            for i in the_products:
                if i.color in colors:
                    pass
                else:
                    colors.append(i.color)
            for x in colors:
                self.ui.size_sell.addItem(x)

    def chose_color_sale(self):
        name = self.ui.procut_sell.text()
        size = self.ui.color_sell.currentText()
        color = self.ui.size_sell.currentText()
        the_products = _services.get_product(_database.SessionLocal(), name, color, size)
        if the_products:
            self.theSaleProductItem = the_products
            self.ui.price_sell.setText(the_products.price_out)

    def addItemSale(self):
        num = self.ui.num_sell.text()
        price_out = self.ui.price_sell.text()
        w = None
        if num and num != "" and self.theSaleProductItem:
            if int(self.theSaleProductItem.num) >= int(num):
                if self.theSaleProductItem and num and int(num) > 0 and int(price_out) > 0:
                    w = [self.theSaleProductItem, num, price_out]
                if self.theSaleProductItem is None or w in self.cart:
                    self.ui.feedback.setText("item already in cart")
                    self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                else:
                    self.ui.procut_sell.setText("")
                    self.ui.color_sell.clear()
                    self.ui.size_sell.clear()
                    self.ui.num_sell.setText("")
                    self.ui.price_sell.setText("")
                    self.showTotal = self.showTotal + (int(num) * int(price_out))
                    self.ui.final_price.setText(str(self.showTotal))
                    self.cart.append(w)
                    self.ui.size_sell.clear()
                    self.ui.color_sell.clear()
                    self.showItemsInCart()
                    self.removeCart.setVisible(True)
                    self.ui.feedback.setText("item added successfully")
                    self.ui.feedback.setStyleSheet(u"color: #00946d;")
            else:

                self.ui.feedback.setText("not enough items in the store ")
                self.ui.feedback.setStyleSheet(u"color: #b90000;")
        else:

            self.ui.feedback.setText("complete the sale please!")
            self.ui.feedback.setStyleSheet(u"color: #b90000;")

    def showItemsInCart(self):
        self.clear_tab(self.ui.verticalLayout_12)
        from widgets.productWidget.ui_selling import ProductWidget
        for i in self.cart:
            self.ui.verticalLayout_12.addWidget(
                ProductWidget((i[0]).id, (i[0]).name, (i[0]).size, (i[0]).color, i[1], (i[0]).price_out, i[2], "sale"))

        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_12.addItem(self.vertical_spacer2)

    def doneSellCart(self):
        name = self.ui.clientname.text()
        phone = self.ui.phone.text()
        link = self.ui.Link.text()
        date = datetime.now()
        total = 0
        real_total = 0
        status = "انتظار"
        sale_id = None
        if (len(self.cart)) > 0:
            self.ui.addToCart.setEnabled(False)
            self.ui.done_sell.setEnabled(False)
            self.ui.addToCart.setText("... استني")
            self.ui.done_sell.setText("... استني")
            payload = {
                "name": name,
                "phone": phone,
                "link": link,
                "date": date,
                "total": total,
                "status": status,
                "real_total": real_total,
            }
            create_sale = _services.create_sales(
                _database.SessionLocal(), payload
            )
            if create_sale:
                sale_id = create_sale.id
                for i in self.cart:
                    total = int(total) + int(i[2])
                    real_total = int(real_total) + int((i[0]).price_out)
                    payload = {
                        "num_of_products": i[1],
                        "price_out": i[2],
                        "sale_id": sale_id,
                        "product_id": (i[0]).id
                    }
                    add_Sale_item = _services.create_Sale_item(
                        _database.SessionLocal(), payload
                    )
                    if add_Sale_item:
                        update_product_num = _services.update_product_num(
                            _database.SessionLocal(), (i[0]).id, i[1]
                        )
                        if update_product_num:
                            self.ui.feedback.setText("updated nums in store")
                            self.ui.feedback.setStyleSheet(u"color: #00946d;")

                finish_sale = _services.finish_sale(
                    _database.SessionLocal(), sale_id, total, real_total
                )
                if finish_sale:
                    # refresh store and refresh the sales
                    self.clear_tab(self.ui.verticalLayout_12)
                    self.showSalesInSalesStore()
                    self.showProductsInStore()
                    self.cart = []
                    self.ui.clientname.setText("")
                    self.ui.phone.setText("")
                    self.ui.Link.setText("")
                    self.showTotal = 0
                    self.ui.final_price.setText(str(self.showTotal))
                    self.ui.feedback.setText("successfully completed sale")
                    self.ui.feedback.setStyleSheet(u"color: #00946d;")
        else:
            self.ui.feedback.setText("please add items to cart")
            self.ui.feedback.setStyleSheet(u"color: #ff0000;")
        self.ui.done_sell.setText("اتمام العملية")
        self.ui.done_sell.setEnabled(True)
        self.ui.addToCart.setText("ادخال")
        self.ui.addToCart.setEnabled(True)

    def removeCartFun(self):
        self.clear_tab(self.ui.verticalLayout_12)
        self.cart = []
        self.ui.clientname.setText("")
        self.ui.phone.setText("")
        self.ui.Link.setText("")
        self.showTotal = 0
        self.ui.final_price.setText(str(self.showTotal))
        self.ui.feedback.setText("cart is empty now")
        self.ui.feedback.setStyleSheet(u"color: #d90000;")
        self.removeCart.setVisible(False)

    # /////////////////////////////////////////////////////////// store
    # default
    def setDefaultStore(self):
        self.ui.enter_store.setText("بحث ")
        self.clear_tab_except_first(self.ui.verticalLayout_9)
        self.clear_tab_except_first(self.ui.verticalLayout_10)
        self.sizes = []
        self.colors = []
        self.ui.add_product.setText("")
        self.ui.add_num.setText("")
        self.ui.add_p_in.setText("")
        self.ui.add_p_out.setText("")
        self.ui.color_sell_3.setCurrentIndex(0)
        self.ui.color_sell_4.setCurrentIndex(0)
        self.main_completing()
        self.ui.feedback.setText(f"removed old selection")
        self.ui.feedback.setStyleSheet(u"color: #00946d;")
        self.ui.pushButton.setVisible(False)

    # colors
    def ShowColorsInComboBox(self):
        self.ui.color_sell_3.clear()
        colors = _services.get_colors(_database.SessionLocal())
        self.ui.color_sell_3.addItem("")
        for i in colors:
            self.ui.color_sell_3.addItem(i.name)

    def addProductColors(self):
        the_color = self.ui.color_sell_3.currentText()
        if the_color in self.colors:
            self.ui.feedback.setText(f"color {the_color} already exists")
            self.ui.feedback.setStyleSheet(u"color: #ff0000;")
        else:

            self.ui.pushButton.setVisible(True)
            if the_color != "" and the_color != " ":
                from widgets.labelx.ui_alabelX import aLabelX
                self.ui.verticalLayout_9.addWidget(aLabelX(the_color, "color"))
                self.colors.append(the_color)
                self.ui.enter_store.setText("ادخال")

            self.ui.feedback.setText(f"")

    # sizes
    def ShowSizesInComboBox(self):

        self.ui.color_sell_4.clear()
        sizes = _services.get_sizes(_database.SessionLocal())
        self.ui.color_sell_4.addItem("")
        for i in sizes:
            self.ui.color_sell_4.addItem(i.name)

    def addProductSizes(self):
        the_size = self.ui.color_sell_4.currentText()
        if the_size in self.sizes:
            self.ui.feedback.setText(f"size {the_size} already exists")
            self.ui.feedback.setStyleSheet(u"color: #ff0000;")
        else:
            if the_size != "" and the_size != " ":
                from widgets.labelx.ui_alabelX import aLabelX

                self.ui.verticalLayout_10.addWidget(aLabelX(the_size, "size"))
                self.sizes.append(the_size)
                self.ui.enter_store.setText("ادخال")
            self.ui.feedback.setText(f"")

    def removeColorAndWidgets(self, _type, name):
        if _type == "size":
            self.sizes.remove(name)
        if _type == "color":
            self.colors.remove(name)

            # product

    def enterStoreFun(self):

        worker = Worker(
            partial(
                self.adding_thread,
            )
        )

        worker.signals.result.connect(partial(self.resultFunction))
        self.threadpool.start(worker)

    def adding_thread(self, progress_callback):
        name = (self.ui.add_product.text()).lower()
        num = self.ui.add_num.text()
        priceIn = self.ui.add_p_in.text()
        priceOut = self.ui.add_p_out.text()
        if len(self.sizes) > 0 and len(self.colors) > 0:
            self.ui.enter_store.setText("...adding")
            for size in self.sizes:
                for color in self.colors:
                    TheProductExists = _services.get_product(_database.SessionLocal(), name, color, size)
                    if TheProductExists:
                        self.ui.feedback.setText(f"the product with {name} ,{color}, {size} already exists")
                        self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                    else:
                        if name and name != "" and name != " " and len(name) >= 2:
                            if num and int(num) > 0:
                                if priceIn and priceOut:
                                    if int(priceOut) >= int(priceIn) and int(priceIn) > 0 and int(priceOut) > 0:
                                        payload = {
                                            "id": str(uuid.uuid4()),
                                            "name": name,
                                            "num": num,
                                            "price_in": priceIn,
                                            "price_out": priceOut,
                                            "color": color,
                                            "size": size,
                                        }
                                        createProduct = _services.create_Product(
                                            _database.SessionLocal(), payload
                                        )
                                        if createProduct:

                                            self.ui.feedback.setText(f"product {name} created successfully")
                                            self.ui.feedback.setStyleSheet(u"color: #00946d;")
                                            if size == self.sizes[-1] and color == self.colors[-1]:
                                                self.clear_tab_except_first(self.ui.verticalLayout_9)
                                                self.clear_tab_except_first(self.ui.verticalLayout_10)
                                                self.sizes = []
                                                self.colors = []
                                                self.ui.add_product.setText("")
                                                self.ui.add_num.setText("")
                                                self.ui.add_p_in.setText("")
                                                self.ui.add_p_out.setText("")
                                                self.ui.color_sell_3.setCurrentIndex(0)
                                                self.ui.color_sell_4.setCurrentIndex(0)
                                        else:
                                            self.ui.feedback.setText(f"can't create product {name}")
                                            self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                                    else:
                                        self.ui.add_p_in.setFocus()
                                        self.ui.add_p_out.setFocus()
                                        self.ui.feedback.setText(f"please check price in and price out")
                                        self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                                else:
                                    self.ui.add_p_in.setFocus()
                                    self.ui.add_p_out.setFocus()
                                    self.ui.feedback.setText(f"please check price in > price out > 0 ")
                                    self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                            else:
                                self.ui.add_num.setFocus()
                                self.ui.feedback.setText(f"please enter a valid number > 0 ")
                                self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                        else:
                            self.ui.add_product.setFocus()
                            self.ui.feedback.setText(f"enter a valid name more than or equal to 3 characters")
                            self.ui.feedback.setStyleSheet(u"color: #ff0000;")
        else:
            # if len( name ) > 0:
            #     self.ui.feedback.setText(f"do you wanna search for {name}")
            #     self.ui.feedback.setStyleSheet(u"color: #008000;")
            # else:
            if name and len(name) > 0 and name != "":
                self.namingSearch = True
                # searchedProducts = _services.get_products_by_name(_database.SessionLocal(), name)
                # self.showSearchedProductsInStore(searchedProducts)
            self.ui.feedback.setText(f"Please choose a size and a color")
            self.ui.feedback.setStyleSheet(u"color: #ff0000;")

    def resultFunction(self, result):
        name = (self.ui.add_product.text()).lower()
        if self.namingSearch:
            if name and len(name) > 0 and name != "":
                searchedProducts = _services.get_products_by_name(_database.SessionLocal(), name)
                self.showSearchedProductsInStore(searchedProducts)
        else:
            self.showProductsInStore()
            self.main_completing()
        self.namingSearch = False

    def showProductsInStore(self):
        self.ui.enter_store.setText("بحث ")
        self.clear_tab(self.ui.verticalLayout_13)
        products = _services.get_products(_database.SessionLocal())
        from widgets.productWidget.ui_selling import ProductWidget
        for i in (products[::-1]):
            self.ui.verticalLayout_13.addWidget(
                ProductWidget(i.id, i.name, i.size, i.color, i.num, i.price_in, i.price_out, "store"))
        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_13.addItem(self.vertical_spacer2)

    def showSearchedProductsInStore(self, searchedProducts):
        self.ui.enter_store.setText("عرض الكل")
        self.ui.add_product.setText("")
        self.clear_tab(self.ui.verticalLayout_13)
        products = searchedProducts
        from widgets.productWidget.ui_selling import ProductWidget
        for i in (products[::-1]):
            self.ui.verticalLayout_13.addWidget(
                ProductWidget(i.id, i.name, i.size, i.color, i.num, i.price_in, i.price_out, "store"))

        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_13.addItem(self.vertical_spacer2)

    #  /////////////////////////////////////////////////////////// SalesStore
    def searchInSalesStore(self):
        searchType = self.ui.color_sell_2.currentText()
        searchKey = self.ui.procut_sell_2.text()
        theSales = {}
        if searchType and searchType != "" and searchKey != " ":
            if searchKey and searchKey != " " and searchKey != "" and len(searchKey) > 0:
                if searchType == "رقم العملية":
                    if isinstance(int(searchKey), int):
                        theSales = _services.get_sales_by_id(_database.SessionLocal(), int(searchKey))
                        if theSales:
                            self.showSearchedSalesInSalesStore(theSales)
                            self.ui.feedback.setText("")
                    else:
                        self.ui.feedback.setText("please a valid number of sales")
                        self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                if searchType == "اسم العميل":
                    theSales = _services.get_sales_by_name(_database.SessionLocal(), str(searchKey))
                    if theSales:
                        self.showSearchedSalesInSalesStore(theSales)
                        self.ui.feedback.setText("")
                elif searchType == "الحالة":
                    theSales = _services.get_sales_by_status(_database.SessionLocal(), str(searchKey))
                    if theSales:
                        self.showSearchedSalesInSalesStore(theSales)
                        self.ui.feedback.setText("")
                elif searchType == "رقم التيلفون":
                    if isinstance(int(searchKey), int):
                        theSales = _services.get_sales_by_phone(_database.SessionLocal(), str(searchKey))
                        if theSales:
                            self.showSearchedSalesInSalesStore(theSales)
                            self.ui.feedback.setText("")
                    else:
                        self.ui.feedback.setText("please a valid number of phone")
                        self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                elif searchType == "اللنك":
                    theSales = _services.get_sales_by_link(_database.SessionLocal(), str(searchKey))
                    if theSales:
                        self.showSearchedSalesInSalesStore(theSales)

                        self.ui.feedback.setText("")
            else:
                self.showSalesInSalesStore()
                self.ui.feedback.setText("please a valid name ")
                self.ui.feedback.setStyleSheet(u"color: #ff0000;")
        else:
            self.showSalesInSalesStore()
            self.ui.feedback.setText("please select a search type")
            self.ui.feedback.setStyleSheet(u"color: #ff0000;")

    def showSalesInSalesStore(self):

        self.clear_tab(self.ui.verticalLayout_14)

        sales = _services.get_all_sales(_database.SessionLocal())
        from widgets.selling_store.ui_sales_main import SalesMain
        for i in (sales[::-1]):
            self.ui.verticalLayout_14.addWidget(SalesMain(i))

        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_14.addItem(self.vertical_spacer2)

    def showSearchedSalesInSalesStore(self, searchedSales):
        # self.ui.search.setText("عرض الكل")
        self.clear_tab(self.ui.verticalLayout_14)
        sales = searchedSales

        from widgets.selling_store.ui_sales_main import SalesMain

        for i in sales:
            self.ui.verticalLayout_14.addWidget(SalesMain(i))
        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_14.addItem(self.vertical_spacer2)

    #  /////////////////////////////////////////////////////////// Edits
    # colors 
    def addColorFun(self):
        color = self.ui.add_color_line.text()
        if color and color != "" and color != " ":
            colorExist = _services.get_color(_database.SessionLocal(), str(color))
            if colorExist:
                self.ui.feedback.setText("color already exists")
                self.ui.feedback.setStyleSheet(u"color: #ff0000;")
            else:
                payload = {
                    "id": str(uuid.uuid4()),
                    "name": color
                }
                createColor = _services.create_color(
                    _database.SessionLocal(), payload
                )
                if createColor:
                    self.ui.add_color_line.setText("")
                    self.showColors()
                    self.ShowColorsInComboBox()
                    self.ui.feedback.setText("added successfully")
                    self.ui.feedback.setStyleSheet(u"color: #00b359;")
        else:
            self.ui.feedback.setText("Please enter a valid color")
            self.ui.feedback.setStyleSheet(u"color: #ce0000;")

    def showColors(self):
        self.clear_tab(self.ui.verticalLayout_17)
        colors = _services.get_colors(_database.SessionLocal())
        from widgets.size_color_user.ui_color_size import SizeAndColor
        for i in (colors[::-1]):
            self.ui.verticalLayout_17.addWidget(SizeAndColor(i.id, i.name, "color"))

        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_17.addItem(self.vertical_spacer2)

    # sizes
    def addSizeFun(self):
        size = self.ui.add_size_line.text()
        if size and size != "" and size != " ":
            sizeExist = _services.get_size(_database.SessionLocal(), str(size))
            if sizeExist:
                self.ui.feedback.setText("size already exists")
                self.ui.feedback.setStyleSheet(u"color: #ff0000;")
            else:
                payload = {
                    "id": str(uuid.uuid4()),
                    "name": size
                }
                createSize = _services.create_size(
                    _database.SessionLocal(), payload
                )
                if createSize:
                    self.ui.add_size_line.setText("")
                    self.showSizes()
                    self.ShowSizesInComboBox()
                    self.ui.feedback.setText("added successfully")
                    self.ui.feedback.setStyleSheet(u"color: #00b359;")
        else:
            self.ui.feedback.setText("please enter a valid size")
            self.ui.feedback.setStyleSheet(u"color: #b90000;")

    def showSizes(self):
        self.clear_tab(self.ui.verticalLayout_19)
        sizes = _services.get_sizes(_database.SessionLocal())
        from widgets.size_color_user.ui_color_size import SizeAndColor
        for i in (sizes[::-1]):
            self.ui.verticalLayout_19.addWidget(SizeAndColor(i.id, i.name, "size"))

        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_19.addItem(self.vertical_spacer2)

    # users
    def addUserFun(self):
        name = self.ui.add_usr.text()
        password = self.ui.add_pass.text()
        if name and name != "" and name != " " and len(name) >= 4:
            if password and password != "" and password != " " and len(password) >= 4:
                userExist = _services.get_user(_database.SessionLocal(), str(name))
                if userExist:
                    self.ui.feedback.setText("userName already exists")
                    self.ui.feedback.setStyleSheet(u"color: #ff0000;")
                else:
                    payload = {
                        "name": name,
                        "password": password,
                        "user_type": self.ui.checkBox.isChecked(),
                    }
                    createUser = _services.create_user(
                        _database.SessionLocal(), payload
                    )
                    if createUser:
                        self.ui.add_usr.setText("")
                        self.ui.add_pass.setText("")
                        self.ui.checkBox.setChecked(False)
                        self.showUsers()
                        self.ui.feedback.setText("added successfully")
                        self.ui.feedback.setStyleSheet(u"color: #00b359;")
        else:
            self.ui.feedback.setText("please enter a valid name and pass word")
            self.ui.feedback.setStyleSheet(u"color: #ff0000;")

    def showUsers(self):
        self.clear_tab(self.ui.verticalLayout_15)
        users = _services.get_users(_database.SessionLocal())
        from widgets.size_color_user.ui_color_size import SizeAndColor
        for i in (users[::-1]):
            self.ui.verticalLayout_15.addWidget(SizeAndColor(i.id, i.name, "user"))

        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_15.addItem(self.vertical_spacer2)

    def checkUserName(self):
        name = self.ui.add_usr.text()
        if len(name) >= 4:
            self.ui.add_pass.setFocus()
        else:
            self.ui.feedback.setText(f"the name must be at least 4 characters")
            self.ui.feedback.setStyleSheet(u"color: #ff0000;")

    #  /////////////////////////////////////////////////////////// Statics
    def changeDuration(self):
        text = self.ui.color_sell_5.currentText()
        if text == "last 24 hours":
            self.duration = 1
        elif text == "last 7 days":
            self.duration = 7
        elif text == "last 30 days":
            self.duration = 30
        elif text == "last year":
            self.duration = 360
        elif text == "all the time":
            self.duration = 36000

    def showStatics(self):
        self.ui.pushButton_10.setEnabled(False)
        worker = Worker(
            partial(
                self.start_statics,
            )
        )
        worker.signals.result.connect(partial(self.resultFunctionStatics))
        self.threadpool.start(worker)

    def start_statics(self, progress_callback):
        theSales = _services.get_all_sales(_database.SessionLocal())
        num = 0
        pieces_num = 0
        total_in = 0
        total_out = 0
        real = 0
        predicted = 0
        priceIn = 0
        output = 0
        theSales = _services.get_all_sales(_database.SessionLocal())
        if theSales:
            for sales in theSales:
                if sales.status != "مرفوض":
                    if sales.date >= (datetime.now() - timedelta(days=int(self.duration))):
                        num = num + 1
                        total_in = total_in + int(sales.total)
                        total_out = total_out + int(sales.real_total)
                        items = _services.get_sales_items(_database.SessionLocal(), sales.id)
                        for item in items:
                            pieces_num = pieces_num + int(item.num_of_products)
                            theProduct = _services.get_product_by_id(_database.SessionLocal(), item.product_id)
                            if theProduct:
                                real = real + int(item.price_out)
                                priceIn = priceIn + int(theProduct.price_in)
                                predicted = predicted + int(theProduct.price_out)
        predictedIncome = int(predicted) - int(priceIn)
        real = real - int(priceIn)
        self.ui.label_53.setText(f"{str(num)} n")
        self.ui.label_65.setText(f"{str(pieces_num)} n")
        self.ui.label_61.setText(f"{str(total_in)} $")
        self.ui.label_57.setText(f"{str(real)} $")
        self.ui.label_63.setText(f"{str(total_out)} $")
        self.ui.label_59.setText(f"{str(predictedIncome)} $")
        self.ui.label_67.setText(f"{str(priceIn)} $")

        theOutPut = _services.get_outputs(_database.SessionLocal())
        if theOutPut:
            for sales in theOutPut:
                if sales.date >= (datetime.now() - timedelta(days=int(self.duration))):
                    output += sales.num
        self.ui.label_74.setText(f"{str(output)} $")

    def resultFunctionStatics(self, result):
        self.ui.pushButton_10.setEnabled(True)

    def showGard(self):
        self.ui.pushButton_11.setEnabled(False)
        worker = Worker(
            partial(
                self.start_gard,
            )
        )
        worker.signals.result.connect(partial(self.resultFunctionGard))
        self.threadpool.start(worker)

    def start_gard(self, progress_callback):
        num = 0
        total_in = 0
        total_out = 0
        predicted = 0
        theProducts = _services.get_products(_database.SessionLocal())
        if theProducts:
            for product in theProducts:
                num = num + int(product.num)
                total_in = total_in + (int(product.price_in) * int(product.num))
                total_out = total_out + (int(product.price_out) * int(product.num))
            predicted = total_out - total_in
        self.ui.label_84.setText(str(num))
        self.ui.label_82.setText(str(total_in))
        self.ui.label_80.setText(str(total_out))
        self.ui.label_54.setText(str(predicted))

    def resultFunctionGard(self, result):
        self.ui.pushButton_11.setEnabled(True)

    def showCharts(self):
        self.ui.stackedWidget_4.setCurrentIndex(0)

    def showOutCome(self):
        self.ui.stackedWidget_4.setCurrentIndex(1)

    def createOutPut(self):
        num = self.ui.add_color_line_2.text()
        disc = self.ui.add_color_line_3.text()
        if num and num != "" and num != " " and len(disc) > 0:
            payload = {
                "num": int(num),
                "disc": disc,
                "date": datetime.now(),
            }
            createPut = _services.create_output(
                _database.SessionLocal(), payload
            )
            if createPut:
                self.ui.add_color_line_2.setText("")
                self.ui.add_color_line_3.setText("")
                self.showOutPut()
                self.ui.feedback.setText("added successfully")
                self.ui.feedback.setStyleSheet(u"color: #00b359;")
        else:
            self.ui.feedback.setText("اظبط ياض")
            self.ui.feedback.setStyleSheet(u"color: #b90000;")

    def showOutPut(self):
        self.clear_tab(self.ui.verticalLayout_42)
        sizes = _services.get_outputs(_database.SessionLocal())
        from widgets.size_color_user.ui_color_size import SizeAndColor
        for i in (sizes[::-1]):
            self.ui.verticalLayout_42.addWidget(SizeAndColor(i.id, i.num, "output", i.disc, i.date))

        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum,
                                            QSizePolicy.Expanding)
        self.ui.verticalLayout_42.addItem(self.vertical_spacer2)

    def passDataToChart(self):
        
        _type = self.ui.color_sell_6.currentText()
        if _type == "Orders":
            self.SeriesNames = ["انتظار", "مقبول", "مرفوض"]
            
        if _type == "Sales":
            self.SeriesNames = ["البيع المتوقع", "البيع الفعلي", "قيمة ما تم رفضة"]
            
        if _type == "Income":
            self.SeriesNames = ["المكسب المتوقع", "المكسب الفعلي", "قيمة ما تم رفضة"]

        worker = Worker(
            partial(
                self.start_passingDataToChart,
            )
        )
        worker.signals.result.connect(partial(self.resultFunctionPassingData))
        self.threadpool.start(worker)

    def start_passingDataToChart(self, progress_callback):
        self.ui.color_sell_6.setEnabled(False)
        total_in = 0
        total_out = 0
        pieces_num = 0
        real = 0
        priceIn = 0
        predicted = 0
        rejected_out = 0
        rejectedIn = 0
        _type = self.ui.color_sell_6.currentText()
        self.ChartData = [
            [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        theSales = _services.get_all_sales( _database.SessionLocal())
        if theSales:
            for sales in theSales:
                # if sales.status != "مرفوض":
                if sales.date >= (datetime.now() - timedelta(days=int(360))):
                    if sales.status != "مرفوض":
                        total_in = total_in + int(sales.total)
                        total_out = total_out + int(sales.real_total)
                    if sales.status == "مرفوض":
                        rejected_out = rejected_out + int(sales.total)
                    if _type == "Orders":
                        if sales.status == "مرفوض":
                            self.ChartData[2][sales.date.month] += 1
                        if sales.status == "انتظار":
                            self.ChartData[0][sales.date.month] += 1
                        if sales.status == "مقبول":
                            self.ChartData[1][sales.date.month] += 1
                    
                    if _type == "Sales":
                        if sales.status == "مرفوض":
                            self.ChartData[2][sales.date.month] += sales.total
                        else:
                            self.ChartData[1][sales.date.month] += sales.total
                            self.ChartData[0][sales.date.month] += sales.real_total

                    if _type == "Income":
                        items = _services.get_sales_items(_database.SessionLocal(),sales.id)
                        for item in items:
                            pieces_num = pieces_num + int(item.num_of_products)
                            theProduct = _services.get_product_by_id(_database.SessionLocal(),item.product_id)
                            if theProduct:
                                if sales.status != "مرفوض": 
                                    real = real + int(item.price_out)
                                    priceIn = priceIn + int(theProduct.price_in)
                                    predicted = predicted + int(theProduct.price_out)
                                if sales.status == "مرفوض": 
                                    rejectedIn = rejectedIn + int(theProduct.price_in) 
            if _type == "Income":
                self.ChartData[0][sales.date.month] += (total_out - priceIn)
                self.ChartData[1][sales.date.month] += (total_in - priceIn)
                self.ChartData[2][sales.date.month] += (rejected_out - rejectedIn)


    def resultFunctionPassingData(self, result):
        self.clear_tab(self.ui.gridLayout_19)
        self.lineChart = PyLineChart(
            color="#343b48",
            bg_color="#343b48",
            line_color="#cd1234",
            data=self.ChartData,
            seriesNames = self.SeriesNames,
        )
        self.ui.gridLayout_19.addWidget(self.lineChart)
        self.ui.color_sell_6.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
