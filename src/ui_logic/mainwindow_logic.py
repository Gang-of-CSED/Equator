import sys
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from src.ui.mainwindow_ui import Ui_MainWindow as MainWindowUI
from PySide6.QtCore import SIGNAL
import numpy as np
from gauss_operations import gauss_elimination,gauss_Jordan
from src.operations.CroutLU import CroutLU
from CholeskyLU import Cholesky
class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.operation_index=0
        self.update_visiblity()
        self.update_labels()
        self.operationComboBox.connect(self.operationComboBox, SIGNAL("currentIndexChanged(int)"), self.comboBox_changed)
        self.solveButton.connect(self.solveButton, SIGNAL("clicked()"), self.solveButton_clicked)
        self.add_validatitors()
        self.noRowsLine.setText("3")
        self.noRowsLine.textChanged.connect(self.noRowsLine_changed)
        # change solutionErrorLabel to red
        self.solutionErrorLabel.setStyleSheet("QLabel { color : red; }")
    
    def comboBox_changed(self, index):
        self.operation_index=index
        self.update_visiblity()
        self.update_labels()
        print(index)
    
    def update_visiblity(self):
        if self.operation_index in [4,5,6]:
            self.vectorTable.setVisible(False)
        else:
            self.vectorTable.setVisible(True)
        
        # solutionMatrix_2
        if self.operation_index in [4,5,6]:
            self.solutionMatrix_2.setVisible(True)
        else:
            self.solutionMatrix_2.setVisible(False)
            
        # solutionLabel_2
        if self.operation_index in [4,5,6]:
            self.solutionLabel_2.setVisible(True)
        else:
            self.solutionLabel_2.setVisible(False)

        # parametersLabel
        if self.operation_index in [2,3]:
            self.parametersLabel.setVisible(True)
        else:
            self.parametersLabel.setVisible(False)
        
        # iteartionsLabel
        if self.operation_index in [2,3]:
            self.iteartionsLabel.setVisible(True)
        else:
            self.iteartionsLabel.setVisible(False)
        
        # iterationLine
        if self.operation_index in [2,3]:
            self.iterationLine.setVisible(True)
        else:
            self.iterationLine.setVisible(False)
        
        # errorLabel
        if self.operation_index in [2,3]:
            self.errorLabel.setVisible(True)
        else:
            self.errorLabel.setVisible(False)

        # errorLine
        if self.operation_index in [2,3]:
            self.errorLine.setVisible(True)
        else:
            self.errorLine.setVisible(False)
        
        # initialLabel
        if self.operation_index in [2,3]:
            self.initialLabel.setVisible(True)
        else:
            self.initialLabel.setVisible(False)
        
        # initialTable
        if self.operation_index in [2,3]:
            self.initialTable.setVisible(True)
        else:
            self.initialTable.setVisible(False)

        
    def solveButton_clicked(self):
        self.solutionErrorLabel.setText("")

        # get items from qt table to numpy array
        matrix_data = []
        for row in range(self.matrixTable.rowCount()):
            matrix_data.append([])
            for column in range(self.matrixTable.columnCount()):
                matrix_data[row].append(self.matrixTable.item(row, column).text())
        
        matrix_data = np.array(matrix_data).astype(np.float64)
    
        vector_data = []
        if self.operation_index in [0,1,2,3]:
            for row in range(self.vectorTable.rowCount()):
                vector_data.append([])
                for column in range(self.vectorTable.columnCount()):
                    print(row,column,self.vectorTable.itemAt(row,column))
                    vector_data[row].append(self.vectorTable.item(row,column).text())
            vector_data = np.array(vector_data).astype(np.float64)

        if self.operation_index == 0:
            # gauss elimination
            solvable,solution,steps = gauss_elimination(matrix_data,vector_data)
            print("solvable",solvable)
            if not solvable:
                self.solutionErrorLabel.setText("No Solution")
                return
            print(solution)
            print(steps)
            self.solutionMatrix_1.setRowCount(len(solution))
            self.solutionMatrix_1.setColumnCount(1)
            for i in range(len(solution)):
                self.solutionMatrix_1.setItem(i,0,QTableWidgetItem(str(solution[i])))
        
        if self.operation_index == 1:
            # gauss elimination
            solvable,solution,steps = gauss_Jordan(matrix_data,vector_data)
            if not solvable:
                self.solutionErrorLabel.setText("No Solution")
                return
            
            self.solutionMatrix_1.setRowCount(len(solution))
            self.solutionMatrix_1.setColumnCount(1)
            for i in range(len(solution)):
                self.solutionMatrix_1.setItem(i,0,QTableWidgetItem(str(solution[i])))
        
        if self.operation_index == 5:
            # crout LU
            output,steps = CroutLU(matrix_data)
            L= output[-1]['L']
            U= output[-1]['U']

            self.solutionMatrix_1.setRowCount(len(output))
            self.solutionMatrix_1.setColumnCount(len(output))
            self.solutionMatrix_2.setRowCount(len(output))
            self.solutionMatrix_2.setColumnCount(len(output))
            for i in range(len(output)):
                for j in range(len(output)):
                    self.solutionMatrix_1.setItem(i,j,QTableWidgetItem(str(L[i,j])))
                    self.solutionMatrix_2.setItem(i,j,QTableWidgetItem(str(U[i,j])))
        
        if self.operation_index == 6:
            # Cholesky LU
            output,steps = Cholesky(matrix_data)
            L=output
            if len(output)==0:
                self.solutionErrorLabel.setText("Non Symmetric Positive Definite Matrices")
                return
            print(L)
            U=np.transpose(output)
            print(U)
            self.solutionMatrix_1.setRowCount(len(output))
            self.solutionMatrix_1.setColumnCount(len(output))
            self.solutionMatrix_2.setRowCount(len(output))
            self.solutionMatrix_2.setColumnCount(len(output))
            for i in range(len(output)):
                for j in range(len(output)):
                    self.solutionMatrix_1.setItem(i,j,QTableWidgetItem(str(L[i][j])))
                    self.solutionMatrix_2.setItem(i,j,QTableWidgetItem(str(U[i][j])))


        
            
        
    def update_labels(self):
        if self.operation_index in [0,1,2,3]:
            self.solutionLabel_1.setText("X")
            self.matrixLabel.setText("Coefficient Matrix")
            self.vectorLabel.setText("Vector")
        
        if self.operation_index in [4,5,6]:
            self.solutionLabel_1.setText("L")
            self.matrixLabel.setText("Matrix")
            self.solutionLabel_2.setText("U")

        
    def add_validatitors(self):
        # add regex to make sure input is a float number
        number_regex = QRegularExpression("^[-+]?[0-9]*\.?[0-9]+$")
        input_validator = QRegularExpressionValidator(number_regex,self.errorLine)
        self.errorLine.setValidator(input_validator)
        self.noRowsLine.setValidator(input_validator)
        self.precisionLine.setValidator(input_validator)
        integer_regex = QRegularExpression("^[0-9]+$")
        integer_validator = QRegularExpressionValidator(integer_regex,self.iterationLine)
        self.iterationLine.setValidator(integer_validator)

        # add validator to matrix table
        self.matrixTable.cellChanged.connect(self.matrixTable_changed)
        self.vectorTable.cellChanged.connect(self.matrixTable_changed)
        self.initialTable.cellChanged.connect(self.matrixTable_changed)
        self.solutionMatrix_1.cellChanged.connect(self.matrixTable_changed)
        self.solutionMatrix_2.cellChanged.connect(self.matrixTable_changed)

    
    def matrixTable_changed(self,x,y):
        print(x,y,self.matrixTable.item(x,y).text())
        number_regex = QRegularExpression("^[-+]?[0-9]*\.?[0-9]+$")
        if not number_regex.match(self.matrixTable.item(x,y).text()).hasMatch():
            
            # force it to be a float number by remove any chracter not digit
            filterd_text=self.matrixTable.item(x,y).text()
            for i in range(len(filterd_text)-1,-1,-1):
                if i >= len(filterd_text):
                    continue
                print(filterd_text,i)
                if filterd_text[i] not in ['0','1','2','3','4','5','6','7','8','9']:
                    print("filtering",i)
                    filterd_text=filterd_text.replace(filterd_text[i],'')
            
            print(filterd_text)
            
            self.matrixTable.item(x,y).setText(filterd_text)
    
    def noRowsLine_changed(self):
        no_rows=int(self.noRowsLine.text())
        self.matrixTable.setRowCount(no_rows)
        self.matrixTable.setColumnCount(no_rows)
        self.vectorTable.setRowCount(no_rows)
        self.initialTable.setRowCount(no_rows)
        self.solutionMatrix_1.setRowCount(no_rows)
        self.solutionMatrix_1.setColumnCount(no_rows)
        self.solutionMatrix_2.setRowCount(no_rows)
        self.solutionMatrix_2.setColumnCount(no_rows)
        

        