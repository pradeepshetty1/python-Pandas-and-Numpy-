import re

f = open('file_1_5_sample.txt')
gmails = re.findall(r'[\w\.-]+@gmail[\w\.-]+',f.read())

for email in gmails:
    print email