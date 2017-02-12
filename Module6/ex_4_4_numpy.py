import numpy

arr = numpy.array([[1,4],[6,4]])

mat = numpy.mat(arr)

print arr
print mat

print arr ** 4
print mat ** 4
print '##################################'
mattranspose = mat.T
matinverse = mat.I

print mattranspose
print matinverse
print '##################################'
print mat*matinverse


