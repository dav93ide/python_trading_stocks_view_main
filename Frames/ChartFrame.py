import wx
import numpy as np
import wx.lib.mixins.inspection as WIT
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
from matplotlib.figure import Figure

class ChartFrame(wx.Frame):
   
    __mFigure = None
    __mCanvas = None
    __mAxes = None
    __mToolbar = None
   
    def __init__(self, x, y):
        super().__init__(None, -1, 'CanvasFrame', size=(550, 350))

        self.__mFigure = Figure()
        self.__mAxes = self.figure.add_subplot()

        self.__mAxes.plot(x, y)

        self.__mAxes.fill_between(x, min(y), y, alpha=0.5)
        self.__mCanvas = FigureCanvas(self, -1, self.__mFigure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.__mCanvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

        self.add_toolbar()

#region - Public Methods
    def add_toolbar(self):
        self.__mToolbar = NavigationToolbar(self.__mCanvas)
        self.__mToolbar.Realize()
        self.sizer.Add(self.__mToolbar, 0, wx.LEFT | wx.EXPAND)
        self.__mToolbar.update()

    def update_values_with_color(self, x, y, color):
        self.__mAxes.clear()
        self.__mAxes.plot(x, y, color)
        self.__mAxes.fill_between(x, min(y), y, alpha=0.5)
        self.__mCanvas.draw()
        self.__mCanvas.flush_events()

    def update_values(self, x, y):
        self.__mAxes.clear()
        self.__mAxes.plot(x, y)
        self.__mAxes.fill_between(x, min(y), y, alpha=0.5)
        self.__mCanvas.draw()
        self.__mCanvas.flush_events()
#endregion