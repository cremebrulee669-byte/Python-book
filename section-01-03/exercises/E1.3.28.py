import stdio

x = int(input("I want a number "))
y = int(input("I want another number "))

if x > y:
    while x > 0:
        z = y % x
        y = x
        x = z
    stdio.writeln(y)
else:
    while y > 0:
        z = x % y
        x = y
        y = z
    stdio.writeln(x)