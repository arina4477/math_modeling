import matplotlib.pyplot as plt
import numpy as np

def rose(k = 5):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = np.sin(k*f)

    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y)
    plt.savefig('fig_13.png')
    plt.close()




def rose_2(k = 1/5):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = np.sin(k*f)

    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plotr(x, y)
    plt.savefig('fig_14.png')



if __name__ == '__main__':
    rose()
    rose_2()