import numpy as np

def aver_func(a):
    x = np.sum(a) / len(a)
    return x
   
print(aver_func([1, 2, 3, 4, 5, 6]))