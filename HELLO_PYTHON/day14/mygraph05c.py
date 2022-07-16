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
# ax.plot(arrx, arry, arrz[0]) 
# ax.plot(arrx+1, arry, arrz[1])
# ax.plot(arrx+2, arry, arrz[2]) 
# ax.plot(arrx+3, arry, arrz[3])
# ax.plot(arrx+4, arry, arrz[5])

for idx,arr in enumerate(arrz):
    ax.plot(arrx+idx    ,arry   ,arr)

plt.show()



