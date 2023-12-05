import numpy as np


def func(figure, r, b, c, n):
    ''' figure = 1 - circle, figure = 2 - square
    '''
    r = 0
    b = 0
    c = 0
    n = 0
    if figure==1:
        S = np.pi * r**2
    elif figure==2:
        S = b**2
    else:
        S = c * n 
    
    return S



func(1, r=3)