import numpy

list = [[1,2,3],[4,5,6],[7,8,9],[17,18,19]]

arr = numpy.array(list)

print arr

divarr = arr % 2 ==0

print divarr

print arr[divarr]

print '========================='

print 'sum ', arr.sum()
print 'mean ', arr.mean()
print 'std ', arr.std()
print 'max ', arr.max()
print 'max ', arr.min()
