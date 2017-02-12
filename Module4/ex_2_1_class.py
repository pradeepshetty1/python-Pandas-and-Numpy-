class Edureka():
    course = "Mastering Python"
    startDate = "04th June 2016"

    def __str__(self):
        pass

    def printCourseDetails(self):
        return "I will provide course details."


if __name__ == "__main__":
    myObject = Edureka()
    print myObject.printCourseDetails()
    print 'Before update',myObject.startDate
    myObject.startDate = "Yet to Decide"
    print 'After Update',myObject.startDate

    myObject1 = Edureka()
    print myObject1.printCourseDetails()
    print 'start date of myobject1',myObject1.startDate


    print dir(Edureka) #List all its namespace
    print dir(myObject)
    print '__main__',Edureka.__name__
    print '__doc__',Edureka.__doc__
    print '__dict__',Edureka.__dict__
    print '__module__',Edureka.__module__
