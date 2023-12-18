from src.ui.steps_window_ui import Ui_stepsDialog
from PySide6.QtWidgets import QDialog, QVBoxLayout, QScrollArea, QWidget, QGridLayout, QTableWidget, QTableWidgetItem,QHBoxLayout,QLabel
from PySide6.QtWidgets import QTextBrowser, QPushButton

class StepsWindow(QDialog,Ui_stepsDialog):
    
    def __init__(self,output,comments=[],theme="Light") -> None:
        self.output = output
        self.comments = comments
        self.theme = theme
        super().__init__()
        self.setupUi(self)
        self.clear_steps()
        # add steps
        for i in range(len(self.output)):
            step = self.output[i]
            comment = self.comments[i]
            step_page = self.get_step_page(i,step,comment)
            self.stackedWidget.addWidget(step_page)

    def show_steps(self):
        self.show()

        
    def get_step_page(self,index,step,comment):
        # update theme
        background_color = "#FFFFFF"
        text_color = "#000000"
        table_color = "#f5f6f8"
        input_color = "#f5f6f8"
        label_color = "#69B6E3"
        error_color = "#b13600"
        cells_border="#e2e2f1"
        if self.theme == "Dark":
            background_color = "#14171d"
            text_color = "#FFFFFF"
            cells_border="#FFFFFF"
            table_color = "#1b1e25"
            input_color = "#21252c"
            label_color = "rgb( 84, 105, 212 )"
            error_color = "#f27400"
        # create page
        self.setStyleSheet(f"background-color:{background_color};color:{text_color};")
        step_page=QWidget()
        for key_i in range(len(step.keys())):
            print(key_i,list(step.keys()))
            key=list(step.keys())[key_i]
            print(key)
            data=step[key]
            step_matrix_label=QLabel(step_page)
            step_matrix_label.setText(key)            
            step_matrix_label.setGeometry(0+key_i*(740/len(step.keys())),140,(740/len(step.keys()))-10,30)
            step_matrix_label.setStyleSheet(f"color: {label_color};")
            # bold label
            font = step_matrix_label.font()
            font.setBold(True)
            step_matrix_label.setFont(font)
            
            print("textttttttttt:",step_matrix_label.text())
            step_matrix= QTableWidget(step_page)
            step_matrix.setRowCount(len(data))
            step_matrix.setColumnCount(len(data[0]))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    step_matrix.setItem(i,j,QTableWidgetItem(str(data[i][j])))
            step_matrix.setGeometry(0+key_i*(740/len(step.keys())),170,(740/len(step.keys()))-10,300)
            step_matrix.setStyleSheet(f"background-color: {table_color}; color: {text_color}; border: 1px solid {background_color}; gridline-color: {cells_border}; ")
            # hide headers
            step_matrix.horizontalHeader().hide()
            step_matrix.verticalHeader().hide()
        # add comment
        step_comment =QTextBrowser(step_page)
        step_comment.setText(comment)
        step_comment.setGeometry(0,0,740,150)
        step_comment.setReadOnly(True)
        step_comment.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color};")
        
        # add buttons
        if index != len(self.output)-1:
            next_button = QPushButton(step_page)
            next_button.setText("Next")
            next_button.setGeometry(600,480,100,30)
            next_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1))
            next_button.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color}; border-radius: 25px;")

        if index>0:
            prev_button = QPushButton(step_page)
            prev_button.setText("Previous")
            prev_button.setGeometry(0,480,100,30)
            prev_button.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1))
            prev_button.setStyleSheet(f"background-color: {input_color}; color: {text_color}; border: 1px solid {background_color}; border-radius: 25px;")

        return step_page


    def clear_steps(self):
        for i in range(self.stackedWidget.count()):
            self.stackedWidget.removeWidget(self.stackedWidget.widget(0))
        self.stackedWidget.setCurrentIndex(0)