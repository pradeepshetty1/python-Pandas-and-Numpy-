class Edureka:
    count = 0
    @staticmethod
    def myCounter():
        Edureka.count = Edureka.count+1

print 'Class Variable count',Edureka.count
Edureka.myCounter()
myObject = Edureka()
print 'static class from instance',myObject.count
print 'Class Variable count',Edureka.count
Edureka.myCounter()
myObject1 = Edureka()
print 'static class from instance',myObject1.count
print 'Class Variable count',Edureka.count


