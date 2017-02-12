def myfunction1(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

def myfunction2(**myargs):
    print 'args type ',type(myargs)
    for k,v in myargs.iteritems():
        print k, ' - ',v

kwargs = {"arg3": 3, "arg2": {"name":"kumar", "location":"chennai"}}
kwargs1 = {"arg3": 3, "arg2": "Edureka"}
kwargs2 = {"arg1": 3, "arg3":"Another test","arg2": "Edureka"}
myfunction1(1, **kwargs)
print '========================'
myfunction1(1, **kwargs1)
print '========================'
myfunction1(**kwargs1)
print '========================'
myfunction1(**kwargs2)
print '========================'
myfunction2(**kwargs2)
