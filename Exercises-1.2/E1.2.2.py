import math

# A program that uses math.sin() and math.cos() to check that the value of cos^2(x) + sin^2(x) equals 1 for any x.
x = 89
cos_squared = math.cos(x) ** 2
sin_squared = math.sin(x) ** 2
print(cos_squared + sin_squared)