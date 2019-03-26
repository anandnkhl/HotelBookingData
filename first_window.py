'''
Created on 02-Jun-2018

@author: Nikhil Anand
'''
import tkinter as tk
from tkinter import ttk, Canvas
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style


Large_Font= ("Verdana", 30)
style.use("ggplot")

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.iconbitmap(self, default= "icon.ico")
        tk.Tk.wm_title(self, "First App")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageThree):
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column = 0, sticky="nsew")
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)
   
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font= Large_Font)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Visit Page One", command=lambda: controller.show_frame(PageOne))
        button1.pack()
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font= Large_Font)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Visit Graph Page", command=lambda: controller.show_frame(PageThree))
        button1.pack()    
        
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font= Large_Font)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Back to Start Page", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
        f = Figure(figsize=(5,5), dpi = 100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,1,2,9,1,3,5,3])
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)
        
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
    
app = SeaofBTCapp()
app.mainloop()