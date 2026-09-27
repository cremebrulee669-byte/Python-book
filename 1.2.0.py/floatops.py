# program 1.2.3
# floatops.py


import stdio
import sys

a = float(123.456)
b = float(78.9)

total = a + b
diff = a - b
prod = a * b
quot = a // b
rem = a % b
exp = a ** b

stdio.write(str(a) + ' + ' + str(b) + ' = ' + str(total))
stdio.write('\n')
stdio.write(str(a) + ' - ' + str(b) + ' = ' + str(diff))
stdio.write('\n')
stdio.write(str(a) + ' * ' + str(b) + ' = ' + str(prod))
stdio.write('\n')
stdio.write(str(a) + ' // ' + str(b) + ' = ' + str(quot))
stdio.write('\n')
stdio.write(str(a) + ' % ' + str(b) + ' = ' + str(rem))
stdio.write('\n')
stdio.write(str(a) + ' ** ' + str(b) + ' = ' + str(exp))