import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Generating a random dataset with two features
np.random.seed(42)
X = np.random.rand(100, 2)

# Applying K-means with 3 clusters
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Scatter plot of the data points colored by cluster
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')

# Marking cluster centroids
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='X', s=200, c='red')

plt.title('K-Means Clustering (2D)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()