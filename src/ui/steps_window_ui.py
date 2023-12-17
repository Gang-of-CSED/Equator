# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'steps_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QSizePolicy,
    QStackedWidget, QTextBrowser, QWidget)

class Ui_stepsDialog(object):
    def setupUi(self, stepsDialog):
        if not stepsDialog.objectName():
            stepsDialog.setObjectName(u"stepsDialog")
        stepsDialog.resize(759, 535)
        self.gridLayout = QGridLayout(stepsDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(stepsDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.textBrowser = QTextBrowser(self.page)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 741, 151))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(stepsDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(stepsDialog)
    # setupUi

    def retranslateUi(self, stepsDialog):
        stepsDialog.setWindowTitle(QCoreApplication.translate("stepsDialog", u"Steps", None))
    # retranslateUi

