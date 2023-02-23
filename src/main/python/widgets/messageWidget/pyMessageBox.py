
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont)
from PySide6.QtWidgets import (QDialog, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout)

# from widgets.buttonIcon.pyIconButton import  PyIconB
# from widgets.buttonIcon.pyIconButton import Functions, PyIconB

stateErrorMessage = False
class PyMessageBox(QDialog):
    def __init__(
        self,
        width = 323,
        height = 176,
        title = 'Wave app message',
        message = 'details of the message',
        info ='Extra details of the message with instructions and more information and even a possible link to more info',
        buttonRight = "مقبول",
        buttonLeft = "مرفوض",
        icon = "info.png"
    ):
        super().__init__()
        # this will hide the title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self._buttonRight = buttonRight
        self._buttonLeft = buttonLeft
        self._title = title
        self._message = message
        self._info = info
        self._state = stateErrorMessage
        self.resize(width, height)
        self.setStyleSheet(u"border-radius:10px")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(36, 40, 47);\n"
        "border-radius:0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(40, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 82, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 9, 0)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Cascadia Code"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
        "")
        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(166, 166, 166);")
        self.label_3.setMaximumWidth(220)
        self.label_3.setWordWrap(True)   
        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(40, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 82, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 82))
        self.frame.setMaximumSize(QSize(16777215, 82))
        self.frame.setStyleSheet(u"background-color: rgb(25, 28, 34);\n"
        "border-radius:0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(55, 58, 63);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius:20px;")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 41))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(81, 195, 223);\n"
        "border-radius:20px")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)

        self.pushButton_2.setFont(font2)
        self.pushButton.setFont(font2)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.frame)
        
        #////////////// icons
             
        # EXIT
        self.close_btn = QPushButton(self.frame)
        
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(0, 41))
        self.close_btn.setText("x")
        self.close_btn.setStyleSheet(u"color:#dd0000;\n"
        "border-radius:20px")
        font12 = QFont()
        font12.setPointSize(12)
        self.close_btn.setFont(font12)
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        # self.close_btn = PyIconB(
        #     self,
        #     bg_color="#414449",
        #     bg_color_hover="#414449",
        #     bg_color_pressed="#414449",
        #     icon_color="#B1B1B1",
        #     icon_color_hover="#CC4656",
        #     icon_color_pressed="#FFFFFF",
        #     icon_color_active="#CC4656",
        #     context_color="#34393C",
        #     radius=15,
        #     # icon_path=Functions.set_svg_icon("close_small.svg"),
        # )
        self.verticalLayout_4.insertWidget(0, self.close_btn)

        # INFO
        # self.info_btn = PyIconB(
        #     self,
        #     bg_color="#24282f",
        #     bg_color_hover="#24282f",
        #     bg_color_pressed="#24282f",
        #     icon_color="#B1B1B1",
        #     icon_color_hover="#B1B1B1",
        #     icon_color_pressed="#B1B1B1",
        #     icon_color_active="#B1B1B1",
        #     context_color="#34393C",
        #     radius=15,
        #     # icon_path=Functions.set_svg_icon(icon),
        # )
        # self.verticalLayout_3.insertWidget(0, self.info_btn)

        self.pushButton.clicked.connect(self.pushButtonLeftFun)
        self.pushButton_2.clicked.connect(self.pushButtonRightFun)
        self.close_btn.clicked.connect(self.pushButtonClose)
        
        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        self.exec_()

    # setupUi


    def mouseMoveEvent(self, event):

        if self.isMouseDown:
            mousePoint = event.globalPos()
            self.move(mousePoint + self.positionDifference)

    def mousePressEvent(self, event):
        self.isMouseDown = True
        self.positionDifference = self.pos() - event.globalPos()

    def mouseReleaseEvent(self, event):
        self.isMouseDown = False

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", self._title, None))
        self.label_2.setText(QCoreApplication.translate("Dialog", self._message, None))
        self.label_3.setText(QCoreApplication.translate("Dialog", self._info, None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", self._buttonRight, None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", self._buttonLeft, None))
    # retranslateUi
    def pushButtonRightFun(self):
        global stateErrorMessage 
        stateErrorMessage = True
        self._state = stateErrorMessage

        self.close()
    def pushButtonLeftFun(self):
        global stateErrorMessage 
        stateErrorMessage = "False"
        self._state = stateErrorMessage
        self.close()

    def pushButtonClose(self):
        global stateErrorMessage 
        stateErrorMessage = None
        self._state = stateErrorMessage
        self.close()
    def theStateOfTheMessaheBox(self):
        return stateErrorMessage