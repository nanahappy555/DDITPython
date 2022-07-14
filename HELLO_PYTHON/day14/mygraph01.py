import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

xList = [0,0,0]
yList = [0,3,6]
zList = [0,10,0]

# ax.plot([0,0,0],[0,3,6],[0,10,0])
ax.plot(xList,yList,zList)

# ax.set_xlim3d(-5, 5)
# ax.set_ylim3d(-5, 5)
# ax.set_zlim3d(-5, 5)


plt.show()