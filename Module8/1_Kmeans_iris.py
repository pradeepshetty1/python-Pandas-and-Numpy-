from sklearn import datasets

from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans

mydataset = datasets.load_iris()

print 'Data : ',mydataset.data
print 'Target : ',mydataset.target


print mydataset

model = DecisionTreeClassifier()
#model = KMeans(n_clusters=3)
#model = KMeans(n_clusters=8)

model.fit(mydataset.data, mydataset.target)


print model.predict([5.5,3.1,5.5,0.9])
print model.predict([5.5,3.1,2.5,0.9])