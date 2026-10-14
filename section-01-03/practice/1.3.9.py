import stdio

n = int(input("gimme a number "))

factor = 2
while factor*factor <= n:
    while (n % factor) == 0:
        n //= factor
        stdio.writeln(str(factor) + ' ')
    factor += 1
if n > 1:
    stdio.write(n)
stdio.writeln()