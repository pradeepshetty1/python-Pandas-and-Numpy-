import re

myPattern = re.compile('abb')

match = myPattern.search('abbreviated with abbreviations')

match1 = myPattern.findall('abbreviated with abbreviations')


print match.group()
print match1