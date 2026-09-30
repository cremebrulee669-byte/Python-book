# Intro program
#a = 1234
#b = 99
#c = a + b

# a literal is a Python-code representation of a data-type value.
# adding a decimal point makes the value type float.

#An operator in python is + - / *
# addition, subtraction, division, multiplication

# An identifier is a python-code representation of a variable name.

# A variable is a Python-code representation of a storage location for a value.

# A constant variable is a Python-code representation of a storage location for a value that is not intended to change because it is constant.

# expression is a Python-code representation of a combination of values, variables, and operators that evaluates to a single value.

# An operator precedence is the order in which operators are evaluated in an expression.

import stdio

# program 1.2.1
# ruler.py

#ruler1 = '1'
#ruler2 = ruler1 + '2' + ruler1
#ruler3 = ruler2 + '3' + ruler2
#ruler4 = ruler3 + '4' + ruler3
#stdio.write(ruler1)

#stdio.write(ruler2)

#stdio.write(ruler3)

#stdio.write(ruler4)

# program 1.2.2
# intops.py

import sys

#a = 1234
#b = 5

#total = a + b
#diff = a - b
#prod = a * b
#quot = a // b
#rem = a % b
#exp = a ** b

#stdio.write(str(a) + ' + ' + str(b) + ' = ' + str(total))
#stdio.write('\n')
#stdio.write(str(a) + ' - ' + str(b) + ' = ' + str(diff))
#stdio.write('\n')
#stdio.write(str(a) + ' * ' + str(b) + ' = ' + str(prod))
#stdio.write('\n')
#stdio.write(str(a) + ' // ' + str(b) + ' = ' + str(quot))
#stdio.write('\n')
#stdio.write(str(a) + ' % ' + str(b) + ' = ' + str(rem))
#stdio.write('\n')
#stdio.write(str(a) + ' ** ' + str(b) + ' = ' + str(exp))

# program 1.2.3
# floatops.py

#a = float(123.456)
#b = float(78.9)

#total = a + b
#diff = a - b
#prod = a * b
#quot = a // b
#rem = a % b
#exp = a ** b

#stdio.write(str(a) + ' + ' + str(b) + ' = ' + str(total))
#stdio.write('\n')
#stdio.write(str(a) + ' - ' + str(b) + ' = ' + str(diff))
#stdio.write('\n')
#stdio.write(str(a) + ' * ' + str(b) + ' = ' + str(prod))
#stdio.write('\n')
#stdio.write(str(a) + ' // ' + str(b) + ' = ' + str(quot))
#stdio.write('\n')
#stdio.write(str(a) + ' % ' + str(b) + ' = ' + str(rem))
#stdio.write('\n')
#stdio.write(str(a) + ' ** ' + str(b) + ' = ' + str(exp))

# program 1.2.4

# quadratic formoola
# quadratic.py

import math

#b = float(input('Enter the value of b: '))
#c = float(input('Enter the value of c: '))

#discriminant = b*b - 4.0*c
#d = math.sqrt(discriminant)
#stdio.writeln((-b + d) / 2.0)
#stdio.writeln((-b - d) / 2.0)
# ITS PERFECT

# program 1.2.5
# leapyear.py

#year = int(input('Enter the year: '))

#isLeapYear = (year % 4 ==0)
#isLeapYear = isLeapYear and ((year % 100) != 0)
#isLeapYear = isLeapYear or  ((year % 400) == 0)
#stdio.writeln(isLeapYear)