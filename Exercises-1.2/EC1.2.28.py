import stdio
import math

lo0 = 98
lo = float(input("Enter the longitude of the point (in degrees): "))
la = float(input("Enter the latitude of the point (in degrees): "))
y = 1/2 * math.log((1 + math.sin(la)) / (1 - math.sin(la)))
x = lo - lo0
print("Mercator projection coordinates: x =", x, ", y =", y)