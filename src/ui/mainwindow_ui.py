# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 485)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.matrixTable = QTableWidget(self.centralwidget)
        if (self.matrixTable.columnCount() < 3):
            self.matrixTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.matrixTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.matrixTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.matrixTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.matrixTable.rowCount() < 3):
            self.matrixTable.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.matrixTable.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.matrixTable.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.matrixTable.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.matrixTable.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.matrixTable.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.matrixTable.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.matrixTable.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.matrixTable.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.matrixTable.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.matrixTable.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.matrixTable.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.matrixTable.setItem(2, 2, __qtablewidgetitem14)
        self.matrixTable.setObjectName(u"matrixTable")
        self.matrixTable.setGeometry(QRect(30, 60, 401, 161))
        self.operationComboBox = QComboBox(self.centralwidget)
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.setObjectName(u"operationComboBox")
        self.operationComboBox.setGeometry(QRect(650, 290, 151, 22))
        self.solveButton = QPushButton(self.centralwidget)
        self.solveButton.setObjectName(u"solveButton")
        self.solveButton.setGeometry(QRect(650, 370, 151, 28))
        self.vectorTable = QTableWidget(self.centralwidget)
        if (self.vectorTable.columnCount() < 1):
            self.vectorTable.setColumnCount(1)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.vectorTable.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        if (self.vectorTable.rowCount() < 3):
            self.vectorTable.setRowCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.vectorTable.setVerticalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.vectorTable.setVerticalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.vectorTable.setVerticalHeaderItem(2, __qtablewidgetitem18)
        self.vectorTable.setObjectName(u"vectorTable")
        self.vectorTable.setGeometry(QRect(450, 60, 151, 151))
        self.solutionLabel = QLabel(self.centralwidget)
        self.solutionLabel.setObjectName(u"solutionLabel")
        self.solutionLabel.setGeometry(QRect(650, 30, 55, 16))
        self.solutionMatrix = QTableWidget(self.centralwidget)
        if (self.solutionMatrix.columnCount() < 1):
            self.solutionMatrix.setColumnCount(1)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.solutionMatrix.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        if (self.solutionMatrix.rowCount() < 3):
            self.solutionMatrix.setRowCount(3)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.solutionMatrix.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.solutionMatrix.setVerticalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.solutionMatrix.setVerticalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.solutionMatrix.setItem(0, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.solutionMatrix.setItem(1, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.solutionMatrix.setItem(2, 0, __qtablewidgetitem25)
        self.solutionMatrix.setObjectName(u"solutionMatrix")
        self.solutionMatrix.setGeometry(QRect(650, 60, 231, 161))
        self.solutionMatrix.setShowGrid(True)
        self.solutionMatrix.horizontalHeader().setVisible(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.matrixTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem1 = self.matrixTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem2 = self.matrixTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem3 = self.matrixTable.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem4 = self.matrixTable.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem5 = self.matrixTable.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled = self.matrixTable.isSortingEnabled()
        self.matrixTable.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.matrixTable.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem7 = self.matrixTable.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem8 = self.matrixTable.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem9 = self.matrixTable.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem10 = self.matrixTable.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem11 = self.matrixTable.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem12 = self.matrixTable.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem13 = self.matrixTable.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem14 = self.matrixTable.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.matrixTable.setSortingEnabled(__sortingEnabled)

        self.operationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gauss Elimination", None))
        self.operationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Gauss-Jordan", None))
        self.operationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Gauss-Seidel ", None))
        self.operationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Jacobi-Iteration", None))
        self.operationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Doolittle Decomposition", None))
        self.operationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Crout Decomposition", None))
        self.operationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Cholesky Decomposition", None))

        self.solveButton.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        ___qtablewidgetitem15 = self.vectorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem16 = self.vectorTable.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem17 = self.vectorTable.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem18 = self.vectorTable.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        self.solutionLabel.setText(QCoreApplication.translate("MainWindow", u"Solution:", None))
        ___qtablewidgetitem19 = self.solutionMatrix.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem20 = self.solutionMatrix.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem21 = self.solutionMatrix.verticalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem22 = self.solutionMatrix.verticalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"x3", None));

        __sortingEnabled1 = self.solutionMatrix.isSortingEnabled()
        self.solutionMatrix.setSortingEnabled(False)
        self.solutionMatrix.setSortingEnabled(__sortingEnabled1)

    # retranslateUi

