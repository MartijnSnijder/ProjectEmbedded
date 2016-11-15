import tkinter as Tk
import pprint


class instellingen(Tk.Toplevel):
    st_fields = {'Minimale uitrol (cm)': 5, 'Maximale uitrol (cm)': 200,
                 'Temperatuurwaarde (C)': 21,'Lichtwaarde (int)': 150,'Meet interval (sec)': 40}
    fields = st_fields
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("500x200")
        self.title("Instellingen")
        self.buttons()
        self.makeform()

    # ----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()

    # ----------------------------------------------------------------------
    def buttons(self):
        btn_save = Tk.Button(self, text='Opslaan', command=self.get_entry_values)
        btn_save.grid(row=10, column=1)
        btn_std = Tk.Button(self, text='Standaard instellingen', command=())
        btn_std.grid(row=10, column=2)
        btn_close = Tk.Button(self, text="Close", command=self.onClose)
        btn_close.grid(row=10, column=3)

    # -----------------------------------------------------------------------

    def huidige_waardes(self):
            for key in instellingen.st_fields:
                print(key, instellingen.st_fields[key])


    def makeform(self):
        x = 1
        Tk.Label(self, text="Huidig:").grid(row=0, column=3, sticky=Tk.W)
        Tk.Label(self, text=" ").grid(row=0, column=4, sticky=Tk.W)
        Tk.Label(self, text="Standaard: ").grid(row=0, column=5, sticky=Tk.W)
        for key in instellingen.st_fields:
            Tk.Label(self, text=key).grid(row=x, sticky=Tk.W)
            e1 = Tk.Entry(self)
            e1.grid(row=x, column=2)
            Tk.Label(self, text=instellingen.st_fields[key]).grid(row=x, column=5, sticky=Tk.W)
            x += 1

    def get_entry_values(self):
        for key in instellingen.fields:

            if instellingen.fields.get(key) != 0:
                print("yolo")
        print(instellingen.fields)

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


