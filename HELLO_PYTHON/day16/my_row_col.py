import numpy as np

a = np.arange(15).reshape(3, 5)


a_t = np.transpose(a)


print(a)

print(a_t)
"""
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
[[ 0  5 10]
 [ 1  6 11]
 [ 2  7 12]
 [ 3  8 13]
 [ 4  9 14]]

"""