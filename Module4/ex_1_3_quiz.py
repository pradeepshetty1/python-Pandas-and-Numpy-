import re
m = re.match(r"(..)+","edureka")

print m.group(0)
print m.group(1)

print '------------------------'
m = re.match(r"((..)+)","edureka")

print m.group(0)
print m.group(1)
print m.group(2)

print '==================BREAK============'

myString = 'start123456789end'

myPattern = re.compile('start([0-9]*)(end)')

myGroup = myPattern.match(myString)

print myGroup.group()
print myGroup.group(0)
print myGroup.group(1)
print myGroup.group(2)
