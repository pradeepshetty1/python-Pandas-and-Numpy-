import re

print re.search('py','Mastering Python')

myresult = re.search('Py','Mastering Python')

print myresult

print myresult.group()
print myresult.start()
print myresult.end()
print myresult.span()

print '=================BREAK====================='

myresult1 = re.search('py','Mastering Python. Python is great language. Python!!',re.IGNORECASE)
print myresult1.group()

myresult11 = re.search('(py)+','Mastering Python. Python is great language. Python!!',re.IGNORECASE)
print myresult11.group()


myrecompile = re.compile('(Py)+')

myFindAll = myrecompile.findall('Mastering Python. Python is great language. Python!!')

print myFindAll

print '=================BREAK====================='




