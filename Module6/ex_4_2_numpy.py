import numpy

mat = numpy.mat([[1,9],[2,8]])

print mat

arr = numpy.array([[1,9],[2,8]])
mat1 = numpy.mat(arr)
print arr
print mat1
arr[1,0] =100

print arr
print mat1


print '############################'

arr22 = numpy.array([[1,9],[2,8]])
mat22 = numpy.asmatrix(arr22)
print arr22
print mat22
arr22[1,0] =100

print arr22
print mat22


