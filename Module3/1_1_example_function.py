def add (mylist):
    mylist.append('third')

def addnew(mylist):
    mylist = ['first','second']
    mylist.append('third')

l1 = ['first','second']
print l1
print
add(l1)
print l1
print '==========================='

l2 = ['first','second']
print l2
print
addnew(l2)
print l2
print


