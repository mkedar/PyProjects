import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from gpiozero import CPUTemperature

def fetch_temperature():
    cpu = CPUTemperature()
    return cpu.temperature

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'r-', animated=True)

def init():
    ax.set_xlim(0, 10) 
    ax.set_ylim(30, 80)  
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(fetch_temperature())

    if len(xdata) > 10:
        ax.set_xlim(max(xdata) - 9, max(xdata) + 1)
    else:
        ax.set_xlim(0, 10)

    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True)
plt.show()
