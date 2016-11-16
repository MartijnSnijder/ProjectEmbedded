import serial
import time

class connect:
    # COM-poort zoeken waar Arduino op aangesloten is
    wmi = win32com.client.GetObject("winmgmts:")
    for port in wmi.InstancesOf("Win32_SerialPort"):
        # print port.Name #port.DeviceID, port.Name
        if "Arduino" in port.Name:
            comPort = port.DeviceID
            print
            comPort, "is Arduino"
    # Hier wordt de Arduino afgelezen en de byte wordt in "ser" gezet
    ser = serial.Serial('COM3', 9600, timeout=0)
    intvalue = 1

    # Deze functie zet een waarde om naar een int
    def to_int(s):
        try:
            return int(s)
        except ValueError:
            return float(s)

    def light(self):
        datalist = []
        while 1:
            try:
                for line in connect.ser:
                    intvalue = (line.rstrip().decode('utf-8'))  # Byte > Str > Int
                    datalist.append(intvalue)  # De int wordt in een lijst gezet
                    print(intvalue)
                    # Het gemiddele van de laatste 10 waarden in de lijst wordt geprint
                    average = sum(datalist[-10:]) / len(datalist[-10:])
                    self.average = round(average)
                    self.intvalue = intvalue

            except Exception:
                return ('Data could not be read')
            print(self.intvalue)

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