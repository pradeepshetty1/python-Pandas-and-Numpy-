alist = ['a1', 'a2', 'a3']

for value in enumerate(alist):
    print value

print "==================================="

for i, a in enumerate(alist):
    print i, a



mylist = ["a","b","c","d"]

print 'mylist : ',list(enumerate(mylist))

print 'Use of enumerate to merge two list horizontally'
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print i, a, b
    
for i, x in enumerate(zip(alist, blist)):
    print i, x    