import numpy as np
A=np.array([[11,12],[13,14]])
B=np.array([[14,15],[16,17]])
C=A+B
D=A-B
E=A*B
#MATRIX MULTIPLICATION
F=np.dot(A,B)
A_TRANSPOSE=A.T
print("Addition:")
print(C)
print("\nSubtraction:")
print(D)
print("\nElement wise Mutiplication:")
print(E)
print("\nMultiplication:")
print(F)
print("Matrix Tanspose: \n",A_TRANSPOSE)


"""OUTPUT
Addition:
[[25 27]
 [29 31]]

Subtraction:
[[-3 -3]
 [-3 -3]]

Element wise Mutiplication:
[[154 180]
 [208 238]]

Multiplication:
[[346 369]
 [406 433]]
Matrix Tanspose: 
 [[11 13]
 [12 14]]
"""
