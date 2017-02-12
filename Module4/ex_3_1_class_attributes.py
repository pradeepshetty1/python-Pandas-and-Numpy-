from datetime import datetime as dt

class Master1(object):
    pass

class Master2(object):
    pass

class Edureka(Master1,Master2):
    COURSE = "Mastering Python"
    START_DATE = "04th June 2016"

    def __init__(self):
        print 'Inside constructor'
        self.currentTime = dt.now()

    def addAttr(self):
        self.participants = 30
        self.end_date = '03rd July 2016'

if __name__ == "__main__":
    print 'Will instantiate Edureka Class'
    myObject = Edureka()
    myObject1 = Edureka()

    print 'object dictionary',myObject.__dict__
    print 'object dictionary1',myObject1.__dict__
    print 'now object',myObject.currentTime

    myObject.addAttr()
    print 'object dictionary after addAttr',myObject.__dict__
    print 'object1 without adding attribute',myObject1.__dict__

    print 'Class info',Edureka.__dict__





