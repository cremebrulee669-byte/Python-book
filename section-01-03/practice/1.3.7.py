import stdio

n = int(input("gimme a number "))

v = 1
while v <= n // 2:
    v *= 2
while v > 0:
    if n < v:
        stdio.write(0)
    else:
        stdio.write(1)
        n -= v
    v //= 2
stdio.writeln()