import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

# Generating a random dataset with three features
np.random.seed(42)
X_3d = np.random.rand(100, 3)

# Applying K-means with 3 clusters
kmeans_3d = KMeans(n_clusters=3)
kmeans_3d.fit(X_3d)

# Creating a 3D scatter plot of the data points colored by cluster
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_3d[:, 0], X_3d[:, 1], X_3d[:, 2], c=kmeans_3d.labels_, cmap='viridis')

# Marking cluster centroids in the 3D space
ax.scatter(kmeans_3d.cluster_centers_[:, 0], kmeans_3d.cluster_centers_[:, 1],
           kmeans_3d.cluster_centers_[:, 2], marker='X', s=200, c='red')

ax.set_title('K-Means Clustering (3D)')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
plt.show()