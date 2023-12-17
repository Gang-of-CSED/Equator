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
from src.operations.Gauss_Seidel_Method import gauss_seidel_method
from src.operations.Gacobi_Method import gacobi_method
from PySide6.QtGui import QColor
from src.ui_logic.steps_window_logic import StepsWindow

import time

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
        self.color_theme = "Light"
        self.update_color_theme()

        self.themeButton.clicked.connect(self.themeButton_clicked)
        self.stepsButton.clicked.connect(self.stepsButton_clicked)
        self.output=[]
        self.comments=[]
        # #1c284f
    def themeButton_clicked(self):
        self.themeButton.setText(self.color_theme)
        if self.color_theme == "Light":
            self.color_theme = "Dark"
        else:
            self.color_theme = "Light"
        self.update_color_theme()


    def update_color_theme(self):
        background_color = "#FFFFFF"
        text_color = "#000000"
        table_color = "#f5f6f8"
        input_color = "#f5f6f8"
        label_color = "#69B6E3"
        error_color = "#b13600"
        cells_border="#e2e2f1"
        if self.color_theme == "Dark":
            background_color = "#14171d"
            text_color = "#FFFFFF"
            cells_border="#FFFFFF"
            table_color = "#1b1e25"
            input_color = "#21252c"
            label_color = "rgb( 84, 105, 212 )"
            error_color = "#f27400"
        
        
        self.setStyleSheet(f"background-color: {background_color}; color: {text_color};")
        #  change tables background color and header color to table color
        self.matrixTable.setStyleSheet(f"background-color: {table_color}; color: {text_color}; border: 1px solid {background_color}; gridline-color: {cells_border}; ")
        self.vectorTable.setStyleSheet(f"background-color: {table_color}; color: {text_color}; border: 1px solid {background_color}; gridline-color: {cells_border}; ")
        self.initialTable.setStyleSheet(f"background-color: {table_color}; color: {text_color}; border: 1px solid {background_color}; gridline-color: {cells_border}; ")
        self.solutionMatrix_1.setStyleSheet(f"background-color: {table_color}; color: {text_color}; border: 1px solid {background_color}; gridline-color: {cells_border}; ")
        self.solutionMatrix_2.setStyleSheet(f"background-color: {table_color}; color: {text_color}; border: 1px solid {background_color}; gridline-color: {cells_border}; ")

    
        # change input background color and border color to background color
        self.noRowsLine.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.precisionLine.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.iterationLine.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.errorLine.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.solveButton.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.operationComboBox.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.stepsButton.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.themeButton.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color}; border-radius: 25px;")

        # change labels color to label color
        self.matrixLabel.setStyleSheet(f"color: {label_color};")
        self.vectorLabel.setStyleSheet(f"color: {label_color};")
        self.solutionLabel_1.setStyleSheet(f"color: {label_color};")
        self.solutionLabel_2.setStyleSheet(f"color: {label_color};")
        self.parametersLabel.setStyleSheet(f"color: {label_color};")
        self.iteartionsLabel.setStyleSheet(f"color: {label_color};")
        self.errorLabel.setStyleSheet(f"color: {label_color};")
        self.initialLabel.setStyleSheet(f"color: {label_color};")
        self.noRowsLabel.setStyleSheet(f"color: {label_color};")
        self.precisionLabel.setStyleSheet(f"color: {label_color};")
        self.solutionLabel.setStyleSheet(f"color: {label_color};")
        self.solutionErrorLabel.setStyleSheet(f"color: {error_color};")



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
        
        if self.operation_index in [4,5,6]:
            self.vectorLabel.setVisible(False)
        else:
            self.vectorLabel.setVisible(True)
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
        start_time=time.time()
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
        
        if self.operation_index == 2:
            # gauss seidel
            no_iterations = int(self.iterationLine.text())
            tolerance = float(self.errorLine.text())
            initial_values = []
            for row in range(self.initialTable.rowCount()):
                initial_values.append([])
                for column in range(self.initialTable.columnCount()):
                    initial_values[row].append(self.initialTable.item(row,column).text())
            initial_values = np.array(initial_values).astype(np.float64)

            precision=int(self.precisionLine.text())
            solvable,steps,comments = gauss_seidel_method(matrix_data,vector_data,initial_values,no_iterations,tolerance,precision)
            print("solvable",solvable)
            if not solvable:
                self.solutionErrorLabel.setText("No Solution")
                return
            print(steps)
            print(comments)
            output=[]
            for step in steps:
                output.append({"X":step[:,0:1],"Relative Approximate Error":step[:,1:]})
            self.output=output
            self.comments =comments
            solution = steps[-1]
            print("solution",solution)
            self.solutionMatrix_1.setRowCount(len(solution))
            self.solutionMatrix_1.setColumnCount(1)
            for i in range(len(solution)):
                self.solutionMatrix_1.setItem(i,0,QTableWidgetItem(str(solution[i][0])))

        if self.operation_index == 3:
            # gauss jacobi
            no_iterations = int(self.iterationLine.text())
            tolerance = float(self.errorLine.text())
            initial_values = []
            for row in range(self.initialTable.rowCount()):
                initial_values.append([])
                for column in range(self.initialTable.columnCount()):
                    initial_values[row].append(self.initialTable.item(row,column).text())
            initial_values = np.array(initial_values).astype(np.float64)

            precision=int(self.precisionLine.text())
            solvable,steps,comments = gacobi_method(matrix_data,vector_data,initial_values,no_iterations,tolerance,precision)
            print("solvable",solvable)
            if not solvable:
                self.solutionErrorLabel.setText("No Solution")
                return
            print(steps)
            print(comments)
            output=[]
            for step in steps:
                output.append({"X":step[:,0:1],"Relative Approximate Error":step[:,1:]})
            self.output=output
            self.comments =comments
            solution = steps[-1]
            print("solution",solution)
            self.solutionMatrix_1.setRowCount(len(solution))
            self.solutionMatrix_1.setColumnCount(1)
            for i in range(len(solution)):
                self.solutionMatrix_1.setItem(i,0,QTableWidgetItem(str(solution[i][0])))

        if self.operation_index == 5:
            # crout LU
            output,steps = CroutLU(matrix_data)
            self.output= output
            self.comments =steps
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

        end_time=time.time()
        total_time =round(end_time-start_time,3)
        print("time",total_time)
        self.solutionErrorLabel.setText(f"Time: {total_time} seconds")
        
            
        
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
        
    def stepsButton_clicked(self):
        print("stepsButton_clicked")
        # self.steps_window = StepsWindow(output=[{"L":[[1,2],[3,4]],"U":[[5,6],[7,8]]},{"X":[[5,6],[7,8]]},{"X":[[5,6],[7,8]]}],comments=["hello","iam fine","tmam"])
        self.steps_window = StepsWindow(output=self.output,comments=self.comments,theme=self.color_theme)
        self.steps_window.show_steps()
        