import numpy
import math
from matplotlib import pyplot as plt

def sinc(x):
    if x == 0.0:
        return 1.0
    else:
        w = math.pi*x
        return math.sin(w)/w

x = numpy.r_[-5:5:100j]


vsinc = numpy.vectorize(sinc)

y = vsinc(x)

print x
print y

plt.plot(x,y)
plt.show()


#r_ means simple way to build array
#j is imaginary number - If step is an imaginary number (i.e. 100j) then its integer
# portion is interpreted as a number-of-points desired and the start and stop are inclusive.
# In other words, start:stop:stepj is interpreted as np.linspace(start, stop, step, endpoint=1)
# inside of the brackets. After expansion of slice notation, all comma separated sequences are
# concatenated together.

print numpy.r_[numpy.array([1,2,3]), 0, 0, numpy.array([4,5,6])]



