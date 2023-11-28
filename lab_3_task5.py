import numpy as np
from lab_3_task4 import A as a

print(4)

b = np.zeros(len(a[::1, 1]))
print(b)
for i in range(0, len(a[::1, 1])):
    a[::1, 1] = a[::1, 0]

    a[::1, 0] =a[::1, 1]

    print(a)