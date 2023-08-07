import numpy as np
import random
import sys
np.set_printoptions(threshold=sys.maxsize, linewidth=200)
np.set_printoptions(suppress=True)


A = np.random.standard_normal(size=(5,10))

B = np.matmul(A.transpose(), A)

alpha=0.01

# normal(loc=0, scale=1, size=(k,10)) and varying k
a=np.random.normal(loc=0, scale=1, size=(7,10))
a=np.round(a,5)

print(a)
step=0
L=99999
while L > 0.0000001:

    M = np.subtract(B,np.matmul(a.transpose(),a))
    L=pow(np.sum(M),2)
    print(round(L,7))

    GA=np.dot(4,np.matmul(a,np.subtract(np.matmul(a.transpose(),a),B)))

    a=np.subtract(a,np.dot(alpha,GA))
    step+=1

print(step)
print("Initial factor of B")
print(A)
print("B")
print (B)
print("Factor")
print(a)
print("product")
print(np.matmul(a.transpose(),a))
