import numpy as np 
from lab_3_task4 import A as a, N



for i in range(0, N):
    s = a[i , 0] 
    a[i , 0] = a[i, 1]
    a[i, 1] = s
print(a)