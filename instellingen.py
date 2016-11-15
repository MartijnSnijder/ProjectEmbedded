import tkinter as Tk
import graphs

class instellingen(Tk.Toplevel):
    fields = 'Minimale uitrol', 'Maximale uitrol', 'Temperatuurwaarde', 'Lichtwaarde', 'Meet interval'
    entries = [5, 200, 21, 50, 40]
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("400x300")
        self.title("Instellingen")

        btn_close = Tk.Button(self, text="Close", command=self.onClose)
        btn_close.pack()
        b1 = Tk.Button(self, text='Opslaan', command=())
        b1.pack()
        b2 = Tk.Button(self, text='Standaard instellingen', command=())
        b2.pack()

    # ----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()

    # ----------------------------------------------------------------------
    def buttons(self):
       pass

    def standaardwaarden(self):
        for e in range(len(instellingen.fields)):
            print(instellingen.fields[e], instellingen.entries[e])

    def fetch(entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))



    def makeform(self, fields):
        entries = []
        for field in fields:
            row = Tk.Frame(self)
            lab = Tk.Label(row, width=20, text=field, anchor='w')
            ent = Tk.Entry(row)
            row.pack(side=Tk.TOP, fill=Tk.X, padx=5, pady=5)
            lab.pack(side=Tk.LEFT)
            ent.pack(side=Tk.RIGHT, expand=Tk.YES, fill=Tk.X)
            entries.append((field, ent))
        return entries



    def standaardwaarden(self):
        for e in range(len(instellingen.fields)):
            print(instellingen.fields[e], instellingen.entries[e])

    def fetch(entries):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            print('%s: "%s"' % (field, text))



    def makeform(self, fields):
        entries = []
        for field in fields:
            row = Tk.Frame(self)
            lab = Tk.Label(row, width=20, text=field, anchor='w')
            ent = Tk.Entry(row)
            row.pack(side=Tk.TOP, fill=Tk.X, padx=5, pady=5)
            lab.pack(side=Tk.LEFT)
            ent.pack(side=Tk.RIGHT, expand=Tk.YES, fill=Tk.X)
            entries.append((field, ent))
        return entries

