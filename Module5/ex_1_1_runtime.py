class Edureka():
    pass

def testruntime(a,b):
    print var
    return a/b

def handleRuntime(a,b):
    try:
        div = a/b
        return div
    except Exception as e:
        print e
        return None


def testkeyerror():
    myvar = {'a':1,'b':2}
    print myvar['a']
    print myvar['c']

def testattributeError():
    ob = Edureka()
    ob.attr

def testIndexError():
    myvar = [1,2,3]
    print myvar[4]

#testruntime('Edureka',2)
# testruntime(5,2)
#
# print handleRuntime('Edureeka',3)
# print handleRuntime(5,3)
#
# testkeyerror()
#
# testattributeError()

testIndexError()
