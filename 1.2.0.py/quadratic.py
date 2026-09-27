import stdio
import sys

# program 1.2.4

# quadratic formoola
# quadratic.py

import math

b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))

discriminant = b*b - 4.0*c
d = math.sqrt(discriminant)
stdio.writeln((-b + d) / 2.0)
stdio.writeln((-b - d) / 2.0)