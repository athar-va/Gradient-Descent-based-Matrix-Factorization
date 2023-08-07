#Generate a random B, taking D = 10; k = 10, and taking A as a random initial atrix, implementing this process to show that L decreases over time to 0

import numpy as np
import random
import sys

# Configurations to show the whole output in console
np.set_printoptions(threshold=sys.maxsize, linewidth=200)
np.set_printoptions(suppress=True)

# Generate B from A^T.A
A = np.random.standard_normal(size=(10,10))
B = np.matmul(A.transpose(), A)

# Setting a small step size
alpha=0.005

# Generating a random matrix a
a=np.random.normal(loc=0, scale=1, size=(10,10))
a=np.round(a,5)

step=0
L=99999

# Loop untill the loss hits a desirable level
while L > 0.0001:

    M = np.subtract(B,np.matmul(a.transpose(),a))
    L=pow(np.sum(M),2)
    print(round(L,7))

    # Minimize loss
    GA=np.dot(4,np.matmul(a,np.subtract(np.matmul(a.transpose(),a),B)))

    a=np.subtract(a,np.dot(alpha,GA))
    step+=1


print(step)
print("B")
print (B)
print("Factor")
print(a)
print("Product of the factors is :")
print(np.matmul(a.transpose(),a))
