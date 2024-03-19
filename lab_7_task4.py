from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import numpy as np 

N = 10

D=0.33
x0 = 0.01
y0=0.01
C = 0.3

x = []
x.append(x0)
y = []
y.append(y0)
for i in range(1, N):
    x.append(x[i-1]**2-y[i-1]**2+C)
    y.append(2*x[i-1]*y[i-1]+D)


def animate(i):
    ball.set_data(x[:i], y[:i])

if __name__ == '__main__':
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label ='Ball')

    edge = 3  
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        interval=100,
                        frames = N
                        )
    
    ani.save('animation_7.gif')