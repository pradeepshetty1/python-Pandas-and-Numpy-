multiply = lambda x,y:(x*y)**2
print 'My lambda output',multiply(3,4)

print '===================================='

joinlist = lambda *x: ' -- '.join(x)

print 'Joined list',joinlist('Edureka','Python','Course')

print '===================================='

addAll = lambda *x:sum(x)
print 'Add All output',addAll(1,2,3,4)

print '===================================='

anotherTry = lambda *x : (sum(x),max(x))


print 'Way to get multiple value',anotherTry(1,2,3,4)


