import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock

ds = DaoStock()

arrx = np.zeros(16)

arry = list(range(16))

# 이미 결과가 정렬된 데이터가 들어간 배열이라서 for문 돌릴 필요가 없음
arr_name = ds.selectAllNames()

# for
arrz = []
for i in arr_name:
    arrz.append(ds.selects(i))


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

for idx,arr in enumerate(arrz):
    arr_n = np.array(arr)
    # print(idx,arr_n,arr_name[idx],arr_n/arr_n[0])
    ax.plot(arrx+idx    ,arry   ,arr_n/arr_n[0])

plt.show()



