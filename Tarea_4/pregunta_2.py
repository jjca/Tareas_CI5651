import numpy as np
A = np.array([3,4,2,10])
#A = np.array([2,2,1,22,15])
ctr = 0
B = []
print(A)
mem = np.zeros((len(A),len(A)))
i = 0
cantidad = 0
for i in range(0,len(A)):
    for j in range(0,len(A)):
        if A[j] % (i+1) == 0:
            if i == 0:
                mem[i][j] = 1
                cantidad+=1
            else:
                mem[i][j] = np.sum(mem[i-1][:j])
                cantidad+=mem[i][j]
print(mem)
print(cantidad)