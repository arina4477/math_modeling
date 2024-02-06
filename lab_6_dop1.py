import matplotlib.pyplot as plt
import numpy as np

def lisagy (a = 1, A = 1, B = 4, b = 2):

    f = np.pi/2

    t = np.arange(0.01, 9, 0.1)

    x = A * np.sin(a*t+f)


    y = B * np.sin(b*t)

    plt.plot(x, y)
    plt.savefig('fig_15.png')

if __name__ == '__main__':
    lisagy()    