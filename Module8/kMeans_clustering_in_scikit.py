import numpy as np
import sqlite3

# Matplotlib imports
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# scikit imports
from sklearn import datasets
from sklearn.cluster import KMeans

centers = [[1,1],[-1,-1],[1,-1]]
np.random.seed(5)

iris = datasets.load_iris()
X = iris.data
y = iris.target


estimators = {'k_means_iris_3': KMeans(n_clusters=3),
              'k_means_iris_8': KMeans(n_clusters=8),
              'k_means_iris_bad_init': KMeans(n_clusters=3, n_init=1, init='random')}

fignum = 1
for name, est in estimators.items():
    fig = plt.figure(str(fignum)+name, figsize=(4, 3))
    plt.clf() #Clears entire figure
    ax= Axes3D(fig, rect=[0, 0, 1, 1], elev=48) #, azim=134)
    plt.cla() # Clears an axiz

    est.fit(X)
    labels = est.labels_

    ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels.astype(np.float))
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Petal width')
    ax.set_ylabel('Sepal length')
    ax.set_zlabel('Petal length')
    fignum = fignum+ 1

fig = plt.figure(fignum, figsize=(8, 5))
#plt.clf()
#fig.show()
ax= Axes3D(fig, rect=[0, 0, 1, 1], elev=48, azim=134)
plt.cla()


for name, label in[('Setosa', 0),
                   ('Versicolour', 1),
                   ('Virginica', 2)]:
    ax.text3D(X[y == label, 3].mean(),
              X[y == label, 0].mean() + 1.5,
              X[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='b', facecolor='w'))

# reorder the labels to have colors match cluster results
# np.choose, constructs an array from indexed array (indexed arrays are similar to Series in pandas)
y = np.choose(y, [1,0,2]).astype(np.float)

#print X
#print X[:,3]

ax.scatter(X[:,3],X[:,0],X[:,2], c=y)
ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('Petal width')
ax.set_ylabel('Sepal length')
ax.set_zlabel('Petal length')
plt.show()