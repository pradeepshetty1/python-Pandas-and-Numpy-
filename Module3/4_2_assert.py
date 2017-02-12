def myinput1(a,b):
    assert a==b, 'input are not same'

def myinput2(a,b):
    try:
        assert a==b, 'inputs are not same'
    except AssertionError as ae:
        print "Error :",ae

myinput1(2,3)
#myinput2(2,3)
