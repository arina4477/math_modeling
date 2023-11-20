import numpy as np
from lab_3_task1 import free_fall as g

x0 = 2
V0 = 5
y0 = 4
t = np.arange(0, 5, 0,11)

x = x0 + V0 * t
y = y0 + V0 * t - (g * t**2)/2

print(x)


