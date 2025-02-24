import numpy as np 
from numpy.linalg import inv 
from sklearn.preprocessing import PolynomialFeatures 

X = np.array([[1,-1], [1,0], [1,0.5], [1,0.3], [1,0.8]]) 
Y = np.array([[1,0,0], [1,0,0], [0,1,0], [0,0,1], [0,1,0]]) 

## (a) Linear regression for classification 
W = inv(X.T @ X) @ X.T @ Y 
print(f"W=\n{W}\n") 

Xt = np.array([[1,-0.1], [1,0.4]]) 
y_predict = Xt @ W 
print(f"y_predict=\n{y_predict}\n") 

y_class_predict = [[1 if y == max(x) else 0 for y in x] for x in y_predict ] 
print(f"y_class_predict=\n{y_class_predict}\n") 

## (b) Polynomial regression for 
## Generate polynomial features 
order = 5 
poly = PolynomialFeatures(order) 

## only the data column (2nd) is needed for generation of polynomial terms 
reshaped = X[:,1].reshape(len(X[:,1]),1) 
P = poly.fit_transform(reshaped) 
reshaped = Xt[:,1].reshape(len(Xt[:,1]),1) 
Pt = poly.fit_transform(reshaped) 

## dual solution (without ridge) 
Wp_dual = P.T @ inv(P @ P.T) @ Y 
print(f"Wp_dual=\n{Wp_dual}\n") 

yp_predict = Pt @ Wp_dual 
print(f"yp_predict=\n{yp_predict}\n") 

yp_class_predict = [[1 if y == max(x) else 0 for y in x] for x in yp_predict ] 
print(f"yp_class_predict=\n{yp_class_predict}\n")