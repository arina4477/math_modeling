import matplotlib.pyplot as plt
import numpy as np

def spiral(k = 3):
    t = np.arange(0, 8 * np.pi, 0.01)
    r = k * t

    plt.polar(t, r)
    plt.savefig('fig_11.png')

if __name__ == '__main__':
    spiral()