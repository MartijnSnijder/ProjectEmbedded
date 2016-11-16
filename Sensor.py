import serial
import time
import win32com.client
import numpy as np
from matplotlib import pyplot as plt

class connect:
    # COM-poort zoeken waar Arduino op aangesloten is
    connected = False
    wmi = win32com.client.GetObject("winmgmts:")
    for port in wmi.InstancesOf("Win32_SerialPort"):
        if "Arduino" in port.Name:
            comPort = port.DeviceID
            ser = serial.Serial(comPort, 19200, timeout=0)
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
    plt.ylim([0, 400])  # set the y-range to 0 to 400

    # Deze functie zet een waarde om naar een int
    def to_int(s):
        try:
            return int(s)
        except ValueError:
            return float(s)


    def light(self):
        while True:
            data = connect.ser.readline().rstrip()
            data = int.from_bytes(data, byteorder = 'big')  # read data from serial
            # port and strip line endings
            ymin = float(min(connect.ydata)) - 10
            ymax = float(max(connect.ydata)) + 10
            plt.ylim([ymin, ymax])
            connect.ydata.append(data)
            del connect.ydata[0]
            connect.line.set_xdata(np.arange(len(connect.ydata)))
            connect.line.set_ydata(connect.ydata)  # update the data
            plt.draw()  # update the plot

        """ while True:
            for x in connect.ser:
                # data = connect.ser.readline().rstrip().decode('utf-8')
                data = (int.from_bytes(x, byteorder = 'big'))
                connect.ydata.append(data)
                del connect.ydata[0]
                connect.line.set_xdata(np.arange(len(connect.ydata)))
                connect.line.set_ydata(connect.ydata)  # update the data
                plt.draw()  # update the plot
                time.sleep(1) """

connect.light(connect)