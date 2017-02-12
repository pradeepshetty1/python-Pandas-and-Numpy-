myvar = 10

def localAndGlobalTest():
    global myvar
    myvar = 15
    localVar = 20

def anotherFunction():
    global myvar
    myvar = 100
    localVar = 20

def yetanotherFunction():
    myvar = 200
    localVar = 20


print 'Global var before calling function',myvar
localAndGlobalTest()
print 'Global var after calling function',myvar
anotherFunction()
print 'Global var altered in another function',myvar
yetanotherFunction()
print 'Not a Global var altered in yet another function',myvar