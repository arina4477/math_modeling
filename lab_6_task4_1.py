import matplotlib.pyplot as plt
import numpy as np

def log_spiral(b = 0.1):
    n = np.arange(0, 8 * np.pi, 0.001)
    r = np.e**(b*n)

    plt.polar(n, r)
    plt.savefig('fig_10.png')
    
if __name__ == '__main__':
    log_spiral()


