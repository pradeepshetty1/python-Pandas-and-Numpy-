import numpy

list = [[1,2,3],[4,5,6],[7,8,9],[17,18,19]]
list1 = [[[1,2,3],[4,5,6],[7,8,9],[17,18,19]],[[1,2,3],[4,5,6],[7,8,9],[17,18,19]]]

arr = numpy.array(list)
arr1 = numpy.array(list1)

print arr
print
print arr1

print arr.shape

print arr.size

print arr.dtype

print arr.ndim
print 'arr1 dim',arr1.ndim

print arr.data

print numpy.random.rand(3,2,4)