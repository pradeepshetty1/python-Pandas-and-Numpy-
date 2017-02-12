myTup = (20,10,60,40,80,100,50)

print 'Sorted : ',sorted(myTup)
print 'Descending Order : ',sorted(myTup,reverse=True)
print 'Original Tuple: ',myTup

myList = [20,10,60,40,80,100,50]

print 'Sorted : ',sorted(myList)
print 'Descending Order : ',sorted(myList,reverse=True)

myAnotherList = [20,10,60,40,80,100,50]
print 'Before calling sort method :',myAnotherList
myAnotherList.sort()
print 'After calling sort method :',myAnotherList
