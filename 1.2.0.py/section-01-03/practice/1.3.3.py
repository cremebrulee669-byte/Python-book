import stdio

n = int(input("gimme a number "))
power = 1
i = 0
while i <= n:
    stdio.writeln(str(i) + ' ' + str(power))
    power = 2 * power
    i = i + 1