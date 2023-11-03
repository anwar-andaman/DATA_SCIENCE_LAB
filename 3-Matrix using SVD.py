import numpy as np
X=np.array([[11,12,13],[14,15,16],[17,18,19]])
#perform SVD
U,S, VT=np.linalg.svd(X)
#choose the number of component to keep
n_components=2
#reconstruct the matrix with reduced dimensions
X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components]))
print("Orginal Matrix")
print(X)
print("\nReconstructed Matrix (with reduced dimension)")
print(X_reconstructed)

"""
***********OUTPUT***********8**

Orginal Matrix
[[11 12 13]
 [14 15 16]
 [17 18 19]]

Reconstructed Matrix (with reduced dimension)
[[11. 12. 13.]
 [14. 15. 16.]
 [17. 18. 19.]]
"""
