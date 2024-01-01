import sys
import matplotlib
import sympy as sp
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from src.operations.Plotter import plot_function,click_points
from matplotlib import pyplot as plt


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, function,parent=None, width=5, height=4, dpi=100):
        error,fig,self.axes=plot_function(function)
        super(MplCanvas, self).__init__(fig)
        self.points = []
        # self.connect_click_event(function)

    def connect_click_event(self, function, num_clicked_points=2):
        self.axes.set_title(f"Click {num_clicked_points} points on the function line")
        self.draw()
        self.cid = self.mpl_connect('button_press_event', lambda event: self.on_click(event, function, num_clicked_points))

    def on_click(self, event, function, num_clicked_points):
        
        if event.xdata is not None:
            x_clicked = event.xdata
            y_clicked = self.calculate_y(x_clicked, function)

            self.points.append((x_clicked, y_clicked))
            print(f"Clicked at (x, y) = ({x_clicked:.2f}, {y_clicked:.2f}) on the function line")

            self.axes.annotate(f'x={x_clicked:.4f}', (x_clicked, y_clicked), textcoords="offset points",
                               xytext=(0, 10), ha='center', fontsize=10, color='black')
            self.axes.scatter(x_clicked, y_clicked, color='black', marker='x')
            self.draw()

            if len(self.points) == num_clicked_points:
                self.axes.set_title(f'Plot of {function}')
                self.draw()
                self.disconnect_click_event()
                print(f"{num_clicked_points} points clicked. Returning array:", self.points)
                self.draw()
                

    def calculate_y(self, x, function):
        x_symbol = sp.symbols('x')
        expr = sp.sympify(function)
        func = sp.lambdify(x_symbol, expr, 'numpy')
        return func(x)

    def disconnect_click_event(self):
        self.mpl_disconnect(self.cid)

