#### Elementary Matrix

import numpy as np

A = np.array([[0.0, 0.1, 0.2, 0.3, 0.4],
              [1.8, 1.6, 1.4, 1.2, 1.0],
              [2.1, 2.3, 2.5, 2.7, 2.9]])

print(A.dtype)      # float64
print(A.size)       # 15
print(A.ndim)       # 2
print(A.shape)      # (3, 5)

A = np.array([[1.1, 1.2, 2.3],
              [3.4, 5.5, 8.6]])
B = np.array([[3.1, 4.1, 5.9],
              [2.6, 5.3, 5.8]])
C = np.array([[1.1, 1.2, 2.3],
              [3.4, 5.5, 8.6]],dtype=complex)
D = np.matrix([[1.1, 1.2, 2.3],
               [3.4, 5.5, 8.6]],dtype=complex)
E = np.matrix([[3.14, 1.59],
               [2.65, 3.58]])

print(type(A))      
    # <class 'numpy.ndarray'>
print(type(B))      
    # <class 'numpy.ndarray'>
print(type(C))      
    # <class 'numpy.ndarray'>
print(type(D))      
    # <class 'numpy.matrix'>

re = A + 2
print(re)
    # [[ 3.1  3.2  4.3]
    #  [ 5.4  7.5 10.6]]

re = A - 2
print(re)
    # [[-0.9 -0.8  0.3]
    #  [ 1.4  3.5  6.6]]

re = A * 2
print(re)
    # [[ 2.2  2.4  4.6]
    #  [ 6.8 11.  17.2]]

re = A / 2
print(re)
    # [[0.55 0.6  1.15]
    #  [1.7  2.75 4.3 ]]

re = A % 2
print(re)
    # [[1.1 1.2 0.3]
    #  [1.4 1.5 0.6]]

re = A ** 2
print(re)
    # [[ 1.21  1.44  5.29]
    #  [11.56 30.25 73.96]]

re = A.T
print(re)
    # [[1.1 3.4]
    #  [1.2 5.5]
    #  [2.3 8.6]]

re = np.conj(C)
print(re)
    # [[1.1-0.j 1.2-0.j 2.3-0.j]
    #  [3.4-0.j 5.5-0.j 8.6-0.j]]

re = D.H
print(re)
    # [[1.1-0.j 3.4-0.j]
    #  [1.2-0.j 5.5-0.j]
    #  [2.3-0.j 8.6-0.j]]

re = D.I
print(re)
    # [[ 2.07835392+0.j -0.5113589 +0.j]
    #  [-2.22811141+0.j  0.62719803+0.j]
    #  [ 0.60328016+0.j -0.0826708 +0.j]]

re = A + B
print(re)
    # [[ 4.2  5.3  8.2]
    #  [ 6.  10.8 14.4]]

re = A - B
print(re)
    # [[-2.  -2.9 -3.6]
    #  [ 0.8  0.2  2.8]]

re = A * B
print(re)
    # [[ 3.41  4.92 13.57]
    #  [ 8.84 29.15 49.88]]

re = np.dot(A.T,B)
print(re)
    # [[12.25 22.53 26.21]
    #  [18.02 34.07 38.98]
    #  [29.49 55.01 63.45]]

re = np.dot(A,B.T)
print(re)
    # [[21.9  22.56]
    #  [83.83 87.87]]

re = np.trace(E)
print(re)
    # 6.720000000000001

re = np.ndim(E)
print(re)
    # 2

re = np.linalg.det(E)
print(re)
    # 7.0277

re,rp = np.linalg.eig(E)
print(re)
    # [1.29556303 5.42443697]
print(rp)
    # [[-0.65293211 -0.57126457]
    #  [ 0.75741643 -0.82076598]]

## Special Matrices
n = 4
A = np.identity(n)
print(A)
    # [[1. 0. 0. 0.]
    #  [0. 1. 0. 0.]
    #  [0. 0. 1. 0.]
    #  [0. 0. 0. 1.]]

A = np.eye(n, k = -1)
print(A)
    # [[0. 0. 0. 0.]
    #  [1. 0. 0. 0.]
    #  [0. 1. 0. 0.]
    #  [0. 0. 1. 0.]]

A = np.eye(n, k = 0)
print(A)
    # [[1. 0. 0. 0.]
    #  [0. 1. 0. 0.]
    #  [0. 0. 1. 0.]
    #  [0. 0. 0. 1.]]

A = np.eye(n, k = 1)
print(A)
    # [[0. 1. 0. 0.]
    #  [0. 0. 1. 0.]
    #  [0. 0. 0. 1.]
    #  [0. 0. 0. 0.]]

A = np.eye(n, k = 2)
print(A)
    # [[0. 0. 1. 0.]
    #  [0. 0. 0. 1.]
    #  [0. 0. 0. 0.]
    #  [0. 0. 0. 0.]]

A = np.diag(np.arange(0,12,2))
print(A)
    # [[ 0  0  0  0  0  0]
    #  [ 0  2  0  0  0  0]
    #  [ 0  0  4  0  0  0]
    #  [ 0  0  0  6  0  0]
    #  [ 0  0  0  0  8  0]
    #  [ 0  0  0  0  0 10]]

A = np.diag(np.linspace(0,10,6))
print(A)
    # [[ 0.  0.  0.  0.  0.  0.]
    #  [ 0.  2.  0.  0.  0.  0.]
    #  [ 0.  0.  4.  0.  0.  0.]
    #  [ 0.  0.  0.  6.  0.  0.]
    #  [ 0.  0.  0.  0.  8.  0.]
    #  [ 0.  0.  0.  0.  0. 10.]]
