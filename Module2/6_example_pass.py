def predictCreditScore():
    pass

def retriveExistingScore():
    pass

def testPass():
    a = range(10)
    for elem in a:
        if elem%5 ==0:
            predictCreditScore()
        elif elem%3==0:
            retriveExistingScore()
        elif elem%4==0:
            pass
        else:
            print 'cannot find credit score',elem


testPass()



