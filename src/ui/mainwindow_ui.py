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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1110, 675)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabMatrix = QWidget()
        self.tabMatrix.setObjectName(u"tabMatrix")
        self.stepsButton = QPushButton(self.tabMatrix)
        self.stepsButton.setObjectName(u"stepsButton")
        self.stepsButton.setGeometry(QRect(440, 560, 151, 28))
        self.solutionErrorLabel = QLabel(self.tabMatrix)
        self.solutionErrorLabel.setObjectName(u"solutionErrorLabel")
        self.solutionErrorLabel.setGeometry(QRect(710, 20, 301, 16))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.solutionErrorLabel.setFont(font)
        self.precisionLine = QLineEdit(self.tabMatrix)
        self.precisionLine.setObjectName(u"precisionLine")
        self.precisionLine.setGeometry(QRect(440, 480, 151, 22))
        self.errorLabel = QLabel(self.tabMatrix)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(20, 430, 161, 21))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        self.errorLabel.setFont(font1)
        self.vectorLabel = QLabel(self.tabMatrix)
        self.vectorLabel.setObjectName(u"vectorLabel")
        self.vectorLabel.setGeometry(QRect(470, 30, 131, 16))
        font2 = QFont()
        font2.setBold(True)
        self.vectorLabel.setFont(font2)
        self.initialLabel = QLabel(self.tabMatrix)
        self.initialLabel.setObjectName(u"initialLabel")
        self.initialLabel.setGeometry(QRect(210, 340, 81, 21))
        self.initialLabel.setFont(font1)
        self.operationComboBox = QComboBox(self.tabMatrix)
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.addItem("")
        self.operationComboBox.setObjectName(u"operationComboBox")
        self.operationComboBox.setGeometry(QRect(440, 350, 151, 22))
        self.solutionLabel_1 = QLabel(self.tabMatrix)
        self.solutionLabel_1.setObjectName(u"solutionLabel_1")
        self.solutionLabel_1.setGeometry(QRect(710, 40, 121, 16))
        self.solutionLabel_1.setFont(font2)
        self.matrixLabel = QLabel(self.tabMatrix)
        self.matrixLabel.setObjectName(u"matrixLabel")
        self.matrixLabel.setGeometry(QRect(20, 30, 131, 16))
        self.matrixLabel.setFont(font2)
        self.solutionLabel = QLabel(self.tabMatrix)
        self.solutionLabel.setObjectName(u"solutionLabel")
        self.solutionLabel.setGeometry(QRect(700, 0, 55, 16))
        self.solutionLabel.setFont(font2)
        self.solveButton = QPushButton(self.tabMatrix)
        self.solveButton.setObjectName(u"solveButton")
        self.solveButton.setGeometry(QRect(440, 520, 151, 28))
        self.errorLine = QLineEdit(self.tabMatrix)
        self.errorLine.setObjectName(u"errorLine")
        self.errorLine.setGeometry(QRect(20, 460, 151, 22))
        self.parametersLabel = QLabel(self.tabMatrix)
        self.parametersLabel.setObjectName(u"parametersLabel")
        self.parametersLabel.setGeometry(QRect(140, 300, 81, 21))
        self.parametersLabel.setFont(font1)
        self.noRowsLabel = QLabel(self.tabMatrix)
        self.noRowsLabel.setObjectName(u"noRowsLabel")
        self.noRowsLabel.setGeometry(QRect(440, 390, 55, 16))
        self.noRowsLabel.setFont(font1)
        self.initialTable = QTableWidget(self.tabMatrix)
        if (self.initialTable.columnCount() < 1):
            self.initialTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.initialTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.initialTable.rowCount() < 3):
            self.initialTable.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.initialTable.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.initialTable.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.initialTable.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.initialTable.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.initialTable.setItem(1, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.initialTable.setItem(2, 0, __qtablewidgetitem6)
        self.initialTable.setObjectName(u"initialTable")
        self.initialTable.setGeometry(QRect(210, 370, 151, 231))
        self.initialTable.horizontalHeader().setVisible(False)
        self.initialTable.verticalHeader().setVisible(False)
        self.precisionLabel = QLabel(self.tabMatrix)
        self.precisionLabel.setObjectName(u"precisionLabel")
        self.precisionLabel.setGeometry(QRect(440, 450, 61, 16))
        self.precisionLabel.setFont(font1)
        self.solutionMatrix_1 = QTableWidget(self.tabMatrix)
        if (self.solutionMatrix_1.columnCount() < 1):
            self.solutionMatrix_1.setColumnCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.solutionMatrix_1.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        if (self.solutionMatrix_1.rowCount() < 3):
            self.solutionMatrix_1.setRowCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.solutionMatrix_1.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.solutionMatrix_1.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.solutionMatrix_1.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.solutionMatrix_1.setItem(0, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.solutionMatrix_1.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.solutionMatrix_1.setItem(2, 0, __qtablewidgetitem13)
        self.solutionMatrix_1.setObjectName(u"solutionMatrix_1")
        self.solutionMatrix_1.setGeometry(QRect(710, 70, 341, 231))
        self.solutionMatrix_1.setShowGrid(True)
        self.solutionMatrix_1.horizontalHeader().setVisible(False)
        self.solutionMatrix_1.verticalHeader().setVisible(False)
        self.iterationLine = QLineEdit(self.tabMatrix)
        self.iterationLine.setObjectName(u"iterationLine")
        self.iterationLine.setGeometry(QRect(20, 400, 151, 22))
        self.solutionMatrix_2 = QTableWidget(self.tabMatrix)
        if (self.solutionMatrix_2.columnCount() < 1):
            self.solutionMatrix_2.setColumnCount(1)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.solutionMatrix_2.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        if (self.solutionMatrix_2.rowCount() < 3):
            self.solutionMatrix_2.setRowCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.solutionMatrix_2.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.solutionMatrix_2.setVerticalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.solutionMatrix_2.setVerticalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.solutionMatrix_2.setItem(0, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.solutionMatrix_2.setItem(1, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.solutionMatrix_2.setItem(2, 0, __qtablewidgetitem20)
        self.solutionMatrix_2.setObjectName(u"solutionMatrix_2")
        self.solutionMatrix_2.setGeometry(QRect(710, 350, 341, 231))
        self.solutionMatrix_2.setShowGrid(True)
        self.solutionMatrix_2.horizontalHeader().setVisible(False)
        self.solutionMatrix_2.verticalHeader().setVisible(False)
        self.vectorTable = QTableWidget(self.tabMatrix)
        if (self.vectorTable.columnCount() < 1):
            self.vectorTable.setColumnCount(1)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.vectorTable.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        if (self.vectorTable.rowCount() < 3):
            self.vectorTable.setRowCount(3)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.vectorTable.setVerticalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.vectorTable.setVerticalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.vectorTable.setVerticalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.vectorTable.setItem(0, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.vectorTable.setItem(1, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.vectorTable.setItem(2, 0, __qtablewidgetitem27)
        self.vectorTable.setObjectName(u"vectorTable")
        self.vectorTable.setGeometry(QRect(470, 50, 151, 231))
        self.vectorTable.horizontalHeader().setVisible(False)
        self.vectorTable.verticalHeader().setVisible(False)
        self.solutionLabel_2 = QLabel(self.tabMatrix)
        self.solutionLabel_2.setObjectName(u"solutionLabel_2")
        self.solutionLabel_2.setGeometry(QRect(710, 320, 121, 16))
        self.solutionLabel_2.setFont(font2)
        self.themeButton = QPushButton(self.tabMatrix)
        self.themeButton.setObjectName(u"themeButton")
        self.themeButton.setGeometry(QRect(960, 0, 93, 28))
        self.themeButton.setFont(font2)
        self.matrixTable = QTableWidget(self.tabMatrix)
        if (self.matrixTable.columnCount() < 3):
            self.matrixTable.setColumnCount(3)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.matrixTable.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.matrixTable.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.matrixTable.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        if (self.matrixTable.rowCount() < 3):
            self.matrixTable.setRowCount(3)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.matrixTable.setVerticalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.matrixTable.setVerticalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.matrixTable.setVerticalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.matrixTable.setItem(0, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.matrixTable.setItem(0, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.matrixTable.setItem(0, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.matrixTable.setItem(1, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.matrixTable.setItem(1, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.matrixTable.setItem(1, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.matrixTable.setItem(2, 0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.matrixTable.setItem(2, 1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.matrixTable.setItem(2, 2, __qtablewidgetitem42)
        self.matrixTable.setObjectName(u"matrixTable")
        self.matrixTable.setGeometry(QRect(20, 50, 411, 231))
        self.matrixTable.horizontalHeader().setVisible(False)
        self.matrixTable.verticalHeader().setVisible(False)
        self.noRowsLine = QLineEdit(self.tabMatrix)
        self.noRowsLine.setObjectName(u"noRowsLine")
        self.noRowsLine.setGeometry(QRect(440, 420, 151, 22))
        self.iteartionsLabel = QLabel(self.tabMatrix)
        self.iteartionsLabel.setObjectName(u"iteartionsLabel")
        self.iteartionsLabel.setGeometry(QRect(20, 370, 101, 16))
        self.iteartionsLabel.setFont(font1)
        self.tabWidget.addTab(self.tabMatrix, "")
        self.tabRoot = QWidget()
        self.tabRoot.setObjectName(u"tabRoot")
        self.equationLineEdit = QLineEdit(self.tabRoot)
        self.equationLineEdit.setObjectName(u"equationLineEdit")
        self.equationLineEdit.setGeometry(QRect(20, 40, 351, 31))
        self.equationLabel = QLabel(self.tabRoot)
        self.equationLabel.setObjectName(u"equationLabel")
        self.equationLabel.setGeometry(QRect(20, 20, 55, 16))
        self.equationLabel.setFont(font2)
        self.input1Label = QLabel(self.tabRoot)
        self.input1Label.setObjectName(u"input1Label")
        self.input1Label.setGeometry(QRect(20, 120, 101, 16))
        self.input1Label.setFont(font2)
        self.input1LineEdit = QLineEdit(self.tabRoot)
        self.input1LineEdit.setObjectName(u"input1LineEdit")
        self.input1LineEdit.setGeometry(QRect(20, 140, 113, 22))
        self.input2LineEdit = QLineEdit(self.tabRoot)
        self.input2LineEdit.setObjectName(u"input2LineEdit")
        self.input2LineEdit.setGeometry(QRect(260, 140, 113, 22))
        self.input2Label = QLabel(self.tabRoot)
        self.input2Label.setObjectName(u"input2Label")
        self.input2Label.setGeometry(QRect(260, 120, 101, 16))
        self.input2Label.setFont(font2)
        self.iterationLine_root = QLineEdit(self.tabRoot)
        self.iterationLine_root.setObjectName(u"iterationLine_root")
        self.iterationLine_root.setGeometry(QRect(20, 300, 151, 22))
        self.iteartionsLabel_root = QLabel(self.tabRoot)
        self.iteartionsLabel_root.setObjectName(u"iteartionsLabel_root")
        self.iteartionsLabel_root.setGeometry(QRect(20, 270, 101, 16))
        self.iteartionsLabel_root.setFont(font1)
        self.errorLine_root = QLineEdit(self.tabRoot)
        self.errorLine_root.setObjectName(u"errorLine_root")
        self.errorLine_root.setGeometry(QRect(20, 360, 151, 22))
        self.errorLabel_root = QLabel(self.tabRoot)
        self.errorLabel_root.setObjectName(u"errorLabel_root")
        self.errorLabel_root.setGeometry(QRect(20, 330, 161, 21))
        self.errorLabel_root.setFont(font1)
        self.signLine_root = QLineEdit(self.tabRoot)
        self.signLine_root.setObjectName(u"signLine_root")
        self.signLine_root.setGeometry(QRect(20, 430, 151, 22))
        self.signLabel_root = QLabel(self.tabRoot)
        self.signLabel_root.setObjectName(u"signLabel_root")
        self.signLabel_root.setGeometry(QRect(20, 400, 161, 21))
        self.signLabel_root.setFont(font1)
        self.operationComboBox_root = QComboBox(self.tabRoot)
        self.operationComboBox_root.addItem("")
        self.operationComboBox_root.addItem("")
        self.operationComboBox_root.addItem("")
        self.operationComboBox_root.addItem("")
        self.operationComboBox_root.addItem("")
        self.operationComboBox_root.addItem("")
        self.operationComboBox_root.setObjectName(u"operationComboBox_root")
        self.operationComboBox_root.setGeometry(QRect(220, 300, 151, 22))
        self.stepsButton_root = QPushButton(self.tabRoot)
        self.stepsButton_root.setObjectName(u"stepsButton_root")
        self.stepsButton_root.setGeometry(QRect(220, 430, 151, 28))
        self.solveButton_root = QPushButton(self.tabRoot)
        self.solveButton_root.setObjectName(u"solveButton_root")
        self.solveButton_root.setGeometry(QRect(220, 390, 151, 28))
        self.plotButton = QPushButton(self.tabRoot)
        self.plotButton.setObjectName(u"plotButton")
        self.plotButton.setGeometry(QRect(220, 350, 151, 28))
        self.rootLineEdit = QLineEdit(self.tabRoot)
        self.rootLineEdit.setObjectName(u"rootLineEdit")
        self.rootLineEdit.setGeometry(QRect(110, 230, 171, 21))
        self.rootLineEdit.setReadOnly(True)
        self.rootLabel = QLabel(self.tabRoot)
        self.rootLabel.setObjectName(u"rootLabel")
        self.rootLabel.setGeometry(QRect(110, 200, 55, 16))
        self.rootLabel.setFont(font2)
        self.plotWidget = QWidget(self.tabRoot)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setGeometry(QRect(470, 40, 601, 401))
        self.plotLabel = QLabel(self.tabRoot)
        self.plotLabel.setObjectName(u"plotLabel")
        self.plotLabel.setGeometry(QRect(470, 20, 55, 16))
        self.plotLabel.setFont(font2)
        self.range2Label = QLabel(self.tabRoot)
        self.range2Label.setObjectName(u"range2Label")
        self.range2Label.setGeometry(QRect(710, 470, 101, 16))
        self.range2Label.setFont(font2)
        self.range1LineEdit = QLineEdit(self.tabRoot)
        self.range1LineEdit.setObjectName(u"range1LineEdit")
        self.range1LineEdit.setGeometry(QRect(470, 490, 113, 22))
        self.range1Label = QLabel(self.tabRoot)
        self.range1Label.setObjectName(u"range1Label")
        self.range1Label.setGeometry(QRect(470, 470, 101, 16))
        self.range1Label.setFont(font2)
        self.range2LineEdit = QLineEdit(self.tabRoot)
        self.range2LineEdit.setObjectName(u"range2LineEdit")
        self.range2LineEdit.setGeometry(QRect(710, 490, 113, 22))
        self.solutionErrorLabel_root = QLabel(self.tabRoot)
        self.solutionErrorLabel_root.setObjectName(u"solutionErrorLabel_root")
        self.solutionErrorLabel_root.setGeometry(QRect(20, 80, 411, 31))
        self.solutionErrorLabel_root.setFont(font)
        self.tabWidget.addTab(self.tabRoot, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Equator", None))
        self.stepsButton.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.solutionErrorLabel.setText("")
        self.errorLabel.setText(QCoreApplication.translate("MainWindow", u"Absolute Relative Error", None))
        self.vectorLabel.setText(QCoreApplication.translate("MainWindow", u"vector_label", None))
        self.initialLabel.setText(QCoreApplication.translate("MainWindow", u"Initial Vector", None))
        self.operationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gauss Elimination", None))
        self.operationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Gauss-Jordan", None))
        self.operationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Gauss-Seidel ", None))
        self.operationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Jacobi-Iteration", None))
        self.operationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Doolittle Decomposition", None))
        self.operationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Crout Decomposition", None))
        self.operationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Cholesky Decomposition", None))

        self.solutionLabel_1.setText(QCoreApplication.translate("MainWindow", u"solution1_label", None))
        self.matrixLabel.setText(QCoreApplication.translate("MainWindow", u"matrix_label", None))
        self.solutionLabel.setText(QCoreApplication.translate("MainWindow", u"Solution:", None))
        self.solveButton.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.parametersLabel.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.noRowsLabel.setText(QCoreApplication.translate("MainWindow", u"No. rows", None))
        ___qtablewidgetitem = self.initialTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem1 = self.initialTable.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.initialTable.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.initialTable.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled = self.initialTable.isSortingEnabled()
        self.initialTable.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.initialTable.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.initialTable.item(1, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem6 = self.initialTable.item(2, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.initialTable.setSortingEnabled(__sortingEnabled)

        self.precisionLabel.setText(QCoreApplication.translate("MainWindow", u"Precision", None))
        ___qtablewidgetitem7 = self.solutionMatrix_1.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.solutionMatrix_1.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem9 = self.solutionMatrix_1.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled1 = self.solutionMatrix_1.isSortingEnabled()
        self.solutionMatrix_1.setSortingEnabled(False)
        self.solutionMatrix_1.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem10 = self.solutionMatrix_2.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem11 = self.solutionMatrix_2.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem12 = self.solutionMatrix_2.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled2 = self.solutionMatrix_2.isSortingEnabled()
        self.solutionMatrix_2.setSortingEnabled(False)
        self.solutionMatrix_2.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem13 = self.vectorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem14 = self.vectorTable.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem15 = self.vectorTable.verticalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem16 = self.vectorTable.verticalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled3 = self.vectorTable.isSortingEnabled()
        self.vectorTable.setSortingEnabled(False)
        ___qtablewidgetitem17 = self.vectorTable.item(0, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem18 = self.vectorTable.item(1, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem19 = self.vectorTable.item(2, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.vectorTable.setSortingEnabled(__sortingEnabled3)

        self.solutionLabel_2.setText(QCoreApplication.translate("MainWindow", u"solution1_label", None))
        self.themeButton.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        ___qtablewidgetitem20 = self.matrixTable.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem21 = self.matrixTable.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem22 = self.matrixTable.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem23 = self.matrixTable.verticalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem24 = self.matrixTable.verticalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem25 = self.matrixTable.verticalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"3", None));

        __sortingEnabled4 = self.matrixTable.isSortingEnabled()
        self.matrixTable.setSortingEnabled(False)
        ___qtablewidgetitem26 = self.matrixTable.item(0, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem27 = self.matrixTable.item(0, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem28 = self.matrixTable.item(0, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem29 = self.matrixTable.item(1, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem30 = self.matrixTable.item(1, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem31 = self.matrixTable.item(1, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem32 = self.matrixTable.item(2, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem33 = self.matrixTable.item(2, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem34 = self.matrixTable.item(2, 2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"9", None));
        self.matrixTable.setSortingEnabled(__sortingEnabled4)

        self.iteartionsLabel.setText(QCoreApplication.translate("MainWindow", u"Max iterations", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMatrix), QCoreApplication.translate("MainWindow", u"Solve System of Eauations", None))
        self.equationLabel.setText(QCoreApplication.translate("MainWindow", u"Function", None))
        self.input1Label.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.input1LineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.input2LineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.input2Label.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.iterationLine_root.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.iteartionsLabel_root.setText(QCoreApplication.translate("MainWindow", u"Max iterations", None))
        self.errorLine_root.setText(QCoreApplication.translate("MainWindow", u"0.0001", None))
        self.errorLabel_root.setText(QCoreApplication.translate("MainWindow", u"Relative Error", None))
        self.signLine_root.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.signLabel_root.setText(QCoreApplication.translate("MainWindow", u"Signifcant Digits", None))
        self.operationComboBox_root.setItemText(0, QCoreApplication.translate("MainWindow", u"Bisection", None))
        self.operationComboBox_root.setItemText(1, QCoreApplication.translate("MainWindow", u"False-Position", None))
        self.operationComboBox_root.setItemText(2, QCoreApplication.translate("MainWindow", u"Fixed point", None))
        self.operationComboBox_root.setItemText(3, QCoreApplication.translate("MainWindow", u"Original Newton-Raphson", None))
        self.operationComboBox_root.setItemText(4, QCoreApplication.translate("MainWindow", u"Modified Newton-Raphson", None))
        self.operationComboBox_root.setItemText(5, QCoreApplication.translate("MainWindow", u"Secant Method", None))

        self.stepsButton_root.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.solveButton_root.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.rootLabel.setText(QCoreApplication.translate("MainWindow", u"Root", None))
        self.plotLabel.setText(QCoreApplication.translate("MainWindow", u"PLot", None))
        self.range2Label.setText(QCoreApplication.translate("MainWindow", u"max X", None))
        self.range1Label.setText(QCoreApplication.translate("MainWindow", u"min X", None))
        self.solutionErrorLabel_root.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRoot), QCoreApplication.translate("MainWindow", u"Find Root", None))
    # retranslateUi

