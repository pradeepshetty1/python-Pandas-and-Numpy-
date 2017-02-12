import re

myString = 'one@gmail.com, two@yahoo.com, three@hotmail.com'

myResultString = re.sub('gmail','inbox',myString)

print myString
print myResultString

