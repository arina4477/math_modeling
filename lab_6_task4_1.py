import matplotlib.pyplot as plt
import numpy as np

def log_spiral(b = 0.1):
    f = np.arange(0, 8 * np.pi, 0.001)
    r = np.e**(b*f)

    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y)
    plt.savefig('fig_10.png')
    
if __name__ == '__main__':
    log_spiral()


