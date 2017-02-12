class Edureka:
    myDomain = 'Big Data Analytics'

    def setCourse(self,courseName):
        self.name = courseName

myObject1 = Edureka()
myObject2 = Edureka()

myObject1.setCourse('Mastering Python')
myObject2.setCourse('Spark and Scala')

print myObject1.myDomain
print myObject2.myDomain

myObject1.myDomain = 'Big Data Analytics with Data Science'
myObject2.myDomain = 'Big Data Analytics with Spark and Scala'

print myObject1.myDomain
print myObject2.myDomain
print Edureka.myDomain

print 'myObject1 dictionary',myObject1.__dict__
print 'myObject2 dictionary',myObject1.__dict__
print 'Edureka Class dictionary',Edureka.__dict__
