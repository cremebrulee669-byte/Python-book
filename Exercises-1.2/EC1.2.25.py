import stdio

x = input("Enter a number: ")
y = input("Enter another number: ")
z = input("Enter a third number: ")

if (x < y < z) or (x > y > z):
    stdio.writeln(True)
else:
    stdio.writeln(False)