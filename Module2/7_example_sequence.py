
l1 = list(range(10))
l2 = list('Edureka')
l3 = [1,2,3,4]

print(l1)
print(l2)
print(l3)

print(l1[3])
print(l2[3])
print(l3[3])

print "=========BREAK1============="

print (l2[-1])
print (l2[-2])
print(l2[2:4])
print(l2[1:-1])
print(l2[1:-1:2])
print "============BREAK2=========="

#print(l2[10])

print(l2[::-1])

print "============BREAK3=========="


#testString = 'malayalam'
testString = 'Test'

if testString == testString[::-1]:
    print "We got a palindrome"
else:
    print "It is not a palindrome"

print "======================"

testDel = list(range(10))

del testDel[0:3]

print (testDel)

print "======================"



