from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import numpy as np 

def circle_move (C, x0, y0, D):

    for i in range(1, 8):
        n = i-1
        xi = (xn)**2-(yn)**2+C
        yi = 2*x(i-1)*y(i-1)+D
    return xi, yi

def animate(i):
    ball.set_data(circle_move(D=0.33, x0 = 0.01, y0=0.01, C = 0.3))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='r')

    edge = 3
    plt.axis('equal')    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=100,
                        interval=30
                        )
    
    ani.save('animation_7.gif')