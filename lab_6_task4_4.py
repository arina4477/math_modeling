import matplotlib.pyplot as plt
import numpy as np

def rose(k = 5):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = np.sin(k*f)

    plt.polar(f, r)
    plt.savefig('fig_13.png')


if __name__ == '__main__':
    rose()



def rose_2(k = 1/5):
    f = np.arange(0, 8 * np.pi, 0.01)
    r = np.sin(k*f)

    plt.polar(f, r)
    plt.savefig('fig_14.png')



if __name__ == '__main__':
    rose_2()