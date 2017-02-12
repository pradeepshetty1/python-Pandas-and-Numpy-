import numpy

list = [[1,2,3],[4,5,6],[7,8,9],[17,18,19]]

arr = numpy.array(list)

print arr
print 'arr[:,0]',arr[:,0]

arr[:,0] = [9,9,9,9]
print arr