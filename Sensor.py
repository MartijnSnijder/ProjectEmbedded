import serial
import time
import win32com.client
from matplotlib import pyplot as plt

class connect:
    # COM-poort zoeken waar Arduino op aangesloten is
    connected = False
    wmi = win32com.client.GetObject("winmgmts:")
    for port in wmi.InstancesOf("Win32_SerialPort"):
        if "Arduino" in port.Name:
            comPort = port.DeviceID
            ser = serial.Serial(comPort, 9600, timeout=1)
            connected = True
            if ser != 0:
                print("Arduino connected to", comPort)
        else:
            print("Arduino is not connected")
    intvalue = 1
    plt.ion()  # set plot to animated

    ydata = [0] * 50
    ax1 = plt.axes()

    # make plot
    line, = plt.plot(ydata)

    # Deze functie zet een waarde om naar een int
    def to_int(s):
        try:
            return int(s)
        except ValueError:
            return float(s)


    def light(self):
        while True:
            data = connect.ser.readline().rstrip()
            if len(data.split(".")) == 2:
                ymin = float(min(connect.ydata)) - 10
                ymax = float(max(connect.ydata)) + 10
                plt.ylim([ymin, ymax])
                connect.ydata.append(data)
                del connect.ydata[0]
                connect.line.set_xdata(connect.np.arange(len(connect.ydata)))
                connect.line.set_ydata(connect.ydata)  # update the data
                plt.draw()  # update the plot


    def inputnumber(self):
        while 1:
            try:
                for line in connect.ser:
                    time.sleep(1)
                    intvalue = connect.to_int(line.rstrip().decode('utf-8'))  # Byte > Str > Int
                    return round(intvalue)

            except ValueError:
                return 1

    def getAverage(self):
        return self.average

connect.light(connect)