from sklearn.cluster import KMeans
import numpy as np

# input data
x = np.array([[1,1], [0,1], [0,0]])

init_centroids = np.array([[1,1], [0,1]])
kmeans = KMeans(n_clusters=2, init=init_centroids, random_state=0, n_init=1)
kmeans.fit(x)

print(f"prediction: \n {kmeans.labels_} \n")
print(f"centers: \n {kmeans.cluster_centers_} \n")