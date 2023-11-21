import numpy as np
N = 5
M = 4

A = np.zeros((N, M))
print(A)

for i in range(0 , M):
    for j in range (0 ,M):
        A[i, j] = np.sin(N * i - M * j)

print(A)
