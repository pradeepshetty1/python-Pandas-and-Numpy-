def myfunction(*args1):
    print 'args ', args1
    print 'args length',len(args1)
    print 'args formatted'
    print ' - '.join(str(arg) for arg in args1)


def myfunction1(fargs,*vargs):
    print "formal arg:", fargs
    for arg in vargs:
        print "another arg:", arg

#Using special sytnax in calling function

def myfunction2(arg1, arg2, arg3):
    print "arg1:", arg1,
    print "arg2:", arg2,
    print "arg3:", arg3



myfunction(1,2,3,4)
print '==============================='
myfunction([1,2,3])
print '==============================='
myfunction((1,2,3,4,5))
print '==============================='
myfunction(100,(1,2,3,4,5))
print '==============================='
myfunction1(100,(1,2,3,4,5))
myfunction1(100,1,2,3,4,5)
print '==============================='
myVariableInput= ("two", 3)
myVariableInput1 = ("two", 3,4)
myVariableInput2 = ["two", 3,4]
myfunction2(1, *myVariableInput)
print '==============================='
myfunction2(*myVariableInput1)
print '==============================='
myfunction2(*myVariableInput2)
