import tkinter as tk
import pygubu


class Application:
    def __init__(self, master):

        # Maak builder
        self.builder = builder = pygubu.Builder()

        # Laad GUI bestand
        ## GUI is gemaakt met pygubu, is .ui bestand in project directory
        builder.add_from_file('GUI.ui')

        # Maak widget mbv master als 'parent'
        self.mainwindow = builder.get_object('Toplevel_1', master)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()