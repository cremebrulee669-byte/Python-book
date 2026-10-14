import stdio

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))

if a == b and b == c:
    stdio.writeln('True')
else:
    stdio.writeln("False")