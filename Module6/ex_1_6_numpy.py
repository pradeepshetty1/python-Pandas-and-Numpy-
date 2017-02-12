import numpy

arr1 = numpy.array([1,5,9,2])
arr2 = arr1

print arr2

arr1[2]=100
print arr1
print arr2

print '###################################'
arr3 = arr1.view()

print arr1
print arr3

arr1[1]=200

print arr1
print arr3

print arr3.base is arr1

print '###############################'

arr4 = numpy.array([1,5,9,2])
arr5 = arr4.copy()
print arr4
print arr5

arr4[2]=100

print arr4
print arr5

print arr5.base is arr4

print '####################################'

arr11=numpy.array([10,12,14,16])
arr22=numpy.array([5,6,7,8])

print arr11/arr22

print arr22/arr11

print '######################################'

arr33 = numpy.arange(20)
arr44 = arr33 * 2
arrindices = [1,5,6,9]

print arr33[arrindices]
print arr44[arrindices]


