import datetime

print 'Current time',datetime.datetime.utcnow()

print 'Date sample',datetime.datetime(1978,7,20,22,56)


print 'difference is ',(datetime.datetime.utcnow() - datetime.datetime(1978,7,20,22,56))

mylist = []
today = datetime.date.today()
mylist.append(today)
print 'mylist',mylist
mylist.append(today)
print 'mylist',mylist