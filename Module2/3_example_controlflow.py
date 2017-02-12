def flow(a):
    if isinstance(a,str):
        print "a is string", a
    elif isinstance(a,int):
        print "a is numeric", a
    else:
        print "Dont know the type of a"

def testWhile():
    n = 3
    while n > 0:
        if n > 1:
            print n
        n = n - 1

def testFor():
    for x in range(5):
        if x == 3:
            continue
        print x

def testIfElse():
    for x in range(5):
        if x == 3:
            continue
        else:
            print "Done iterating over ",x

def testForElse():
    for x in range(5):
        if x == 3:
            continue
    else:
        print "Done iterating over ",x

def testWhileElse():
    n = 5
    while n !=0:
        while n%2 ==0:
            print n ,
            print 'is an even number'
            n = n -1
        else:
            print '-----------'
        n = n-1



if __name__ == "__main__":
    #flow("Edureka")
    #flow(4)
    #flow([])
    #testWhile()
    #testFor()
    #testIfElse()
    testForElse()
    #testWhileElse()
