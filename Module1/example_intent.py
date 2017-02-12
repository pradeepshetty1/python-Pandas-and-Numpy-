def funs():
    a = 5
    b = 6

    if a == b:
        print "we are equal"

    else:
        print "we are not equal"


def funs_with_return():
    a = 5
    b = 6

    if a == b:
        print "we are equal"
    else:
        print "we are not equal"

    return "I have return value too"

def funs_with_intent():
    a = 5
    b = 6


    if a == b:
        print "we are equal"
    else:
        print "we are not equal"

        for ii in range(10):
            print 'counting %d' % ii

    return "I have return value too"


def more_funs_with_intent():
    a = 5
    b = 6


    if a == b:
        print "we are equal"
    else:
        print "we are not equal"

        for ii in range(10):
            if (ii == a or ii == b):
                print 'got Value of a or b as %d' % ii

#print("Uncommenting this will give more insight")
#funs()
#print funs_with_return()
#print funs_with_intent()
print more_funs_with_intent()


