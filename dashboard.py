from tkinter import *
root = Tk()
from Sensor import *

class mainframe():
    def __init__(self, parent):
        self.parent = parent
        self.initUI()

    def initUI(self):
        #Slider widget voor scherm uitrol
        var = DoubleVar()
        scale = Scale(root, from_=0, to_=160, variable = var, orient_=HORIZONTAL,
                      tickinterval_=20, length_=300, label="Zonnescherm handmatig in/uitrollen (cm)")
        scale.pack()

        #Label lichtintensiteit
        intenslabel = Label(root, text="Lichtintensiteit:")
        ## .pack() gebruiken als je widget wil laten zien
        intenslabel.pack()

        #Label voor waarde lichtintensiteit
        intens = Label(root, text="waarde lichtintensiteit")
        intens.pack()

        # Label gemiddelde lichtintensiteit
        avgintenslabel = Label(root, text="Gemiddelde lichtintensiteit:")
        avgintenslabel.pack()

        # Label voor waarde gemiddelde lichtintensiteit
        avgintens = Label(root, text=connect.getAverage(connect.light(connect)))
        avgintens.pack()

def main():
    root.title("Dashboard")
    app = mainframe(root)
    root.mainloop()

if __name__ == '__main__':
    main()