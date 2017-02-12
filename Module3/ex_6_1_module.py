import os
print os.getcwd()

testPath = 'F:\squarks\Training\Edureka\python\practicals\project\Module3'
fp = open(os.path.join(testPath,'sample.txt'))
for line in fp:
    print line

fp.close()

print os.path.exists('F:\squarks\Training\Edureka\python\practicals\project\Module3')
print os.path.exists('F:\squarks\Training\Edureka\python\practicals\project\Module3_Test')

print os.path.abspath('../..')

print os.path.join('F:\squarks\Training\Edureka\python\practicals\project\Module3','sample.txt')

