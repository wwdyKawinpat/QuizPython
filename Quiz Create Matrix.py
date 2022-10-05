
import numpy as np
M = np.array([[1., 2., 3.],
           [4., 5., 6.],
           [7., 8., 9.],
           [10., 11., 12.]])

# Result is different.
#M[2,:] show result only in index[2].
#M[2,:] show result from index[2] to end.

M[2,:]
#output array([7.,8.,9.])

print(M[2:])
#output array([[ 7.,  8.,  9.],[10., 11., 12.]])
