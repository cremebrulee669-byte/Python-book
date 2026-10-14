import stdio

n = int(input("gimme a number "))
i = 1
j = 1
while 1 <= i <= n:
    for j in range(1, n + 1):
        if (i % j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write(' ')
    i += 1
    stdio.writeln(i)

