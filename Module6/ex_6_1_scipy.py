import scipy as sp
from scipy import stats

s = sp.randn(100)
print s

print s.mean()
print s.min()
print s.max()
print s.var()
print s.std()

print stats.describe(s)

n,min_max,mean, var, skew,kurt = stats.describe(s)

print n
print min_max
print min_max[0]
print mean

