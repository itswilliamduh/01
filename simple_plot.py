import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


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
df['robot_y'] = [2,2,-2,-2]
df['pos_x'] = [-1.8,1.5,-1.8,1.7]
df['pos_y'] = [1.5,1.5,-1.6,-1.7]
df['force'] = [20,23,25,27]

# reshape to 2D array for the heatmap
force_level = np.reshape(list(df.force),(2,2))

# plotting the heatmap
sns.heatmap(force_level, annot=True, fmt=".0f", cmap='Greens_r', linewidths=0.5)

# plt.subplots_adjust(bottom=.180)
# Create another plot
fig, x = plt.subplots(1)

# plotting robot reference
x.plot(df.robot_x.astype(int), df.robot_y.astype(int), 'ro', markersize=10, mfc='none', label='robot_ref')

# plotting the actually position
x.plot(df.pos_x, df.pos_y, 'go' , markersize=10, label='Pos0')

# Turn the grid on
plt.grid(b=True, which='major', linestyle='-')

# Set the max limit
plt.ylim(-4,4)
plt.xlim(-4,4)

# Turn on legend
plt.legend()
# plot a table under current plot
plt.table(cellText=df.values, colLabels=df.columns, loc='bottom')
plt.tight_layout()  # auto fit
plt.show()


