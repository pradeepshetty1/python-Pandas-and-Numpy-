import numpy

arr = numpy.array([10,30,5.5,9.2,5.3,-7])
arr2 = numpy.array([2,2,2,2,2,2])
arr3 = numpy.array([2,2,2,2,2,2,2])
print arr
print arr.sum()
print numpy.sum(arr)

print '##############################'

print numpy.add(arr,arr2)

#addition should be on same shapes
#print numpy.add(arr,arr3)

print numpy.absolute(arr)
absarr = numpy.absolute(arr)

print numpy.log10(absarr)


