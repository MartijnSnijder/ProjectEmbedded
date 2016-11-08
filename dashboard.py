from tkinter import *
root = Tk()
import serial
import time

class mainframe():
    def __init__(self, parent):
        self.parent = parent
        self.initUI()

    # Deze functie zet een waarde om naar een int
    def to_int(s):
        try:
            return int(s)
        except ValueError:
            return float(s)

    # Hier wordt de Arduino afgelezen en de byte wordt in "ser" gezet
    ser = serial.Serial('COM3', 9600, timeout=0)

    datalist = []

    while 1:
        try:
            for line in ser:
                intvalue = to_int(line.rstrip().decode('utf-8'))  # Byte > Str > Int
                datalist.append(intvalue)  # De int wordt in een lijst gezet

                # Het gemiddele van de laatste 10 waarden in de lijst wordt geprint
                average = sum(datalist[-10:]) / len(datalist[-10:])
                # print(round(average))

            time.sleep(1)

        except ser.SerialTimeoutException:
                break

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
        intens = Label(root, text="ser")
        intens.pack()

        # Label gemiddelde lichtintensiteit
        avgintenslabel = Label(root, text="Gemiddelde lichtintensiteit:")
        avgintenslabel.pack()

        # Label voor waarde gemiddelde lichtintensiteit
        avgintens = Label(root, text="average")
        avgintens.pack()

def main():
    root.title("Dashboard")
    app = mainframe(root)
    root.mainloop()

if __name__ == '__main__':
    main()