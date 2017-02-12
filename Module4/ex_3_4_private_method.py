class Edureka:
    def __myPrivate(self):
        print 'This is private method'

    def myPublic(self):
        print 'This is public method'

    def privateCallInternal(self):
        self.__myPrivate()

myobject = Edureka()

myobject.myPublic()
#myobject.__myPrivate()
myobject.privateCallInternal()

#This is round about way. Avoid this as per recommendation.
myobject._Edureka__myPrivate()
