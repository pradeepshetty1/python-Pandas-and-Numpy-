myTuple = ('BigData', 'Hadooop', 'DataScience', 1)

print "Number of elements in Tuple {}".format(len(myTuple))

print "First element of tuple is {}".format(myTuple[0])

print "Last element of tuple is {}".format(myTuple[-1])

print "Type of element of tuple is {}".format(type(myTuple[0]))

print "Type of element of tuple is {}".format(type(myTuple[-1]))

print "Tuple in revers order is {}".format(myTuple[::-1])

print "Does BigData exists in Tuple? {}".format('BigData' in myTuple)

print "Location of DataScience in Tuple {}".format(myTuple.index('DataScience'))

print "Sorted Tuple", sorted(myTuple)

print "Max Tuple", max(myTuple)

print "Min Tuple", min(myTuple)

print "=============================="

tua = (1,2)
tub = (2,1)
tuc = (1,0,2)

tud = (1,2)
print "compare 1 :", cmp(tua,tud)
print "compare 2 :", cmp(tua,tub)
print "compare 3 :", cmp(tua,tuc)
print "compare 4 :", cmp(tub,tua)

print 'tuple from range:',tuple(range(10))





