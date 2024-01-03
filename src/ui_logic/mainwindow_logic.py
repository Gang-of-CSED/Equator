import sys
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QVBoxLayout, QWidget
from PySide6.QtCore import QRegularExpression, QRect
from PySide6.QtGui import QRegularExpressionValidator
import sympy as sp
from src.ui.mainwindow_ui import Ui_MainWindow as MainWindowUI
from PySide6.QtCore import SIGNAL
import numpy as np
from src.operations.gaussOperations import gauss_elimination,gauss_Jordan
from src.operations.CroutLU import CroutLU
from src.operations.DoolittleLU import DoolittleLU
from src.operations.CholeskyLU import Cholesky
from src.operations.Gauss_Seidel_Method import gauss_seidel_method
from src.operations.Gacobi_Method import gacobi_method
from src.operations.Plotter import plot_function
from PySide6.QtGui import QColor

from src.ui_logic.steps_window_logic import StepsWindow
from src.ui_logic.steps_window_root_logic import StepsWindowRoot
from src.ui_logic.plotter_logic import MplCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from src.operations.Plotter import is_valid_function
from src.operations.Bisection import bisection
from src.operations.FalsePosition import FalsePosition
from src.operations.Fixed_Point import fixed_point
from src.operations.Secant_Method import secant_method
from src.operations.NewtonRaphson import *
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
        self.themeButton_root.clicked.connect(self.themeButton_clicked)
        self.stepsButton.clicked.connect(self.stepsButton_clicked)
        self.output=[]
        self.comments=[]
        self.init_root_tab()
        # #1c284f
    def themeButton_clicked(self):
        self.themeButton.setText(self.color_theme)
        self.themeButton_root.setText(self.color_theme)
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
        self.stepsButton_root.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.plotButton.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.range1LineEdit.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.range2LineEdit.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.signLine_root.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.input1LineEdit.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.input2LineEdit.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.errorLine_root.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.iterationLine_root.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.equationLineEdit.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.equationLineEdit_2.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.rootLineEdit.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.noIterationsLineEdit.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.themeButton_root.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color}; border-radius: 25px;")
        self.solveButton_root.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        self.operationComboBox_root.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")

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
        self.range1Label.setStyleSheet(f"color: {label_color};")
        self.range2Label.setStyleSheet(f"color: {label_color};")
        self.input1Label.setStyleSheet(f"color: {label_color};")
        self.input2Label.setStyleSheet(f"color: {label_color};")
        self.errorLabel_root.setStyleSheet(f"color: {label_color};")
        self.iteartionsLabel_root.setStyleSheet(f"color: {label_color};")
        self.equationLabel.setStyleSheet(f"color: {label_color};")
        self.equationLabel_2.setStyleSheet(f"color: {label_color};")
        self.rootLabel.setStyleSheet(f"color: {label_color};")
        self.noIterationsLabel.setStyleSheet(f"color: {label_color};")
        self.solutionErrorLabel_root.setStyleSheet(f"color: {error_color};")
        self.signLabel_root.setStyleSheet(f"color: {label_color};")
        self.plotLabel.setStyleSheet(f"color: {label_color};")

        # change tabs color
        self.tabWidget.setStyleSheet(f"background-color: {background_color}; color: {text_color}; border: 1px solid {background_color};")



    def comboBox_changed(self, index):
        self.operation_index=index
        self.update_visiblity()
        self.update_labels()
        print(index)
    
    def update_visiblity(self):
        self.solutionMatrix_2.setVisible(False)
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
        try:
            start_time=time.time()
            self.solutionErrorLabel.setText("")
            precision= 4
            if self.precisionLine.text() != "":
                precision=int(self.precisionLine.text())
            no_iterations=10
            if self.iterationLine.text() != "":    
                no_iterations = int(self.iterationLine.text())
            tolerance =30
            if self.errorLine.text() != "":
                tolerance = float(self.errorLine.text())
            

            # get items from qt table to numpy array
            matrix_data = []
            for row in range(self.matrixTable.rowCount()):
                matrix_data.append([])
                for column in range(self.matrixTable.columnCount()):
                    matrix_data[row].append(self.matrixTable.item(row, column).text())
            
            matrix_data = np.array(matrix_data).astype(object)
        
            print("columns:",self.initialTable.columnCount(),"rows:",self.initialTable.rowCount())
            initial_values = []
            for row in range(self.initialTable.rowCount()):
                initial_values.append([])
                for column in range(self.initialTable.columnCount()):
                    print(row,column,self.initialTable.item(row,column))
                    if self.initialTable.item(row,column).text() == "":
                        initial_values[row].append(1)
                    else:
                        initial_values[row].append(self.initialTable.item(row,column).text())
            initial_values = np.array(initial_values).astype(np.float64)
            print("initiallll",initial_values)


            vector_data = []
            for row in range(self.vectorTable.rowCount()):
                vector_data.append([])
                for column in range(self.vectorTable.columnCount()):
                    print(row,column,self.vectorTable.itemAt(row,column))
                    vector_data[row].append(self.vectorTable.item(row,column).text())
            vector_data = np.array(vector_data).astype(object)

            if self.operation_index == 0:
                # gauss elimination
                solvable,solution,steps = gauss_elimination(matrix_data.astype(np.float64),vector_data.astype(np.float64),significantD=precision)
                print("solvable",solvable)
                print("solution",solution)
                print("steps",steps)
                if not solvable:
                    self.solutionErrorLabel.setText("No Solution")
                    return
                print(solution)
                print(steps)
                self.solutionMatrix_1.setRowCount(len(solution))
                self.solutionMatrix_1.setColumnCount(1)
                for i in range(len(solution)):
                    self.solutionMatrix_1.setItem(i,0,QTableWidgetItem(str(solution[i])))
                
            
                self.output = [({"Aug. Matrix":step["output"]} if len(np.array(step["output"]).shape) != 1 else {"X": np.array(step["output"]).reshape(-1,1)}) for step in steps]

                self.comments = [step["message"] for step in steps]
            
            if self.operation_index == 1:
                # gauss elimination

                solvable,solution,steps = gauss_Jordan(matrix_data.astype(np.float64),vector_data.astype(np.float64),significantD=precision)
                if not solvable:
                    self.solutionErrorLabel.setText("No Solution")
                    return
                
                self.solutionMatrix_1.setRowCount(len(solution))
                self.solutionMatrix_1.setColumnCount(1)
                for i in range(len(solution)):
                    self.solutionMatrix_1.setItem(i,0,QTableWidgetItem(str(solution[i])))
                # convert solution to column vector
                self.output = [({"Aug. Matrix":step["output"]} if len(np.array(step["output"]).shape) != 1 else {"X": np.array(step["output"]).reshape(-1,1)}) for step in steps]

                self.comments = [step["message"] for step in steps]
            
            if self.operation_index == 2:
                # gauss seidel

                solvable,steps,comments = gauss_seidel_method(matrix_data.astype(np.float64),vector_data.astype(np.float64),initial_values,no_iterations,tolerance,precision)
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
                
                self.solutionMatrix_1.setRowCount(len(solution))
                self.solutionMatrix_1.setColumnCount(1)
                for i in range(len(solution)):
                    self.solutionMatrix_1.setItem(i,0,QTableWidgetItem(str(solution[i][0])))

            if self.operation_index == 3:
                # gauss jacobi
                solvable,steps,comments = gacobi_method(matrix_data.astype(np.float64),vector_data.astype(np.float64),initial_values,no_iterations,tolerance,precision)
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

            if self.operation_index == 4:
                # Doolittle LU
                vector_data_flat = vector_data.flatten()
                print("flat:",vector_data_flat)
                output,steps,answer = DoolittleLU(matrix_data,vector_data_flat,precision)
                print("output: ",output)
                print("steps: ",steps)
                print("answer: ",answer)
                print(len(output),len(steps),answer)
                X =answer['x']

                self.solutionMatrix_1.setRowCount(len(X))
                self.solutionMatrix_1.setColumnCount(len(X[0]))
                for i in range(len(X)):
                    for j in range(len(X[0])):
                        self.solutionMatrix_1.setItem(i,j,QTableWidgetItem(str(X[i,j])))
                output.append(answer)
                self.output= output
                self.comments =steps

            if self.operation_index == 5:
                # crout LU
                vector_data_flat = vector_data.flatten()
                print("flat:",vector_data_flat)
                output,steps,answer = CroutLU(matrix_data,vector_data_flat,precision)
                print("output: ",output)
                print("steps: ",steps)
                print("answer: ",answer)
                print(len(output),len(steps),answer)
                X =answer['x']

                self.solutionMatrix_1.setRowCount(len(X))
                self.solutionMatrix_1.setColumnCount(len(X[0]))
                for i in range(len(X)):
                    for j in range(len(X[0])):
                        self.solutionMatrix_1.setItem(i,j,QTableWidgetItem(str(X[i,j])))
                output.append(answer)
                self.output= output
                self.comments =steps
            
            if self.operation_index == 6:
                # Cholesky LU
                vector_data_flat = vector_data.flatten()
                # convert to float
                vector_data_flat = vector_data_flat.astype(np.float64)
                # convert matrix to float
                matrix_data = matrix_data.astype(np.float64)
                print("flat:",vector_data_flat)
                output,steps,answer = Cholesky(matrix_data,vector_data_flat,precision)
                if len(output) == 0:
                    if len(steps) == 0:
                        self.solutionErrorLabel.setText("Non Symmetric Positive Definite Matrices")
                    else:
                        self.solutionErrorLabel.setText(steps[0])
                    return


                print("output: ",output)
                print("steps: ",steps)
                print("answer: ",answer)

                print(len(output),len(steps),answer)
                
                X =answer['x']

                self.solutionMatrix_1.setRowCount(len(X))
                self.solutionMatrix_1.setColumnCount(len(X[0]))
                
                for i in range(len(X)):
                    for j in range(len(X[0])):
                        self.solutionMatrix_1.setItem(i,j,QTableWidgetItem(str(X[i,j])))
                        
                output.append(answer)
                self.output= output
                self.comments =steps

            end_time=time.time()
            total_time =round(end_time-start_time,3)
            print("time",total_time)
            self.solutionErrorLabel.setText(f"Time: {total_time} seconds")
        
        except:
            self.solutionErrorLabel.setText("Sorry can't solve using this method!")
            # clear solution matrix
            self.solutionMatrix_1.setRowCount(1)
            self.solutionMatrix_1.setColumnCount(1)
            self.solutionMatrix_1.setItem(0,0,QTableWidgetItem("0"))
            
            
        
    def update_labels(self):
        # update labels
        self.solutionLabel_1.setText("X")
        self.matrixLabel.setText("Coefficient Matrix")
        self.vectorLabel.setText("Vector")

        
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
        # validate input
        print(x,y,self.matrixTable.item(x,y).text())
        number_regex = QRegularExpression("^[-+]?[0-9]*\.?[0-9]+$")
        if not number_regex.match(self.matrixTable.item(x,y).text()).hasMatch():
            
            # force it to be a float number by remove any chracter not digit
            filterd_text=self.matrixTable.item(x,y).text()
            for i in range(len(filterd_text)-1,-1,-1):
                if i >= len(filterd_text):
                    continue
                print(filterd_text,i)
                if filterd_text[i] not in ['0','1','2','3','4','5','6','7','8','9','.','-','+','*','/','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']:
                    print("filtering",i)
                    filterd_text=filterd_text.replace(filterd_text[i],'')
            
            print(filterd_text)
            
            self.matrixTable.item(x,y).setText(filterd_text)
    
    def noRowsLine_changed(self):
        # update matrix table
        no_rows=int(self.noRowsLine.text())
        self.matrixTable.setRowCount(no_rows)
        self.matrixTable.setColumnCount(no_rows)
        for i in range(no_rows):
            for j in range(no_rows):
                self.matrixTable.setItem(i,j,QTableWidgetItem("0"))
        self.vectorTable.setRowCount(no_rows)
        for i in range(no_rows):
            self.vectorTable.setItem(i,0,QTableWidgetItem("0"))

        self.initialTable.setRowCount(no_rows)
        for i in range(no_rows):
            self.initialTable.setItem(i,0,QTableWidgetItem("0"))
        self.solutionMatrix_1.setRowCount(no_rows)
        self.solutionMatrix_1.setColumnCount(no_rows)
        self.solutionMatrix_2.setRowCount(no_rows)
        self.solutionMatrix_2.setColumnCount(no_rows)
    
        
    def stepsButton_clicked(self):
        print("stepsButton_clicked")
        # self.steps_window = StepsWindow(output=[{"L":[[1,2],[3,4]],"U":[[5,6],[7,8]]},{"X":[[5,6],[7,8]]},{"X":[[5,6],[7,8]]}],comments=["hello","iam fine","tmam"])
        self.steps_window = StepsWindow(output=self.output,comments=self.comments,theme=self.color_theme)
        self.steps_window.show_steps()

