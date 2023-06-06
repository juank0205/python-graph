from views.views import View
import customtkinter as ctk
from classes.functions import Function, differentialEquation
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
import numpy as np


class GraphicView(View):
    def __init__(self, parent):
        super().__init__(parent )
        self.place(relwidth=1, relheight=1)
        self.x_min = -10
        self.x_max = 10
        self.y_min = -10
        self.y_max = 10
        self.__function = Function("")
        self.__string = ctk.StringVar(parent, value='')

        #Content to be defined
        self.graph_frame = ctk.CTkFrame(master=self)
        self.function_container = ctk.CTkFrame(master = self, width=300, height=50)
        self.function_input = ctk.CTkEntry(master = self.function_container, width=220, height=30)
        self.function_input.place(y=10, x=10)
        self.function_button = ctk.CTkButton(master = self.function_container, width=60, height=30)
        self.function_button.place(y=10, x=10)

        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(20, 5)
        self.fig.patch.set_facecolor('#ffffff')

        self.set_plot_style()

        self.canvas = FigureCanvasTkAgg(self.fig,master=self.graph_frame)
        self.canvas.draw()

        toolbar = NavigationToolbar2Tk(self.canvas, self.graph_frame)
        toolbar.update()

        self.canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
        self.canvas.mpl_connect("key_press_event", key_press_handler)

        self.graph_frame.pack()
        self.canvas.get_tk_widget().pack()
        toolbar.pack()

        self.function_entry = ctk.CTkEntry(master=self, textvariable=self.__string)
        self.function_entry.pack(pady=10)

        ctk.CTkButton(master=self, text='Graph', command=self.change_graph).pack(pady=10)

    def set_plot_style(self):

        #set self.axes limits and aspect ratio
        self.ax.set(xlim=(self.x_min-1, self.x_max+1), ylim=(self.y_min-1, self.y_max+1), aspect='equal')

        #set self.axes position and visibility to look like a cartesian plane
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')

        #set self.axes ticks style
        self.ax.set_xlabel('$t$', size=14, x=1.02, labelpad=-24)
        self.ax.set_ylabel('$y$', size=14, y=1, labelpad=-30, rotation=0)

        #set self.axes ticks
        self.ax.xaxis.set_major_locator(ticker.MaxNLocator(11))
        self.ax.yaxis.set_major_locator(ticker.MaxNLocator(11))
        yticks = self.ax.get_yticks()
        self.ax.set_yticks([tick for tick in yticks if tick != 0])
        self.ax.tick_params(axis='x', labelrotation=-45)

        #Create a grid (decoration)
        self.ax.grid(which='both', color='#a5a5a5', linestyle='-', linewidth=1, alpha=0.5)
        

    def change_graph(self):
        self.__function.set_string(self.__string.get())
        x_data, y_data = self.__function.evalFunction(np.arange(-10, 10, 0.1))
        self.ax.cla()
        self.set_plot_style()
        self.ax.plot(x_data, y_data)
        self.canvas.draw()
        

class EulerView(GraphicView):
    def __init__(self, parent):
        View.__init__(self, parent)
        self.place(relwidth=1, relheight=1)
        self.x_min = -10
        self.x_max = 10
        self.y_min = -10
        self.y_max = 10
        self.initialPoint = (0, 0)
        self.__function = differentialEquation("", self.initialPoint)
        self.__string = ctk.StringVar(parent, value='')

        #Content to be defined
        self.graph_frame = ctk.CTkFrame(master=self)
        self.function_container = ctk.CTkFrame(master = self, width=300, height=50)
        self.function_input = ctk.CTkEntry(master = self.function_container, width=220, height=30)
        self.function_input.place(y=10, x=10)
        self.function_button = ctk.CTkButton(master = self.function_container, width=60, height=30)
        self.function_button.place(y=10, x=10)

        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(20, 5)
        self.fig.patch.set_facecolor('#ffffff')

        self.set_plot_style()

        self.canvas = FigureCanvasTkAgg(self.fig,master=self.graph_frame)
        self.canvas.draw()

        toolbar = NavigationToolbar2Tk(self.canvas, self.graph_frame)
        toolbar.update()

        self.canvas.mpl_connect(
            "key_press_event", lambda event: print(f"you pressed {event.key}"))
        self.canvas.mpl_connect("key_press_event", key_press_handler)

        self.graph_frame.pack()
        self.canvas.get_tk_widget().pack()
        toolbar.pack()

        self.function_entry = ctk.CTkEntry(master=self, textvariable=self.__string)
        self.function_entry.pack(pady=10)

        ctk.CTkButton(master=self, text='Graph', command=self.change_graph).pack(pady=10)

    def change_graph(self):
        print(self.__string.get())
        self.__function.set_string(self.__string.get())
        self.ax.cla()
        self.set_plot_style()
        self.__function.eulerMethod(self.ax.plot)
        self.canvas.draw()

