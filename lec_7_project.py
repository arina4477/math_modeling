import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()



anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(0, 20)
ax.set_ylim(-10, 10)

def update(frame, a=2):
    xdata.append(a * (frame - np.sin(frame)))
    ydata.append(a * (1 - np.cos(frame)))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(0, 3*np.pi, 0.1),
                    interval=1
                    )

ani.save('animation_7.gif')

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(-100, 3*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

def animate(i):
    ball.set_data(circle_move(R=2, vx0 = 0.09, vy0=0.0001, time = i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r', label ='triangle')

    edge = 8
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30
                        )
    
    ani.save('animation_8.gif')