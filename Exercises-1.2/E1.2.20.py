import stdio

d = int(input("Enter a value for d: "))
m = int(input("Enter a value for m: "))

if (3 <= m and d > 20) or (m <= 6 and d < 20):
    stdio.writeln(True)
elif 3 < m < 6:
    stdio.writeln(True)
else:
    stdio.writeln(False)
