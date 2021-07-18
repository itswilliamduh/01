import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Imported math
import math 


"""

| Robot_X | Robot_Y | Pos_X | Pos_Y | Force |
|---------+---------+-------+-------+-------|
|  -2.0   |  +2.0   | -1.8  | +1.5  |  20   |
|  +2.0   |  +2.0   | +1.5  | +1.5  |  23   |
|  -2.0   |  -2.0   | -1.8  | -1.6  |  25   |
|  +2.0   |  -2.0   | +1.7  | -1.7  |  27   |

"""
# Data table
df = pd.DataFrame({'robot_x': [-2,2,-2,2]})
xpoint1 = df['robot_x']
df['robot_y'] = ypoint1 = [2,2,-2,-2]
df['pos_x'] = xpoint2  = [-1.8,1.5,-1.8,1.7]
df['pos_y'] = ypoint2 = [1.5,1.5,-1.6,-1.7]
df['force'] = [20,23,25,27]


# Distance Formula 

distance_final = []
def distanceformula(x1, y1, x2, y2):
    distancenum = []
    for i in range(len(x1)):
        distancenum.append(math.sqrt( ((x1[i]-x2[i])**2) + ((y1[i]-y2[i])**2)) )
    return distancenum
    
distance_final.append(distanceformula(xpoint1, ypoint1, xpoint2, ypoint2))


# reshape to 2D array for the heatmap
force_level = np.reshape(list(df.force),(2,2))

# distance heatmap 
distance_map = np.reshape(distance_final,(2,2))
fig, ax = plt.subplots(2, 1)
sns.heatmap(distance_map, annot=True, fmt=".0f", cmap='mako', vmax=1.5, vmin=0, linewidths=0.5, ax=ax[1])

# plotting the heatmap
sns.heatmap(force_level, annot=True, fmt=".0f", cmap='Greens_r', linewidths=0.5, ax=ax[0])


# plt.subplots_adjust(bottom=.180)
# Create another plot
fig, x = plt.subplots(1)

# plotting robot reference
x.plot(df.robot_x.astype(int), df.robot_y.astype(int), 'ro', markersize=10, mfc='none', label='robot_ref')

# plotting the actually position
x.plot(df.pos_x, df.pos_y, 'go' , markersize=10, label='Pos0')

# Turn the grid on
plt.grid(b=True, which='major', linestyle='-')

# Naming heatmaps
ax[1].set_title('distance between points')
ax[0].set_title('original points')

# Set the max limit
plt.ylim(-4,4)
plt.xlim(-4,4)

# Turn on legend
plt.legend()
# plot a table under current plot
plt.table(cellText=df.values, colLabels=df.columns, loc='bottom')
plt.tight_layout()  # auto fit
plt.show()


