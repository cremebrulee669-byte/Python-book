import stdio

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

if 0.0 < a < 1.0 and 0.0 < b < 1.0:
    stdio.writeln(True)
else:
    stdio.writeln(False)