from math import ceil, log
import random
import numpy as np

def freivalds(A,B,C,n):
    X = []
    for _ in range(n):
        X.append(int(random.uniform(0,2)))
    X = [1,1,0]
    # X*A
    W = [0]*n
    for i in range(n):
        for j in range(n):
            W[i] = X[j]*A[j][i]+W[i]

    # W*B
    Y = [0]*n
    for i in range(n):
        for j in range(n):
            Y[i] = W[j]*B[j][i]+Y[i]

    # X*C
    Z = [0]*n
    for i in range(n):
        for j in range(n):
            Z[i] = X[j]*C[j][i]+Z[i]

    if Y == Z: 
        return True
    return False


def repeatFreivalds(A,B,C,n,k):
    for i in range(1,k):
        if not freivalds(A,B,C,n):
            return False
    return True

def freivaldsEpsilon(A,B,C,n,e):
    k = ceil(log(1/e))
    print(k)
    return repeatFreivalds(A,B,C,n,k)


A = np.array([[6,1,1,3],
      [4,-2,5,1],
      [2,8,7,6],
      [3,1,9,7]
    ])
B = np.array(np.linalg.inv(A))
print(B)
C = np.identity(len(A))
print(C)

print(np.matmul(A,B))
print(freivaldsEpsilon(A,B,C,3,0.0001))