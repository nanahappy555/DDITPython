import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot([-5,-5,-5],[0,3,6],[0,10,0])
ax.plot([0,0,0],[0,3,6],[0,10,0])
ax.plot([5,5,5],[0,3,6],[0,10,0])

# ax.set_xlim3d(-5, 5)
# ax.set_ylim3d(-5, 5)
# ax.set_zlim3d(-5, 5)


plt.show()