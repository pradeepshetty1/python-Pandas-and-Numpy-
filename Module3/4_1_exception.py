def exception_example(a,b):
    c = 0
    try:
        c=a/b
        #raise Exception
        print 'result is ',c
    except Exception as exp:
    #except EOFError as exp:
        print 'encountered exception',exp
    else:
        print 'Done with try'
    finally:
        print 'finally complete activity like releasing all valuable resources'

    return c

#exception_example(10,3)
exception_example(10,0)

