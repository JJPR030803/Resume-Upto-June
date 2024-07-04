import csv
import random
import math
import matplotlib.pyplot as plt

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([float(val) for val in row])
    return data

def initialize_centroids(data, k):
    return random.sample(data, k)

def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

def assign_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster_index = distances.index(min(distances))
        clusters[cluster_index].append(point)
    return clusters

def update_centroids(clusters):
    return [[sum(dim) / len(dim) if dim else random.choice(cluster) for dim in zip(*cluster)] for cluster in clusters]

def kmeans(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if centroids == new_centroids:
            break
        centroids = new_centroids
    return centroids, clusters

def plot_clusters(centroids, clusters):
    plt.figure(figsize=(8, 6))
    
    for i, cluster in enumerate(clusters):
        cluster_points = list(zip(*cluster))
        plt.scatter(cluster_points[0], cluster_points[1], label=f'Cluster {i+1}', marker='o')
    
    centroids_points = list(zip(*centroids))
    plt.scatter(centroids_points[0], centroids_points[1], marker='x', s=200, c='red', label='Centroids')
    
    plt.title('K-means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

def main():
    file_path = 'new_dataset.csv'  # Replace with the path to your CSV file
    k = 9  # Number of clusters
    data = load_data(file_path)
    
    centroids, clusters = kmeans(data, k)
    
    print("Final centroids:")
    print(centroids)
    
    plot_clusters(centroids, clusters)

if __name__ == "__main__":
    main()