ss ="Welcome to Edureka"

def test1():
    a = 'a'
    b = 'string'
    if(type(a)==type(b)):
        print("We are same family")
    else:
        print("We are not same family")


def immutable_test():
    name = "Charles"
    name2 = name
    name += " Saab"
    print("name2 :"+name2)
    print("name :"+name)

    names = ["Charles"]
    names2 = names
    names += ["Saab"]
    names2

    print("printing Names")
    print(names)
    print("=============================")
    print("Printing Names2")
    print(names2)
    print("=============================")

def repet_and_concatenate():
    a = "Welcome"
    b = "To"
    c = "Edureka"
    print("=============================")
    print("String Concatenation")
    print(a+b+c)
    print("=============================")
    print("String Repeat")
    print(((a+b+c)+"    ") * 3)

def test_string_index():
    s = "Edureka"
    print("Printing strart string : "+s[0])
    print("Printing end string : "+s[6])
    print("Printing string length: "+str(len(s)))
    print("Printing string with only end position (end is not inclusive)  : "+s[:4])
    print("Printing string with only start position (start is inclusive)  : "+s[2:])
    print("Printing string with Negative end  : "+s[:-2])
    print("Printing string with Negative end  : "+s[-2:])
    print("Printing every 2nd letter :" + s[::2])

def test_in_string():
    s = "Edureka"
    print("Test for E in Edureka:" + str('E' in s))
    print("Test for Z in Edureka:" + str('Z' in s))
    print("Test for e in Edureka:" + str('e' in s))
    print("Test for K in Edureka (Case insensitive):" + str('K'.upper() in s.upper()))
    print "Test for Z in Edureka:" , ('Z' in s)

def test_string_format():
    print('I am in %s course' % 'Mastering Python')
    print('I am in %s course' % 3)
    #print('I am in %drd course' % '3')
    print('I am in %s course. This is my %dth course' % ('Mastering Python', 4 ))
    print('I am in {} course. This is my {}th course'.format('Mastering Python', 4 ))
    print('I am in {1} course. This is my {0}th course'.format(4,'Mastering Python' ))

    print('This is octal %o' % 0XAA2345)
    print('This is octal %o' % 1234555)

    print('This is exponent notation %e' % 1234555)

    print('This is binary form {:b}'.format(10))
    print('This is octal form {:o}'.format(10))
    print('This is decimal form {:d}'.format(10))
    print('This is decimal form {:0.3f}'.format(10))

    print('This is hexa deciamal %x' % 0XAA2345)
    print('This is hexa deciamal %X' % 0XAA2345)
    print('This is hexa deciamal %X' % 1234555)
    print('This is hexa deciamal %x' % 1234555)
    print('Float decimal to 2 digits %.2f' % 0.916234555)


def test_string_methods():
    global s
    global y 
    s = "mastering Python course with Edureka"

    print("Actual Str :"+s)
    print("capitalize :"+s.capitalize())
    print("upper :"+s.upper())

    print("String \"ur\" occured {} times".format(s.count('ur')))
    encoded = s.encode('base64','strict')
    print("String base64 encode :"+encoded )
    decoded = encoded.decode('base64','strict')
    print("Decoded String :"+decoded)

    print("Index of E is {} ".format(s.index("E")))
    print("Index of Ed is {} ".format(s.index("Ed")))
    #print("Index of Edd is {}: ".format(s.index("Edd")))
    print("Max of String {} ".format(max(s)))
    print("Min of String {} ".format(min(s)))
    y = 'Thisismy4thcoursewithEdureka'
    print("Min of String {} ".format(min(y)))
    print("String Replaced :"+s.replace('ur',''))
    print("String Replaced :"+s.replace('ur','',1))

#test1()
#immutable_test()
#repet_and_concatenate()
#test_string_index()
#test_in_string()
#test_string_format()
test_string_methods()


