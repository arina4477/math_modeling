import matplotlib.pyplot as plt


def giperbola(K=-10, M=10, N=0.01):
    x = np.arange(K, M, N)
    y = 1/x

    plt.plot(x, y)
    plt.savefig('fig_6.png')

if __name__ == '__main__':
    giperbola_plotter()
