import tkinter as Tk
import instellingen

import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

########################################################################
class MyApp(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Scherm overzicht")
        self.frame = Tk.Frame(parent)

        #self.frame.grid()
        self.line_graph()

       # self.initUI()
       # self.current_values()

    # ----------------------------------------------------------------------
    def hide(self):
        self.root.withdraw()

    def buttons(self):
        button = Tk.Button(master=root, text='Quit', command=sys.exit)
        button.pack(side=Tk.LEFT)
        btn_ins = Tk.Button(master=root, text="Instellingen", command=self.openInstellingen, width=15)
        btn_ins.pack(side=Tk.LEFT)

        btn_din = Tk.Button(master=root, text="dingen")
        btn_din.pack(side=Tk.LEFT)

        btn_inr = Tk.Button(master=root, text="Volledig inrollen", command=(), width=15)
        btn_inr.pack(side=Tk.LEFT)

        btn_inr = Tk.Button(master=root, text="Volledig uitrollen", command=(), width=15)
        btn_inr.pack(side=Tk.LEFT)

    # ----------------------------------------------------------------------
    def openInstellingen(self):
        subFrame = instellingen.instellingen(self)
        return subFrame

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

    def current_values(self):
        lijst = instellingen.instellingen.changed_fields
        namen = instellingen.instellingen.namen
        Tk.Label(root, text = "Huidige ingestelde waardes:").grid(row=2, column = 2)
        y=3
        for x in range(len(lijst)):
            Tk.Label(root,text=namen[x], width = 25).grid(row=y, column = 1)
            Tk.Label(root, text=lijst[x], width = 15).grid(row=y, column=2)
            y+=1

    def initUI(self):
        #Slider widget voor scherm uitrol
        var = Tk.DoubleVar()
        scale = Tk.Scale(root, from_=0, to_=160, variable_=var, orient_=Tk.HORIZONTAL,
                      tickinterval_=20, length_=200, label="Zonnescherm handmatig in/uitrollen (cm)")
        scale.grid(row = 4, column= 8)

    def line_graph(self):
        # http://matplotlib.org/examples/user_interfaces/embedding_in_tk2.html

        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)

        a.plot(t, s)
        a.set_title('Tk embedding')
        a.set_xlabel('X axis label')
        a.set_ylabel('Y label')

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        self.buttons()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("600x600")
    app = MyApp(root)
    root.mainloop()