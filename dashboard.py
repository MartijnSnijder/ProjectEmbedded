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
        #self.frame.grid()
        self.line_graph()
        self.initUI()
        self.current_values()



    def hide(self):
        self.root.withdraw()

    def buttons(self):
        btn_ins = Tk.Button(master=root, text="Instellingen", command=self.openInstellingen, width=15)
        btn_ins.pack(side=Tk.LEFT)

        btn_inr = Tk.Button(master=root, text="Volledig inrollen", command=(), width=15)
        btn_inr.pack(side=Tk.LEFT)

        btn_inr = Tk.Button(master=root, text="Volledig uitrollen", command=(), width=15)
        btn_inr.pack(side=Tk.LEFT)

        button_close = Tk.Button(master=root, text='Close', command=sys.exit)
        button_close.pack(side=Tk.LEFT)

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
        Tk.Label(root, text = "Huidige ingestelde waardes:").pack(anchor= Tk.SW)
        y=3
        for x in range(len(lijst)):
            Tk.Label(root,text=namen[x], width = 25).pack(anchor= Tk.S)
            Tk.Label(root, text=lijst[x], width = 15).pack(anchor=Tk.S)
            y+=1

    def initUI(self):
        #Slider widget voor scherm uitrol
        var = Tk.DoubleVar()
        scale = Tk.Scale(root, from_=0, to_=160, variable_=var, orient_=Tk.HORIZONTAL,
                      tickinterval_=20, length_=200, label="Zonnescherm handmatig in/uitrollen (cm)")
        scale.pack(side=Tk.RIGHT)

    def line_graph(self):

        # http://matplotlib.org/examples/user_interfaces/embedding_in_tk2.html

        f = Figure(figsize=(3, 3), dpi=100)
        a = f.add_subplot(111)
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)

        a.plot(t, s)
        a.set_title('Lichtwaardes')
        a.set_xlabel('Ja')
        a.set_ylabel('Zo')

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=self.root)
        canvas.show()
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        self.buttons()

        self.edoe()



    def edoe(self):
        data = [20, 15, 10, 7, 5, 4, 3, 2, 1, 1, 0]
        c_width = 400
        c_height = 350
        c = Tk.Canvas(root, width=c_width, height=c_height, bg='white')
        c.pack(side=Tk.TOP)

        # the variables below size the bar graph
        # experiment with them to fit your needs
        # highest y = max_data_value * y_stretch
        y_stretch = 15
        # gap between lower canvas edge and x axis
        y_gap = 20
        # stretch enough to get all data items in
        x_stretch = 10
        x_width = 20
        # gap between left canvas edge and y axis
        x_gap = 20

        for x, y in enumerate(data):
            # calculate reactangle coordinates (integers) for each bar
            x0 = x * x_stretch + x * x_width + x_gap
            y0 = c_height - (y * y_stretch + y_gap)
            x1 = x * x_stretch + x * x_width + x_width + x_gap
            y1 = c_height - y_gap
            # draw the bar
            c.create_rectangle(x0, y0, x1, y1, fill="red")
            # put the y value above each bar
            c.create_text(x0 + 2, y0, anchor=Tk.SW, text=str(y))


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("1000x800")
    app = MyApp(root)
    root.mainloop()