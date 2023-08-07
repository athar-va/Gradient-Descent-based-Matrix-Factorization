import numpy as np
import random
import sys
np.set_printoptions(threshold=sys.maxsize, linewidth=200)
np.set_printoptions(suppress=True)


B= np.identity(10)
#B[9][9]=-1

alpha=0.0001

a=np.random.normal(loc=0, scale=1, size=(4,10))
a=np.round(a,5)

print(a)
step=0
L=99999
while L > 0.00000000001:

    #print(a)

    M = np.subtract(B,np.matmul(a.transpose(),a))
    L=pow(np.sum(M),2)
    print(round(L,7))

    GA=np.dot(4,np.matmul(a,np.subtract(np.matmul(a.transpose(),a),B)))

    a=np.subtract(a,np.dot(alpha,GA))
    #print(a)
    #print(np.matmul(a.transpose(),a))
    step+=1

print(step)
#print(A)
print("B")
print (B)
print("Factor")
print(a)
print("product")
print(np.matmul(a.transpose(),a))