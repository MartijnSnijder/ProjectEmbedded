import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

lines = serial.Serial('COM3', 19200, timeout=0)
#lines = int.from_bytes(lines, byteorder='big')

xs = []
ys = []
x = 0

def animate(i):
    global xs, xy, x
    for line in lines:
        line = int.from_bytes(line, byteorder='big')
        y = line
        xs.append(x)
        ys.append(y)
        if len(xs) > 10:
            xs.pop(0)
        if len(ys) > 10:
            ys.pop(0)
        x += 1
        print(xs)
        print(ys)
        ax1.clear()
        ax1.plot(xs, ys)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()