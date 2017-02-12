import copy
class Edureka:
    def __init__(self,nameValue):
        name = nameValue
        print 'Class created with name',name

    def __myPrivate(self):
        print 'This is private method'

    def myPublic(self):
        print 'This is public method'

    def privateCallInternal(self):
        self.__myPrivate()

    def __del__(self):
        print 'Destructor getting called'
#myobject = Edureka()
myobject = Edureka('My First Class')

myobject2 = myobject

print 'Both object referring to same reference',myobject,myobject2

del myobject2
print 'myobject2 deleted'

del myobject

myNewObject = Edureka('My New Object')
myNewObject1 = copy.deepcopy(myNewObject)

print 'Both object referring to different reference',myNewObject,myNewObject1
del myNewObject
print 'myNewObject deleted'

del myNewObject1