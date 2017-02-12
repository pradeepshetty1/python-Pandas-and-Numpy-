import re
file = open('customer.xml')

for i in file:
    data = re.search(r'<([a-z]+)>(.*)</\1>',i)
    print data.group(1)+" : "+data.group(2)

