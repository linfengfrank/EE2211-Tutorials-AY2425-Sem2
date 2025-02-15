import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.linalg import inv

# read data
df = pd.read_csv("government-expenditure-on-education.csv")

# convert the data to matrices: X and y
expenditureList = df ['recurrent_expenditure_total'].tolist()
yearList = df ['year'].tolist()
m_list = [[1]*len(yearList), yearList]
X = np.array(m_list).T
y = np.array(expenditureList)

# Linear regression
w = inv(X.T @ X) @ X.T @ y
print(f"w=\n{w}\n")

# plot the results
y_line = X.dot(w)
plt.plot(yearList, expenditureList, 'o', label = 'Expenditure over the years')
plt.plot(yearList, y_line)
plt.xlabel('Year')
plt.ylabel('Expenditure')
plt.title('Education Expenditure')
plt.show()

# prediction
y_predict = np.array([1, 2021]).dot(w)
print(f"y_predict=\n{y_predict}\n")