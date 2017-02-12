# da = dict()
#
# print "Fresh Dictionary",da
#
# da['key1']='myvalue1'
#
# print "One element Added",da
#
# da['name']='kumar'
#
# print "Another element Added",da
#
# da['address'] = {'door':23,'city':'chennai','contactPriority':{1:'support',2:'Email',3:'Phone'}}
#
# print "Complex element Added",da
#
# print "keys in dictionary", da.keys()
#
# print "values in dictionary", da.values()
#
# print "Internal element",da['address']
#
# print "Super Internal element",da['address']['city']
#
# print "Internal element values",da['address'].values()
#
# print "Internal element values with index",da['address'].values()[1]
#
# print "Internal element values with index",da['address'].values()[1].values()[2]
#
# #Find the difference between above and below statement
# print "Internal element values with index",da['address'].values()[1][2]
#
# print "try to get a key which doesnt exists",da.get('org','None')
#
# print'============================='

anotherTest = {'a':1,'b':'kumar','c':3,'r':4,5:6}

print 'Check a 4 exists in the Dictionary',4 in anotherTest

print 'Check a 5 exists in the Dictionary',5 in anotherTest

print 'Check a 4 exists in the Dictionary values',4 in anotherTest.values()

del anotherTest['r']

print 'Dictionary after a pair is deleted',anotherTest

anotherTest.pop('c')

print 'Dictionary after a pair is deleted',anotherTest

print "================================"

iterTest = {'a':1,'b':'kumar','c':3,'r':4,5:6}

for k,v in iterTest.iteritems():
    print k, 'is mapped to',v

print "================================"

iterTest.update({'a':'name'})

print 'after update : ',iterTest

iterTest.update({'z':'Edureka',6:7})

print 'after another update : ',iterTest




