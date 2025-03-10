# Tutorial 7, Q1
# Explore the use of Pearson’s correlation as a feature selection metric

import numpy as np

data = np.array([[0.3510,   2.1812,     0.2415,     -0.1096,    0.1544],
                 [1.1796,   2.1068,     1.7753,     1.2747,     2.0851],
                 [-0.9852,  1.3766,     -1.3244,    -0.6316,    -0.8320]])

target = np.array([0.2758, 1.4392, -0.4611, 0.6154, 1.0006])

from scipy.stats import pearsonr
for i in range(len(data)):
    r, _ = pearsonr(data[i], target)
    
    print("Pearson\'s r of Feature", i+1, "and y=", r)