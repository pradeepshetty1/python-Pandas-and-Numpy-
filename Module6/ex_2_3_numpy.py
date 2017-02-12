import numpy

arr = numpy.array([10,20,5.5,9.2,5.3,7])

print 'arr :',arr

arr.sort

print 'arr :',arr

arr2 = numpy.array([10,20,5.5,9.2,5.3,7])
print 'another sort :',numpy.sort(arr2)

print 'arr2 :',arr2

print 'arg sort :',arr.argsort()

print 'arr[arr.argsort()] :',arr[arr.argsort()]