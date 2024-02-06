import matplotlib.pyplot as plt
import numpy as np

def elips(p = 3, e = 0.6):

    f = np.arange(0, 8*np.pi, 0.01)

    r = p/(1+e*np.cos(f))

    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y)
    plt.savefig('fig_16.png')

if __name__ == '__main__':
    elips()