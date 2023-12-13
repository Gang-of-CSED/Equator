import sys
from PySide6.QtWidgets import QMainWindow
from src.ui.mainwindow_ui import Ui_MainWindow as MainWindowUI
from PySide6.QtCore import SIGNAL

class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.operation_index=0
        self.update_visiblity()
        self.operationComboBox.connect(self.operationComboBox, SIGNAL("currentIndexChanged(int)"), self.comboBox_changed)
        self.solveButton.connect(self.solveButton, SIGNAL("clicked()"), self.solveButton_clicked)
    
    def comboBox_changed(self, index):
        self.operation_index=index
        self.update_visiblity()
        print(index)
    
    def update_visiblity(self):
        if self.operation_index in [4,5,6]:
            self.vectorTable.setVisible(False)
        else:
            self.vectorTable.setVisible(True)
    
    def solveButton_clicked(self):
        print("Solve button clicked")