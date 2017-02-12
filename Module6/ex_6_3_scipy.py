from scipy import linalg
import numpy as np

#solve the below equation
# 3x +2y +0z = 2
# x -y+0z = 4
# 0z +5y +z = -1


a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])

b = np.array([2, 4, -1])
x = linalg.solve(a, b)
print x
print np.dot(a, x) == b

finddet = np.mat('[1 3 5;2 5 1;2 3 8')
print linalg.det(finddet)