import stdio
import math

x = input('Give me an x-value')
y = input('Give me a y-value')

x = int(x)
y = int(y)
stdio.writeln('The distance from the origin is:')
stdio.writeln(math.sqrt((x ** 2) + (y ** 2)))

