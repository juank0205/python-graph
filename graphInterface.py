import tkinter
from tkinter import ttk
import functions as func

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot()
line, = ax.plot([], [])
ax.set_xlabel("time [s]")
ax.set_ylabel("f(t)")

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()

def plotFunction(event = {}):
    newFunction = func.Function(functionEntry.get())
    xValues, yValues = newFunction.evalFunction(np.arange(-10, 10, 1))
    line.set_data(xValues, yValues)
    canvas.draw()

# pack_toolbar=False will make it easier to use a layout manager later on.
toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
toolbar.update()

canvas.mpl_connect(
    "key_press_event", lambda event: print(f"you pressed {event.key}"))
canvas.mpl_connect("key_press_event", key_press_handler)

button_quit = tkinter.Button(master=root, text="Quit", command=root.destroy)
functionEntry = ttk.Entry(master=root)
plotButton = tkinter.Button(master=root, text="Plot", command=plotFunction)

plotButton.pack(side=tkinter.BOTTOM)
button_quit.pack(side=tkinter.BOTTOM)
functionEntry.pack(side=tkinter.BOTTOM, anchor='center') 
functionEntry.bind('<Return>', plotFunction)
toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

tkinter.mainloop()
