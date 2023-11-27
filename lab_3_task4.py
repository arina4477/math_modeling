import numpy as np
N = 5
M = 4

A = np.zeros((N, M))


for i in range(0 , N):
    for j in range (0 ,M):
        A[i, j] = np.sin(N * i - M * j)
        if A[i, j] < 0:
            A[i, j] = 0
            

print(A)
