import serial
import time


class connect:
    # Hier wordt de Arduino afgelezen en de byte wordt in "ser" gezet
    def light(self):
        ser = serial.Serial('COM3', 9600, timeout=0)

        datalist = []
        while 1:
            try:
                for line in ser:
                    intvalue = int(line.rstrip().decode('utf-8'))  # Byte > Str > Int
                    datalist.append(intvalue)  # De int wordt in een lijst gezet

                    # Het gemiddele van de laatste 10 waarden in de lijst wordt geprint
                    average = sum(datalist[-10:]) / len(datalist[-10:])
                    return round(average)

                    time.sleep(1)

            except ser.SerialTimeoutException:
                return('Data could not be read')
                time.sleep(1)
