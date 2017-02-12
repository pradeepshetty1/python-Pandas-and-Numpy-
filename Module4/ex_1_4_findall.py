import re

find = re.findall(r"[\w\.-]+@gmail[\w\.-]+", 'one@gmail.com, two@yahoo.com, three@hotmail.com, test@GMAIL.com')

for rec in find:
    print rec
