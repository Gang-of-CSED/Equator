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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1107, 622)
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
        self.matrixTable.setGeometry(QRect(30, 60, 411, 231))
        self.matrixTable.horizontalHeader().setVisible(False)
        self.matrixTable.verticalHeader().setVisible(False)
        self.operationComboBox = QComboBox(self.centralwidget)
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.setObjectName(u"operationComboBox")
        self.operationComboBox.setGeometry(QRect(450, 360, 151, 22))
        self.solveButton = QPushButton(self.centralwidget)
        self.solveButton.setObjectName(u"solveButton")
        self.solveButton.setGeometry(QRect(450, 530, 151, 28))
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
        __qtablewidgetitem19 = QTableWidgetItem()
        self.vectorTable.setItem(0, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.vectorTable.setItem(1, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.vectorTable.setItem(2, 0, __qtablewidgetitem21)
        self.vectorTable.setObjectName(u"vectorTable")
        self.vectorTable.setGeometry(QRect(480, 60, 151, 231))
        self.vectorTable.horizontalHeader().setVisible(False)
        self.vectorTable.verticalHeader().setVisible(False)
        self.solutionLabel = QLabel(self.centralwidget)
        self.solutionLabel.setObjectName(u"solutionLabel")
        self.solutionLabel.setGeometry(QRect(710, 10, 55, 16))
        font = QFont()
        font.setBold(True)
        self.solutionLabel.setFont(font)
        self.solutionMatrix_1 = QTableWidget(self.centralwidget)
        if (self.solutionMatrix_1.columnCount() < 1):
            self.solutionMatrix_1.setColumnCount(1)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.solutionMatrix_1.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        if (self.solutionMatrix_1.rowCount() < 3):
            self.solutionMatrix_1.setRowCount(3)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.solutionMatrix_1.setVerticalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.solutionMatrix_1.setVerticalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.solutionMatrix_1.setVerticalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.solutionMatrix_1.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.solutionMatrix_1.setItem(1, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.solutionMatrix_1.setItem(2, 0, __qtablewidgetitem28)
        self.solutionMatrix_1.setObjectName(u"solutionMatrix_1")
        self.solutionMatrix_1.setGeometry(QRect(720, 80, 341, 231))
        self.solutionMatrix_1.setShowGrid(True)
        self.solutionMatrix_1.horizontalHeader().setVisible(False)
        self.solutionMatrix_1.verticalHeader().setVisible(False)
        self.noRowsLabel = QLabel(self.centralwidget)
        self.noRowsLabel.setObjectName(u"noRowsLabel")
        self.noRowsLabel.setGeometry(QRect(450, 400, 55, 16))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        self.noRowsLabel.setFont(font1)
        self.noRowsLine = QLineEdit(self.centralwidget)
        self.noRowsLine.setObjectName(u"noRowsLine")
        self.noRowsLine.setGeometry(QRect(450, 430, 151, 22))
        self.precisionLine = QLineEdit(self.centralwidget)
        self.precisionLine.setObjectName(u"precisionLine")
        self.precisionLine.setGeometry(QRect(450, 490, 151, 22))
        self.precisionLabel = QLabel(self.centralwidget)
        self.precisionLabel.setObjectName(u"precisionLabel")
        self.precisionLabel.setGeometry(QRect(450, 460, 55, 16))
        self.precisionLabel.setFont(font1)
        self.parametersLabel = QLabel(self.centralwidget)
        self.parametersLabel.setObjectName(u"parametersLabel")
        self.parametersLabel.setGeometry(QRect(150, 310, 81, 21))
        self.parametersLabel.setFont(font1)
        self.initialTable = QTableWidget(self.centralwidget)
        if (self.initialTable.columnCount() < 1):
            self.initialTable.setColumnCount(1)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.initialTable.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        if (self.initialTable.rowCount() < 3):
            self.initialTable.setRowCount(3)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.initialTable.setVerticalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.initialTable.setVerticalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.initialTable.setVerticalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.initialTable.setItem(0, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.initialTable.setItem(1, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.initialTable.setItem(2, 0, __qtablewidgetitem35)
        self.initialTable.setObjectName(u"initialTable")
        self.initialTable.setGeometry(QRect(220, 380, 151, 231))
        self.initialTable.horizontalHeader().setVisible(False)
        self.initialTable.verticalHeader().setVisible(False)
        self.initialLabel = QLabel(self.centralwidget)
        self.initialLabel.setObjectName(u"initialLabel")
        self.initialLabel.setGeometry(QRect(220, 350, 81, 21))
        self.initialLabel.setFont(font1)
        self.iterationLine = QLineEdit(self.centralwidget)
        self.iterationLine.setObjectName(u"iterationLine")
        self.iterationLine.setGeometry(QRect(30, 410, 151, 22))
        self.errorLabel = QLabel(self.centralwidget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(30, 440, 161, 21))
        self.errorLabel.setFont(font1)
        self.errorLine = QLineEdit(self.centralwidget)
        self.errorLine.setObjectName(u"errorLine")
        self.errorLine.setGeometry(QRect(30, 470, 151, 22))
        self.iteartionsLabel = QLabel(self.centralwidget)
        self.iteartionsLabel.setObjectName(u"iteartionsLabel")
        self.iteartionsLabel.setGeometry(QRect(30, 380, 101, 16))
        self.iteartionsLabel.setFont(font1)
        self.solutionLabel_1 = QLabel(self.centralwidget)
        self.solutionLabel_1.setObjectName(u"solutionLabel_1")
        self.solutionLabel_1.setGeometry(QRect(720, 50, 121, 16))
        self.solutionLabel_1.setFont(font)
        self.solutionLabel_2 = QLabel(self.centralwidget)
        self.solutionLabel_2.setObjectName(u"solutionLabel_2")
        self.solutionLabel_2.setGeometry(QRect(720, 330, 121, 16))
        self.solutionLabel_2.setFont(font)
        self.solutionMatrix_2 = QTableWidget(self.centralwidget)
        if (self.solutionMatrix_2.columnCount() < 1):
            self.solutionMatrix_2.setColumnCount(1)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.solutionMatrix_2.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        if (self.solutionMatrix_2.rowCount() < 3):
            self.solutionMatrix_2.setRowCount(3)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.solutionMatrix_2.setVerticalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.solutionMatrix_2.setVerticalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.solutionMatrix_2.setVerticalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.solutionMatrix_2.setItem(0, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.solutionMatrix_2.setItem(1, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.solutionMatrix_2.setItem(2, 0, __qtablewidgetitem42)
        self.solutionMatrix_2.setObjectName(u"solutionMatrix_2")
        self.solutionMatrix_2.setGeometry(QRect(720, 360, 341, 231))
        self.solutionMatrix_2.setShowGrid(True)
        self.solutionMatrix_2.horizontalHeader().setVisible(False)
        self.solutionMatrix_2.verticalHeader().setVisible(False)
        self.matrixLabel = QLabel(self.centralwidget)
        self.matrixLabel.setObjectName(u"matrixLabel")
        self.matrixLabel.setGeometry(QRect(30, 40, 131, 16))
        self.matrixLabel.setFont(font)
        self.vectorLabel = QLabel(self.centralwidget)
        self.vectorLabel.setObjectName(u"vectorLabel")
        self.vectorLabel.setGeometry(QRect(480, 40, 131, 16))
        self.vectorLabel.setFont(font)
        self.solutionErrorLabel = QLabel(self.centralwidget)
        self.solutionErrorLabel.setObjectName(u"solutionErrorLabel")
        self.solutionErrorLabel.setGeometry(QRect(720, 30, 301, 16))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.solutionErrorLabel.setFont(font2)
        self.themeButton = QPushButton(self.centralwidget)
        self.themeButton.setObjectName(u"themeButton")
        self.themeButton.setGeometry(QRect(970, 10, 93, 28))
        self.themeButton.setFont(font)
        self.stepsButton = QPushButton(self.centralwidget)
        self.stepsButton.setObjectName(u"stepsButton")
        self.stepsButton.setGeometry(QRect(450, 570, 151, 28))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Equator", None))
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
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem17 = self.vectorTable.verticalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem18 = self.vectorTable.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled1 = self.vectorTable.isSortingEnabled()
        self.vectorTable.setSortingEnabled(False)
        ___qtablewidgetitem19 = self.vectorTable.item(0, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem20 = self.vectorTable.item(1, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem21 = self.vectorTable.item(2, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.vectorTable.setSortingEnabled(__sortingEnabled1)

        self.solutionLabel.setText(QCoreApplication.translate("MainWindow", u"Solution:", None))
        ___qtablewidgetitem22 = self.solutionMatrix_1.verticalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem23 = self.solutionMatrix_1.verticalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem24 = self.solutionMatrix_1.verticalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled2 = self.solutionMatrix_1.isSortingEnabled()
        self.solutionMatrix_1.setSortingEnabled(False)
        self.solutionMatrix_1.setSortingEnabled(__sortingEnabled2)

        self.noRowsLabel.setText(QCoreApplication.translate("MainWindow", u"No. rows", None))
        self.precisionLabel.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
        self.parametersLabel.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        ___qtablewidgetitem25 = self.initialTable.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem26 = self.initialTable.verticalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem27 = self.initialTable.verticalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem28 = self.initialTable.verticalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled3 = self.initialTable.isSortingEnabled()
        self.initialTable.setSortingEnabled(False)
        ___qtablewidgetitem29 = self.initialTable.item(0, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem30 = self.initialTable.item(1, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem31 = self.initialTable.item(2, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.initialTable.setSortingEnabled(__sortingEnabled3)

        self.initialLabel.setText(QCoreApplication.translate("MainWindow", u"Initial Vector", None))
        self.errorLabel.setText(QCoreApplication.translate("MainWindow", u"Absolute Relative Error", None))
        self.iteartionsLabel.setText(QCoreApplication.translate("MainWindow", u"Max iterations", None))
        self.solutionLabel_1.setText(QCoreApplication.translate("MainWindow", u"solution1_label", None))
        self.solutionLabel_2.setText(QCoreApplication.translate("MainWindow", u"solution1_label", None))
        ___qtablewidgetitem32 = self.solutionMatrix_2.verticalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem33 = self.solutionMatrix_2.verticalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem34 = self.solutionMatrix_2.verticalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled4 = self.solutionMatrix_2.isSortingEnabled()
        self.solutionMatrix_2.setSortingEnabled(False)
        self.solutionMatrix_2.setSortingEnabled(__sortingEnabled4)

        self.matrixLabel.setText(QCoreApplication.translate("MainWindow", u"matrix_label", None))
        self.vectorLabel.setText(QCoreApplication.translate("MainWindow", u"vector_label", None))
        self.solutionErrorLabel.setText("")
        self.themeButton.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.stepsButton.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
    # retranslateUi

