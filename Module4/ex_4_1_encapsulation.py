import copy
class Edureka:
    __accountMaster = 'Kamal'
    def __init__(self,nameValue):
        name = nameValue
        print 'Class created with name',name
        print 'Account Master'

    def getAccountMaster(self):
        return self.__accountMaster

    def setAccountMaster(self,masterValue):
        self.__accountMaster = masterValue


myobject = Edureka('My First Class')
print 'Account Master Value',myobject.getAccountMaster()

myobject.setAccountMaster('New Master')

print 'Account New Master Value',myobject.getAccountMaster()

print 'Back door entry',myobject._Edureka__accountMaster

