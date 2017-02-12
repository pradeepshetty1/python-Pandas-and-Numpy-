import numpy as np

a=np.mat('4 3; 2 1')
b=np.mat('1 2; 3 4')
print(a)
# [[4 3]
#  [2 1]]
print(b)
# [[1 2]
#  [3 4]]
print(a*b)
# [[13 20]
#  [ 5  8]]

c=np.array([[4, 3], [2, 1]])
d=np.array([[1, 2], [3, 4]])
print(c*d)
# [[4 6]
#  [6 4]]

print(np.dot(c,d))
# [[13 20]
#  [ 5  8]]