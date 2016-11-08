import serial


class connect:
    # Hier wordt de Arduino afgelezen en de byte wordt in "ser" gezet
    ser =  serial.Serial('COM3', 9600, timeout=0)

    def light(self):
        datalist = []
        while 1:
            try:
                for line in connect.ser:
                    intvalue = int(line.rstrip().decode('utf-8'))  # Byte > Str > Int
                    datalist.append(intvalue)  # De int wordt in een lijst gezet

                    # Het gemiddele van de laatste 10 waarden in de lijst wordt geprint
                    average = sum(datalist[-10:]) / len(datalist[-10:])
                    self.average = round(average)

            except connect.ser.SerialTimeoutException:
                return ('Data could not be read')

    def lightgraph(self):
        datalist = []
        while 1:
            try:
                for line in connect.ser:
                    intvalue = int(line.rstrip().decode('utf-8'))  # Byte > Str > Int
                    datalist.append(intvalue)  # De int wordt in een lijst gezet
                    return datalist
            except ValueError:
                return 0



    #kopie versie light
    def temperature(self):

        datalist = []
        while 1:
            try:
                for line in connect.ser:
                    intvalue = int(line.rstrip().decode('utf-8'))  # Byte > Str > Int
                    datalist.append(intvalue)  # De int wordt in een lijst gezet

                    # Het gemiddele van de laatste 10 waarden in de lijst wordt geprint
                    average = sum(datalist[-10:]) / len(datalist[-10:])
                    return round(average)

            except connect.ser.SerialTimeoutException:
                return ('Data could not be read')

    def getAverage(self):
        return self.average