import random
import string

print 'Random range within 100',random.randrange(100)

print 'Random range with step',random.randrange(10,100,5)

print 'Random between',random.randrange(100,200)

myList = ['prg1','prg2','prg3','prg4','prg5']

print 'Choose a program',random.choice(myList)



print 'Get a password',"".join(random.choice(string.ascii_uppercase+string.digits) for _ in range(15))
print 'Get a password',"".join(random.choice(string.ascii_uppercase+string.digits+string.punctuation) for _ in range(15))