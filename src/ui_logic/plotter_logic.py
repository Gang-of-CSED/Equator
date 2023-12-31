import sys
import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from src.operations.Plotter import plot_function,click_points
from matplotlib import pyplot as plt


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, function,num_points=2, x_range=(-10, 10),parent=None, width=5, height=4, dpi=100):
        error,fig,self.axes=plot_function(function,x_range=x_range)
        super(MplCanvas, self).__init__(fig)
        points=click_points(plt,function,num_points)
     

