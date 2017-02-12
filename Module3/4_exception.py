try:
    import mylib
except ImportError as ie:
    print 'module not found: ',ie



def exception_example(a,b):
    c = 0
    try:
        c=a/b
        print 'result is ',c
    except Exception as exp:
        print 'encountered exception',exp

    return c

#exception_example(10,3)
#print 'printing while calling the function',exception_example(10,3)
exception_example(10,0)