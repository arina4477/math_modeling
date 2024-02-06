import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter (k = 1):

    x = np.arange(0.01, 10, 0.1)
    y = k / x

    plt.plot(x, y)
    plt.savefig('fig_6.png')

if __name__ == '__main__':
    giperbola_plotter()


