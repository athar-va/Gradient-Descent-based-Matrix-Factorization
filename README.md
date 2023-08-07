# Project: Gradient-Descent-based-Matrix-Factorization

## Purpose:
The project aims to factorize a matrix using gradient descent and analyze the loss function. It explores the convergence behavior of the algorithm and its dependency on initial starting points and matrix properties. The starting point is then varied to note the behaviour of the algorithm.

## Problems Solved:
- Matrix Factorization: Implementing gradient descent to factorize a given matrix B into two matrices A and A^T.
- Loss Function Analysis: Analyzing the behavior of the loss function during the gradient descent process.
- Convergence Behavior: Investigating how the algorithm converges to a solution and the influence of the initial starting points.

## Major Learnings and Observations:
- We do not recover the same A everytime for a initial starting point. This is because gradient descent being a local search algorithm can converge at a local minima which may give a smaller loss but may be different from the actual minima that we started from (ie the original A)
- Following are the observations when the value of k (rows of the matrix) is varied:
  * It is observed that for values of k < actual dimension, the loss function does not converge
  * It is observed that for values of k >= actual dimension, the loss function converges to 0.
- This is because when we use k < actual dimension, the operation A^t A induces linear dependency. As a result, we cannot use a lower dimensional k to derive higher dimensional factors.
- If B is taken as an Identity matrix, the loss function converges even for a k less than the actual k 

## Technologies and Libraries Used:
- Python
- NumPy

## Concepts Applied:
- Gradient Descent
- Matrix Factorization
- Loss Function
- Convergence Analysis

#project #matrixfactorization #gradientdescent #lossfunction #convergenceanalysis #python #numericalcomputing
