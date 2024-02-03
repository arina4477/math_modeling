import matplotlib.pyplot as plt
import numpy as np

def spiral(k = 3):
    f = np.arange(0.01, 8 * np.pi, 0.01)
    r = k/f**0.5

    plt.polar(f, r)
    plt.savefig('fig_12.png')

    
if __name__ == '__main__':
    spiral()