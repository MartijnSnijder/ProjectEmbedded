import tkinter as Tk
import pprint


class instellingen(Tk.Toplevel):
    st_fields = {'Minimale uitrol (cm)': 5, 'Maximale uitrol (cm)': 200,
                 'Temperatuurwaarde (C)': 21,'Lichtwaarde (int)': 150,'Meet interval (sec)': 40}
    st_fields= sorted((st_fields.keys()))
    fields = st_fields
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("500x300")
        self.title("Instellingen")
        self.buttons()
        self.makeform()
        self.test()
    # ----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()

    # ----------------------------------------------------------------------
    def buttons(self):
        btn_save = Tk.Button(self, text='Opslaan', pady=2, command=self.get_entry_values)
        btn_save.grid(row=10, column=1,pady=2)
        btn_std = Tk.Button(self, text='Standaard instellingen', pady=2, command=())
        btn_std.grid(row=10, column=2,pady=5)
        btn_close = Tk.Button(self, text="Close", pady=2,command=self.onClose)
        btn_close.grid(row=10, column=3, pady=5)

    # -----------------------------------------------------------------------

    def test(self):
        print(self.st_fields)

    def huidige_waardes(self):
            for key in instellingen.st_fields:
                print(key, instellingen.st_fields[key])


    def makeform(self):
        #self.show_standard()

        Tk.Label(self, text="Huidig:").grid(row=0, column=3, sticky=Tk.W)
        Tk.Label(self, text=" ").grid(row=0, column=4, sticky=Tk.W)
        Tk.Label(self, text="Standaard: ").grid(row=0, column=5, sticky=Tk.W)

        #uitrol instellingen --
        Tk.Label(self, text="Uitrol instellingen:").grid(row=0, sticky=Tk.W,pady=6)

        Tk.Label(self, text="Minimale uitrol (cm)").grid(row=1, sticky=Tk.W)
        e1 = Tk.Entry(self)
        e1.grid(row=1, column=2)

        Tk.Label(self, text="Maximale uitrol (cm)").grid(row=2, sticky=Tk.W)
        e2 = Tk.Entry(self)
        e2.grid(row=2, column=2)

        #sensoren -> Lichtwaarde en temperatuurwaarde --
        Tk.Label(self, text="Sensor instellingen:").grid(row=3, sticky=Tk.W, pady=6)

        Tk.Label(self, text="Lichtwaarde (int)").grid(row=4, sticky=Tk.W)
        e3 = Tk.Entry(self)
        e3.grid(row=4, column=2)

        Tk.Label(self, text="Temperatuurwaarde (C)").grid(row=5, sticky=Tk.W)
        e4 = Tk.Entry(self)
        e4.grid(row=5, column=2)

        #meetinterval --
        Tk.Label(self, text="Automatisch meten:").grid(row=6, sticky=Tk.W, pady=6)

        Tk.Label(self, text="Meet interval (sec)").grid(row=7, sticky=Tk.W)
        e5 = Tk.Entry(self)
        e5.grid(row=7, column=2)



    def get_entry_values(self):
        pass

    def show_standard(self):
        x = 1
        for key in instellingen.st_fields:
            Tk.Label(self, text=instellingen.st_fields[key]).grid(row=x, column=5, sticky=Tk.W)
            x += 1


        """

        x=0
        row = Tk.Frame(self)
        lab = Tk.Label(row, width=20, anchor='w')
        ent = Tk.Enty(row)
        row.grid(row=x, column=1, columnspan=2)
        lab.grid(row=x, column=1, columnspan=2)
        ent.grid(row=x,column=1, columnspan=2)
        entries.append(, ent)

        pass
        #for field in instellingen.st_fields:
        x += 1
        row = Tk.Frame(self)
        lab = Tk.Label(row, width=20, text=field, anchor='w')
        ent = Tk.Entry(row)
        row.grid(row=x, column=1, columnspan=2)
        lab.grid(row=x, column=2, columnspan=2)
        ent.grid(row=x, column=3, columnspan=2)
        entries.append((field, ent))
        print(entries)

        return entries
        """


