import numpy

arr = numpy.zeros(5)
print arr

arr1 = numpy.zeros((4,5))

print arr1

print arr1.dtype

arr2 = numpy.zeros((4,5),dtype=numpy.int)

print arr2

print '#############################'

arr3 = numpy.ones((3,4))
print arr3

#arange supports one dimension only.

arr4 = numpy.arange(10)
print arr4

arr5 = arr4*3
print arr5

arr6 = arr4 * 3.0

print arr6

arr7 = numpy.arange(15,dtype=numpy.float)
print arr7


arr8 = numpy.arange(0,14,2)
print arr8



