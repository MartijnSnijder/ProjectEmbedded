import serial
import time

class connect:
    # Hier wordt de Arduino afgelezen en de byte wordt in "ser" gezet
    ser =  serial.Serial('COM3', 9600, timeout=0)

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
                    intvalue = connect.to_int(line.rstrip().decode('utf-8'))  # Byte > Str > Int
                    datalist.append(intvalue)  # De int wordt in een lijst gezet

                    # Het gemiddele van de laatste 10 waarden in de lijst wordt geprint
                    average = sum(datalist[-10:]) / len(datalist[-10:])
                    self.average = round(average)



            except connect.ser.SerialTimeoutException:
                return ('Data could not be read')

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