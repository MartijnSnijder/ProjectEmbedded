import tkinter as Tk
import pprint


class instellingen(Tk.Toplevel):
    """'1. Minimale uitrol (cm)': 5, '2. Maximale uitrol (cm)': 200,
            '4. Temperatuurwaarde (C)': 21,'3. Lichtwaarde (int)': 150,'5. Meet interval (sec)': 40}"""

    standard_fields = [5, 200, 150, 21, 40]
    changed_fields = standard_fields

    # ----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.geometry("500x300")
        self.title("Instellingen")
        self.buttons()
        self.makeform()
        self.show_standard()
        self.show_current_values()
    # ----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()

    # ----------------------------------------------------------------------
    def buttons(self):
        self.btn_save = Tk.Button(self, text='Opslaan', pady=2, command=self.change_values)
        self.btn_save.grid(row=10, column=1,pady=2)
        self.btn_std = Tk.Button(self, text='Standaard instellingen', pady=2, command=self.to_standard)
        self.btn_std.grid(row=10, column=2,pady=5)
        self.btn_close = Tk.Button(self, text="Close", pady=2,command=self.onClose)
        self.btn_close.grid(row=10, column=3, pady=5)

    # -----------------------------------------------------------------------
    def makeform(self):

        Tk.Label(self, text="").grid(row=0, column=3, sticky=Tk.W)
        Tk.Label(self, text="Huidig:").grid(row=0, column=4, sticky=Tk.W)
        Tk.Label(self, text=" ").grid(row=0, column=5, sticky=Tk.W)
        Tk.Label(self, text="Standaard: ").grid(row=0, column=6, sticky=Tk.W)

        #uitrol instellingen --
        Tk.Label(self, text="Uitrol instellingen:").grid(row=0, sticky=Tk.W,pady=6)

        Tk.Label(self, text="Minimale uitrol (cm)").grid(row=1, sticky=Tk.W)
        self.e1 = Tk.Entry(self)
        self.e1.grid(row=1, column=2)

        Tk.Label(self, text="Maximale uitrol (cm)").grid(row=2, sticky=Tk.W)
        self.e2 = Tk.Entry(self)
        self.e2.grid(row=2, column=2)

        #sensoren -> Lichtwaarde en temperatuurwaarde --
        Tk.Label(self, text="Sensor instellingen:").grid(row=3, sticky=Tk.W, pady=6)

        Tk.Label(self, text="Lichtwaarde (int)").grid(row=4, sticky=Tk.W)
        self.e3 = Tk.Entry(self)
        self.e3.grid(row=4, column=2)

        Tk.Label(self, text="Temperatuurwaarde (C)").grid(row=5, sticky=Tk.W)
        self.e4 = Tk.Entry(self)
        self.e4.grid(row=5, column=2)

        #meetinterval --
        Tk.Label(self, text="Automatisch meten:").grid(row=6, sticky=Tk.W, pady=6)

        Tk.Label(self, text="Meet interval (sec)").grid(row=7, sticky=Tk.W)
        self.e5 = Tk.Entry(self)
        self.e5.grid(row=7, column=2)

    def get_entry_values(self):
        lijst = [self.e1.get(),self.e2.get(),self.e3.get(), self.e4.get(),self.e5.get()]
        return lijst

    def change_values(self):
        lijst = self.get_entry_values()

        for x in range(len(lijst)):
            if lijst[x] != '':
                self.changed_fields[x] = lijst[x]
            self.validate_values()
            self.show_current_values()

    def to_standard(self):
        self.changed_fields = self.standard_fields
        self.show_current_values()

    def show_current_values(self):
        y = 1
        for x in range(len(instellingen.changed_fields)):
            if x == 2 or x == 4:
                y += 1
            Tk.Label(self, text=instellingen.changed_fields[x]).grid(row=y, column=4, sticky=Tk.W)
            y += 1

    def show_standard(self):
        y = 1
        for x in range(len(self.standard_fields)):
            if x == 2 or x == 4:
                y += 1
            Tk.Label(self, text=self.standard_fields[x]).grid(row=y, column=6, sticky=Tk.W)
            y += 1

    def validate_values(self):
        # minimale uitrolstand --
        if int(self.changed_fields[0]) < 5:
            self.changed_fields[0] = 5
        if int(self.changed_fields[0]) > 50:
            self.changed_fields[0] = 50

        # maximale uitrolstand --
        if int(self.changed_fields[1]) > 500:
            self.changed_fields[1] = 500
        if int(self.changed_fields[1]) < 51:
            self.changed_fields[1] = 51

        # Lichtwaarde --
        if int(self.changed_fields[2]) > 255:
            self.changed_fields[2] = 255
        if int(self.changed_fields[2]) < 125:
            self.changed_fields[2] = 125

        # Temperatuurwaarde --
        if int(self.changed_fields[3]) > 40:
            self.changed_fields[3] = 40
        if int(self.changed_fields[3]) < 0:
            self.changed_fields[3] = 0

        # Meet interval --
        if int(self.changed_fields[4]) > 600:
            self.changed_fields[4] = 600
        if int(self.changed_fields[4]) < 5:
            self.changed_fields[4] = 5