###########################  Root Tab ##############################
    
    def init_root_tab(self):
        self.operation_index_root=0
        self.update_visiblity_root()
        self.update_labels_root()
        self.operationComboBox_root.connect(self.operationComboBox_root, SIGNAL("currentIndexChanged(int)"), self.comboBox_changed_root)
        self.solveButton_root.connect(self.solveButton_root, SIGNAL("clicked()"), self.solveButton_clicked_root)
        self.add_validatitors_root()
        self.stepsButton_root.connect(self.stepsButton_root, SIGNAL("clicked()"), self.stepsButton_clicked_root)
        self.plotButton.connect(self.plotButton, SIGNAL("clicked()"), self.plotButton_clicked_root)
        self.valid_equation=False
        self.valid_equation_2=False
    def comboBox_changed_root(self, index):
        self.operation_index_root=index
        self.update_visiblity_root()
        self.update_labels_root()
        print(index)
    
    def update_visiblity_root(self):
        # TODO: 
        if self.operation_index_root in [0,1,4,6]:
            self.input2Label.setVisible(True)
            self.input2LineEdit.setVisible(True)
        else:
            self.input2Label.setVisible(False)
            self.input2LineEdit.setVisible(False)
        if self.operation_index_root == 2:
            self.equationLabel_2.setVisible(True)
            self.equationLineEdit_2.setVisible(True)
        else:
            self.equationLabel_2.setVisible(False)
            self.equationLineEdit_2.setVisible(False)
    
    def update_labels_root(self):
        self.equationLabel.setText("f(x)")
        if self.operation_index_root == 6:
            self.input1Label.setText("X0")
            self.input2Label.setText("X1")
        elif self.operation_index_root in [0,1]:
            self.input1Label.setText("a")
            self.input2Label.setText("b")
        elif self.operation_index_root in [2,3,4,5]:
            self.input1Label.setText("X0")
            self.input2Label.setText("m")
    
    def add_validatitors_root(self):

        number_regex = QRegularExpression("^[-+]?[0-9]*\.?[0-9]+$")
        input_validator = QRegularExpressionValidator(number_regex,self.input1LineEdit)
        self.input1LineEdit.setValidator(input_validator)
        self.input2LineEdit.setValidator(input_validator)
        self.range1LineEdit.setValidator(input_validator)
        self.range2LineEdit.setValidator(input_validator)
        self.errorLine_root.setValidator(input_validator)
        integer_regex = QRegularExpression("^[-+]?[0-9]*")
        integer_validator = QRegularExpressionValidator(integer_regex,self.iterationLine_root)
        self.iterationLine_root.setValidator(integer_validator)
        self.signLine_root.setValidator(integer_validator)

        # validate equation using sympy
        self.equationLineEdit.textChanged.connect(self.equationLineEdit_changed)
        self.equationLineEdit_2.textChanged.connect(self.equationLineEdit_changed_2)
    
    def equationLineEdit_changed(self):
        equation = self.equationLineEdit.text()
        if is_valid_function(equation):
            self.update_color_theme()
            self.valid_equation=True
        else:
            self.equationLineEdit.setStyleSheet("QLineEdit { color : red; }")
            self.valid_equation=False
    
    def equationLineEdit_changed_2(self):
        equation = self.equationLineEdit_2.text()
        if is_valid_function(equation):
            self.update_color_theme()
            self.valid_equation_2=True
        else:
            self.equationLineEdit_2.setStyleSheet("QLineEdit { color : red; }")
            self.valid_equation_2=False



    def solveButton_clicked_root(self):
        try:
            start_time=time.time()
            self.solutionErrorLabel_root.setText("")
            add_message=""
            # add default values
            precision=0.00001
            signficant_digits=4
            max_iterations=50

            # get items from lineEdit
            equation = self.equationLineEdit.text()
            a = float(self.input1LineEdit.text())
            b = float(self.input2LineEdit.text())

            if self.errorLine_root.text() != "":
                precision = float(self.errorLine_root.text())
            
            if self.signLine_root.text() != "":
                signficant_digits = int(self.signLine_root.text())
            
            if self.iterationLine_root.text() != "":
                max_iterations = int(self.iterationLine_root.text())

            if self.valid_equation == False or (self.valid_equation_2 == False and self.operation_index_root == 2):
                self.solutionErrorLabel_root.setText("Invalid Equation")
                return
            # solve and update steps
            if self.operation_index_root == 0:
                # bisection
                error,steps,roots = bisection(equation,a,b,signficant_digits,precision,max_iterations)
                print("error",error,"steps",steps,"roots",roots)
                if error != None:
                    self.solutionErrorLabel_root.setText(error)
                    return
                self.solutionErrorLabel_root.setText("")
                self.rootLineEdit.setText(str(roots[-1]))
                self.noIterationsLineEdit.setText(str(len(steps)))
                self.output = roots
                self.comments = steps
            
            if self.operation_index_root == 1:
                # false position
                error,steps,roots = FalsePosition(equation,a,b,signficant_digits,precision,max_iterations)
                print("error",error,"steps",steps,"roots",roots)
                if error != None:
                    self.solutionErrorLabel_root.setText(error)
                    return
                self.solutionErrorLabel_root.setText("")
                self.rootLineEdit.setText(str(roots[-1]))
                self.noIterationsLineEdit.setText(str(len(steps)))
                self.output = roots
                self.comments = steps

            if self.operation_index_root == 2:
                # fixed point
                equation_2 = self.equationLineEdit_2.text()

                flag,error,steps,roots = fixed_point(equation_2,a,precision,max_iterations,signficant_digits)
                print("error",error,"steps",steps,"roots",roots)
                if not flag:
                    self.solutionErrorLabel_root.setText("Sorry can't solve it using this method")
                    return
                add_message="("+error+")"
                self.solutionErrorLabel_root.setText("")
                self.rootLineEdit.setText(str(roots[-1]))
                self.noIterationsLineEdit.setText(str(len(steps)))
                self.output = roots
                self.comments = steps
            
            if self.operation_index_root == 3:
                # newton raphson
                error,roots,steps = ModificationOne(equation,a,1,signficant_digits,precision,max_iterations)
                print("error",error,"steps",steps,"roots",roots)
                print(len(roots),len(steps))

                if error != None:
                    self.solutionErrorLabel_root.setText(error)
                    return
                
                self.solutionErrorLabel_root.setText("")
                self.rootLineEdit.setText(str(roots[-1]))
                self.noIterationsLineEdit.setText(str(len(steps)))
                self.output = roots
                self.comments = steps
            
            if self.operation_index_root == 4:
                # newton raphson
                error,roots,steps = ModificationOne(equation,a,b,signficant_digits,precision,max_iterations)
                print("error",error,"steps",steps,"roots",roots)
                print(len(roots),len(steps))

                if error != None:
                    self.solutionErrorLabel_root.setText(error)
                    return
                
                self.solutionErrorLabel_root.setText("")
                self.rootLineEdit.setText(str(roots[-1]))
                self.noIterationsLineEdit.setText(str(len(steps)))
                self.output = roots
                self.comments = steps
            
            if self.operation_index_root == 5:
                # newton raphson
                error,roots,steps = ModificationTwo(equation,a,signficant_digits,precision,max_iterations)
                print("error",error,"steps",steps,"roots",roots)
                print(len(roots),len(steps))
                if error != None:
                    self.solutionErrorLabel_root.setText(error)
                    return
                
                self.solutionErrorLabel_root.setText("")
                self.rootLineEdit.setText(str(roots[-1]))
                self.noIterationsLineEdit.setText(str(len(steps)))
                self.output = roots
                self.comments = steps

            
            if self.operation_index_root ==6:
                # secant method
                flag,error,steps,roots = secant_method(equation,a,b,precision,max_iterations,signficant_digits)
                print("error",error,"steps",steps,"roots",roots)
                if not flag:
                    self.solutionErrorLabel_root.setText("Sorry can't solve it using this method")
                    return
                add_message="("+error+")"
                self.solutionErrorLabel_root.setText("")
                self.rootLineEdit.setText(str(roots[-1]))
                self.noIterationsLineEdit.setText(str(len(steps)))
                self.output = roots
                self.comments = steps
            
            end_time=time.time()
            total_time =round(end_time-start_time,3)
            print("time",total_time)
            self.solutionErrorLabel_root.setText(f"Time: {total_time} seconds"+add_message)


        except Exception as e:
            print("Errrroorrr",e)
            # add error message
            self.solutionErrorLabel_root.setText("Sorry can't solve using this method!")
            # raise e


    def stepsButton_clicked_root(self):
        steps_window = StepsWindowRoot(output=self.output,comments=self.comments,theme=self.color_theme)
        steps_window.show_steps()

    def plotButton_clicked_root(self):
        if self.valid_equation == False:
            return
        # clear layout first
        if self.plotWidget.layout():
            for i in reversed(range(self.plotWidget.layout().count())): 
                self.plotWidget.layout().itemAt(i).widget().setParent(None)
        else:
            self.plotWidget.setLayout(QVBoxLayout())
        # get function from line edit
        function_text = self.equationLineEdit.text()
        if self.operation_index_root==2:
            function_text+=" - x"
        
        x_range=(-10,10)
        if self.range1LineEdit.text() != "" and self.range2LineEdit.text() != "":
            x_range=(int(self.range1LineEdit.text()),int(self.range2LineEdit.text()))
        sc= MplCanvas(function_text,x_range=x_range)
        layout = self.plotWidget.layout()
        toolbar = NavigationToolbar(sc, self)
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        print("layout",layout)
        # for input on graph
        num_clicked=1
        if self.operation_index_root in [0,1,6]:
            num_clicked=2
        sc.connect_click_event(function_text,num_clicked_points=num_clicked)
        # points= MplCanvas.get_points(sc, function_text, 2)
        # print("points",points)        
