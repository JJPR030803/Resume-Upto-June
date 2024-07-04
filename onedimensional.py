import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Generating a random one-dimensional dataset
np.random.seed(42)
X_1d = np.random.rand(100, 1)

# Applying K-means with 3 clusters
kmeans_1d = KMeans(n_clusters=3)
kmeans_1d.fit(X_1d)

# Scatter plot of the data points colored by cluster
plt.scatter(X_1d, np.zeros_like(X_1d), c=kmeans_1d.labels_, cmap='viridis', alpha=0.7)

# Marking cluster centroids
plt.scatter(kmeans_1d.cluster_centers_, np.zeros_like(kmeans_1d.cluster_centers_), marker='X', s=200, c='red')

plt.title('K-Means Clustering (1D)')
plt.xlabel('Feature 1D')
plt.yticks([])  # Removing y-axis for better visualization in 1D
plt.show()