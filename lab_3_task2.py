import numpy as np
from lab_3_task1 import free_fall as g 

h = 100
a = np.pi/3
b = 30

v=((g * h*np.tan(b)**2) / (2 * np.cos(a)**2 * (1 - np.tan(b) * np.tan(a))))**0.5
print(v)