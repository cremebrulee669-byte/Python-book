import stdio

a = int(input("Enter a number: "))
if a > 0 or a < 0:
    stdio.writeln('a is a good value')
else:
    stdio.writeln("Cant perform quadratic operation")
    
b = int(input("Enter another number: "))
c = int(input("Enter the third number: "))
discriminant = b**2 - 4*a*c
if discriminant < 0:
    stdio.writeln("No real roots")
else:
    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)
    stdio.writeln(x1)
    stdio.writeln(x2)
