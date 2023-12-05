import numpy as np


def func(a, b, N):
    X = np.linspace(a, b, N)
    Y = X**2
    return Y 


print(func(1, 10, 200))


