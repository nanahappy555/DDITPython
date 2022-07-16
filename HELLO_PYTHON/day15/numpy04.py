import numpy as np

arr = range(100)
arr2 = list(range(100))
arr_n = np.array(arr2)

arr_1010 = np.reshape(arr_n,(10,10))

print(arr) #range(0, 100)
print(arr2) #[0,1,2,3,...]
print(arr_n) # [0 1 2 3 4 5 ...]
print(arr_1010) # 2차원배열