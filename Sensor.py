import serial
import time


class connect:
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
                    print(round(average))

                time.sleep(1)

            except ser.SerialTimeoutException:
                print('Data could not be read')
            time.sleep(1)
