import tkinter as Tk
import instellingen

########################################################################
class MyApp(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Scherm overzicht")
        self.frame = Tk.Frame(parent)
        self.frame.grid()
        self.initUI()
        self.buttons()
        self.waardes()


    # ----------------------------------------------------------------------
    def hide(self):
        self.root.withdraw()

    def waardes(self):
        waardes = Tk.Label(root, text="Gekkigheid")
        waardes.grid(row=2, column=1)

    def buttons(self):
        btn_ins = Tk.Button(self.frame, text="Instellingen", command=self.openInstellingen)
        btn_ins.grid(row=1, column=3)

        btn_din = Tk.Button(self.frame, text="dingen")
        btn_din.grid(row=1, column=4)

        btn_inr = Tk.Button(self.frame, text="Volledig inrollen" , command=())
        btn_inr.grid(row=4, column= 4, columnspan= 3)

        btn_inr = Tk.Button(self.frame, text="Volledig uitrollen" , command=())
        btn_inr.grid(row=4, column=1, columnspan=3)

    # ----------------------------------------------------------------------
    def openInstellingen(self):
        subFrame = instellingen.instellingen(self)
        return subFrame

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

    def initUI(self):
        #Slider widget voor scherm uitrol
        var = Tk.DoubleVar()
        scale = Tk.Scale(root, from_=0, to_=160, variable_=var, orient_=Tk.HORIZONTAL,
                      tickinterval_=20, length_=300, label="Zonnescherm handmatig in/uitrollen (cm)")
        scale.grid(row=1, column=3, columnspan= 6)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("600x200")
    app = MyApp(root)
    root.mainloop()