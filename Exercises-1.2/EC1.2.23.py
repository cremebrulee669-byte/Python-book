import stdio
import math

x = float(input("Enter a value for x: "))
y = float(input("Enter a value for y: "))

r = math.sqrt(x ** 2 + y ** 2)
theta = math.atan(y / x)
stdio.writeln(r)
stdio.writeln(theta)
stdio.writeln("This is your polar coordinates")