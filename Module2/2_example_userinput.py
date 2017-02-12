def test_raw_input():
    myraw_input = raw_input("Enter your name")
    print("Your name is {}").format(myraw_input)
    print("Type of user input is {}".format(type(myraw_input)))

    #Edureka
    #5

def test_input():
    my_input = input("Enter different type of data?")
    print "User entered {}".format(my_input)
    print "User type input {}".format(type(my_input))

    #5
    #"Edureka"
    #(1,2,3)
    #[1,2,3]

if __name__ =="__main__":
    test_raw_input()
    #test_input()