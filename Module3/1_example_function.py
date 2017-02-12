def f1():
    print 'inside f1'
    pass

def f2(a):
    print 'inside f2'
    return a**2

def f3(b=[]):
    print 'inside f3'
    return ' '.join(b)

f1()
print f2(6)
print f3()
print f3(['join','test'])