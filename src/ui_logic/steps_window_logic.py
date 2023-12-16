from src.ui.steps_window_ui import Ui_stepsDialog
from PySide6.QtWidgets import QDialog, QVBoxLayout, QScrollArea, QWidget, QGridLayout, QTableWidget, QTableWidgetItem,QHBoxLayout,QLabel
from PySide6.QtWidgets import QTextBrowser, QPushButton

class StepsWindow(QDialog,Ui_stepsDialog):
    
    def __init__(self,output,comments=[]) -> None:
        self.output = output
        self.comments = comments
        super().__init__()
        self.setupUi(self)
        self.clear_steps()
        for i in range(len(self.output)):
            step = self.output[i]
            comment = self.comments[i]
            step_page = self.get_step_page(i,step,comment)
            self.stackedWidget.addWidget(step_page)

    def show_steps(self):
        self.show()

        
    def get_step_page(self,index,step,comment):
        step_page=QWidget()
        for key_i in range(len(step.keys())):
            print(key_i,list(step.keys()))
            key=list(step.keys())[key_i]
            print(key)
            data=step[key]
            step_matrix_label=QLabel(step_page)
            step_matrix_label.setText(key)            
            step_matrix_label.setGeometry(0+key_i*(740/len(step.keys())),130,(740/len(step.keys()))-10,30)

            step_matrix= QTableWidget(step_page)
            step_matrix.setRowCount(len(data))
            step_matrix.setColumnCount(len(data[0]))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    step_matrix.setItem(i,j,QTableWidgetItem(str(data[i][j])))
            step_matrix.setGeometry(0+key_i*(740/len(step.keys())),170,(740/len(step.keys()))-10,300)
            # hide headers
            step_matrix.horizontalHeader().hide()
            step_matrix.verticalHeader().hide()
        
        step_comment =QTextBrowser(step_page)
        step_comment.setText(comment)
        step_comment.setGeometry(0,0,740,150)
        step_comment.setReadOnly(True)

        if index != len(self.output)-1:
            next_button = QPushButton(step_page)
            next_button.setText("Next")
            next_button.setGeometry(600,480,100,30)
            next_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1))
        
        if index>0:
            prev_button = QPushButton(step_page)
            prev_button.setText("Previous")
            prev_button.setGeometry(0,480,100,30)
            prev_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1))

        return step_page


    def clear_steps(self):
        for i in range(self.stackedWidget.count()):
            self.stackedWidget.removeWidget(self.stackedWidget.widget(0))
        self.stackedWidget.setCurrentIndex(0)