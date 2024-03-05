

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def update(frame):
    xdata.append(np.sin(frame)*(np.e**np.cos(frame)-2*np.cos(4*frame)+(np.sin(frame/12)**5)))
    ydata.append(np.cos(frame) * (np.e**np.cos(frame)-2*np.cos(4*frame)+(np.sin(frame/12)**5)))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(0, 12*np.pi, 0.1),
                    interval=30
                    )

ani.save('animation_5.gif')
plt.close()

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def update(frame):
    xdata.append(16*np.sin(frame)**3)
    ydata.append(13 * np.cos(frame) - 5*np.cos(2*frame)-2*np.cos(3*frame)-np.cos(4*frame))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=30
                    )

ani.save('animation_6.gif')
