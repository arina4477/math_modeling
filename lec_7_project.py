import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

xdata, ydata = [], []

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 3*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y


def update(frame):
    xdata.append(2 * (frame - np.sin(frame)))
    ydata.append(2 * (1 - np.cos(frame)))
    anim_object.set_data(xdata, ydata)
    ball.set_data(circle_move(R=4, vx0 = 1.8, vy0=0.0001, time = frame))


if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r', label ='triangle')
    anim_object, = plt.plot([], [], '-', lw=2)

    edge = 20
    plt.axis('equal')
    ax.set_xlim(0, edge)
    ax.set_ylim(-8, edge)

    ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(0, 3*np.pi, 0.1),
                    interval=100
                    )

    
    ani.save('animation_8.gif')