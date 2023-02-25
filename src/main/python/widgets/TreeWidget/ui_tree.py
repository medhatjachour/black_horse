# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treeInWpTP.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QTimer,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QSizePolicy,QSpacerItem,
    QWidget)
from ui_child import PY_TreeChild
class PY_TreeWidget(QFrame):
    def __init__(
        self,
        id = 1,
        data = 
            {"first":{"f1":"se",
                 "f12":{"se":"third level","s2":"third level2","s3":"third level3",},
                 "f3":"se",},
             "second":{"f23":"se",
                 "f22":{"se":"third level","se":"third level","se":"third level",}
                 },
             "third":{"f33":"se3"}
            },
    ):
        super().__init__()
        self._id = id
        self._data = data
        self.setObjectName(u"self")
        self.resize(393, 314)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        QMetaObject.connectSlotsByName(self)
        self.title = PY_TreeChild({},{}, 0)
        self.gridLayout_2.addWidget(self.title)
        self.id = 0

        
        for i in self._data.keys():
            from ui_parent import PY_TreeParent
            self.parent = PY_TreeParent(self.id ,self._data)
            self.id += 1
            self.gridLayout_2.addWidget(self.parent)
            
        self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(self.vertical_spacer2)
        
        self.old_data = {} 
        ####### here to update the the tree every 3000 ms == 3 s if the data i changed
        # self.liveDataFun()
        # self._plot_timer = QTimer()
        # self._plot_timer.timeout.connect(self.liveDataFun)
        # self._plot_timer.start(int(3000))
        # # /////////////////////////////////////////////////////////// clearing taps
    def clear_tab(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    def liveDataFun(self):
        if self.old_data != self._data:
            self.clear_tab(self.gridLayout_2)
            for i in self._data.keys():
                from ui_parent import PY_TreeParent
                self.parent = PY_TreeParent(self.id ,self._data)
                self.id += 1
                self.gridLayout_2.addWidget(self.parent)
                
            self.vertical_spacer2 = QSpacerItem(20, 104, QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.gridLayout_2.addItem(self.vertical_spacer2)
            self.old_data = self._data

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PY_TreeWidget()
    window.show()
    sys.exit(app.exec())
