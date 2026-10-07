import stdio

n = int(input("gimme a number "))

total = 0.0
for i in range(1, n + 1):
    total += 1.0 / i
stdio.writeln(total)