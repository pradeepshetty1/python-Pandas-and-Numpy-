from operator import itemgetter

print 'Item getter output', itemgetter(2)(range(1,10))

edureka_course = {'Hadoop':40,'DataScience':30,'Cloud Computing':30,'Python':45,'Spark':20,'Spring':10}

print 'Sorted with key as 0',sorted(edureka_course,key=itemgetter(0))

print 'Sorted with key as 1 with full items',sorted(edureka_course.items(),key=itemgetter(1))

print 'Sorted with key as 0 with full items',sorted(edureka_course.items(),key=itemgetter(0))

print 'Sorted - multi level',sorted(edureka_course.items(),key=itemgetter(0,1))
print 'Sorted - multi level',sorted(edureka_course.items(),key=itemgetter(1,0))




