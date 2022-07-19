
import matplotlib.pyplot as plt

import numpy as np
from day16.daostocksynksem import DaoStockSink

dss = DaoStockSink()




    
arrzs = dss.selects()    
    
mylen = len(arrzs[0])  
print("mylen",mylen)  

arrx = np.zeros(mylen)
arry = list(range(mylen))


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

for idx,arrz in enumerate(arrzs):
    ax.plot(arrx+idx,arry,arrz/arrz[0])


plt.show()