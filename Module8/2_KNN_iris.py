from sklearn import datasets

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

mydataset = datasets.load_iris()

print mydataset

model = KNeighborsClassifier()

model.fit(mydataset.data, mydataset.target)

print model.predict([5.5,3.1,5.5,0.9])
print model.predict([5.5,3.1,2.5,0.9])