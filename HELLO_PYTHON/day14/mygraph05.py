import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock

ds = DaoStock()
import numpy as np

arrx = np.zeros(16)

arry = list(range(16))

arr_name = ["삼성전자", "LG", "SK"]

arrz = []
arrz.append(ds.selects(arr_name[0]))
arrz.append(ds.selects(arr_name[1]))
arrz.append(ds.selects(arr_name[2]))


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot(arrx, arry, arrz[0]) # 삼전 -1 x좌표
ax.plot(arrx+1, arry, arrz[1]) # LG 0
ax.plot(arrx+2, arry, arrz[2]) # SK 1

plt.show()



