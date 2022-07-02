from sklearn.cluster import KMeans
import numpy as np

X = np.array(
    [[124, 191], [21, 85], [176, 9], [1, 168], [67, 27], [155, 192], [163, 18], [119, 90], [93, 102], [73, 61], [57, 1],
     [110, 1], [67, 126], [111, 173], [190, 151], [121, 20], [97, 2], [52, 77], [125, 10], [135, 45]])
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
