def add(list1, newlist2):
    print 'inside add function'
    list1.append('new-value')
    newlist2 = list1
    print list1
    print
    print newlist2
    print
    print 'returing from add function'

list1 = ['edureka']
list2 = ['python']
add(list1, list2)
print
print list1
print
print list2