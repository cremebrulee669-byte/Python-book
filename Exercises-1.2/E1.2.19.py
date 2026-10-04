import math
import stdio

x = input("Enter a value for x: ")
x = float(x)
y = input("Enter a value for y: ")
y = float(y)
t = input("Enter a value for t: ")
t = float(t)
g = 9.80665

stdio.writeln(x + (y*t) - (g*(t**2) / 2))