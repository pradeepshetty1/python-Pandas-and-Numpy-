s1 = set([1,2,3])
s2 = set([3,4,5])

s3 = set([1,2,3,5,6])

print 'Union of set :',s1|s2

print 'Intersection of set :',s1&s2

print 'Difference of set :',s1-s2

print 'Union of set :',s1.union(s2)

print 'Intersection of set :',s1.intersection(s2)

print 'Difference of set :',s1.difference(s2)

print 'S1 is superset of S3 :',s1.issuperset(s3)

print 'S1 is superset of S3 :',s1.issubset(s3)