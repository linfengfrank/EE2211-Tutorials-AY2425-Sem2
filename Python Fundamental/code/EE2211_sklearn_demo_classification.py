from sklearn.datasets import make_blobs
import numpy as np
import pandas as pd


# Generate a toy example using sklearn
X, y = make_blobs(n_samples=1000, centers=20, random_state=123)
labels = ["b", "r"]
y = np.take(labels, (y < 10))
# Print the data and label sizes
print(X.shape)
print(y)

Y = np.expand_dims(y, axis=-1)
# Concatenate the input data and label.
data = np.concatenate([X, Y], axis=-1)

# Convert it to pandas.Dataframe and save to local file.
data = pd.DataFrame(data, columns=['x', 'y', 'label'])
data.to_csv("data.csv")
# Print the first 10 samples
print(data.head(10))

import matplotlib.pyplot as plt
# Visualize the samples by its category.
plt.figure(figsize=(8, 8))
for label in labels:
    mask = (y == label)
    plt.scatter(X[mask, 0], X[mask, 1], c=label)

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()



from matplotlib import pyplot as plt
import numpy as np
# Function to plot the classification probability.

def plot_surface(clf, X, y,
                xlim=(-10, 10), ylim=(-10, 10), n_steps=250,
                subplot=None, show=True):

    if subplot is None:
        fig = plt.figure()
    else:
        plt.subplot(*subplot)
        xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], n_steps),
        np.linspace(ylim[0], ylim[1], n_steps))

    if hasattr(clf, "decision_function"):
        z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    
    z = z.reshape(xx.shape)
    plt.contourf(xx, yy, z, alpha=0.8, cmap=plt.cm.RdBu_r)
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.xlim(*xlim)
    plt.ylim(*ylim)

    if show:
        plt.show()

def plot_clf(clf, X, y):
    plt.figure(figsize=(16, 8))
    plot_surface(clf, X, y, subplot=(1, 2, 1), show=True)

from sklearn.neural_network import MLPClassifier

# Define a multi-layer perception to fit the data.
clf = MLPClassifier(hidden_layer_sizes=(100, 100, 100), activation="relu",learning_rate="invscaling")
clf.fit(X, y)
plot_clf(clf, X, y)