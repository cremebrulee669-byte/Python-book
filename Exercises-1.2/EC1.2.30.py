import stdio
import math

x1 = input("Enter the x-coordinate of the first point: ")
y1 = input("Enter the y-coordinate of the first point: ")
x2 = input("Enter the x-coordinate of the second point: ")
y2 = input("Enter the y-coordinate of the second point: ")

x1 = math.radians(float(x1))
y1 = math.radians(float(y1))
x2 = math.radians(float(x2))
y2 = math.radians(float(y2))

d = 60 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
stdio.writeln(d)