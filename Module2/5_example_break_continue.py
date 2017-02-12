def test_break():
    for y in range(10):
        if y == 3:
            break
        print y

def test_continue():
    for y in range(10):
        if y == 3:
            continue
        print y

def test_with_else():
    for y in range(10):
        if y == 3:
            #continue
            break
        print y
    else:
        print "I am in else block of for loop"




#test_break()
#test_continue()
test_with_else()
