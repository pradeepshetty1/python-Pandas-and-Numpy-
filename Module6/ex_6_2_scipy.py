from scipy import constants
import math
from scipy import integrate


print constants.physical_constants['electron mass']

print integrate.quad(lambda x:math.cos(math.exp(x)),2,3)

