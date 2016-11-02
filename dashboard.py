from tkinter import *
root = Tk()

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

def main():
    root.title("Dashboard")
    app = mainframe(root)
    root.mainloop()

if __name__ == '__main__':
    main()