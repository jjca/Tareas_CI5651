from math import ceil, log2
import random
import numpy as np

def freivalds(A,B,C,n):
    X = np.random.randint(2,size=n)
    print(X)
    # X*A
    #W = np.matmul(X,A)
    #print(W)
    #for i in range(n):
    #    for j in range(n):
    #        W[i] = X[j]*A[j][i]+W[i]

    # W*B
    #Y = np.matmul(W,B)
    #Y = [0]*n
    #for i in range(n):
    #    for j in range(n):
    #        Y[i] = W[j]*B[j][i]+Y[i]

    # X*C
    """ Z = [0]*n
    for i in range(n):
        for j in range(n):
            Z[i] = X[j]*C[j][i]+Z[i] """
    #Z = np.matmul(X,C)

    if np.array_equal(np.matmul(np.matmul(X,A),B),np.matmul(X,C)): 
        print("Aaaa")
        return True
    return False


def repeatFreivalds(A,B,C,n,k):
    for _ in range(0,k):
        if freivalds(A,B,C,n) == False:
            return False
    return True

def freivaldsEpsilon(A,B,C,n,e):
    k = ceil(log2(1/e))
    print(k)
    return repeatFreivalds(A,B,C,n,k)


#A = np.array([[6,1,1,3],
   #   [4,-2,5,1],
   #   [2,8,7,6],
  #    [3,1,9,7]
 #   ])

A = np.random.randint(10,size=(2,2))
#
B = np.array(np.linalg.inv(A))

""" A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
B = np.array([[3,1,4],
              [1,5,9],
              [2,6,5]])
C = np.array([[11,29,37],
              [29,65,91],
              [47,99,45]])
 """
print(B)
C = np.identity(len(A))
print(C)

print(np.matmul(A,B))
res = freivaldsEpsilon(A,B,C,len(A),0.00001)
if res:
    print("Son iguales")
else:
    print("Son diferentes")