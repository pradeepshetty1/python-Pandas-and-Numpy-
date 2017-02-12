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
        self.__private = 'I am private'
        self._protected = 'I am protected'
        self.public = 'I am public'

    def addAttr(self):
        self.participants = 30
        self.end_date = '03rd July 2016'

    def getPrivate(self):
        return self.__private

    def changePrivate(self,new_value):
        self.__private = new_value


if __name__ == "__main__":
    print 'Will instantiate Edureka Class'
    myObject = Edureka()

    print 'myObject dictionary',myObject.__dict__
    print
    #print 'get private directly ',myObject.__private
    print 'get Original private attribute throuth accessor',myObject.getPrivate()
    myObject.changePrivate('Private value changed')
    print 'private changed : ',myObject.getPrivate()






