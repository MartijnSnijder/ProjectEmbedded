import tkinter as Tk
import instellingen

########################################################################


########################################################################
class MyApp(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        self.initUI()
        self.buttonInstellingen()

    # ----------------------------------------------------------------------
    def hide(self):
        self.root.withdraw()

    def buttonInstellingen(self):
        btn = Tk.Button(self.frame, text="Instellingen", command=self.openInstellingen)
        btn.pack()

    # ----------------------------------------------------------------------
    def openInstellingen(self):
        """"""
        subFrame = instellingen.instellingen(self)


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
        scale.pack()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()