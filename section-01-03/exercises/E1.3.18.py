import stdio
import math

S = int(input("What square root do you want to find? "))
x = 1
y = 1
while y ** 2 != S:
    x = y
    y = 0.5 * (x + S / x)
stdio.writeln(y)