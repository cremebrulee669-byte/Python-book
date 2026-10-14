import stdio

n = int(input("gimme a number "))
i = 1
j = 1
while 1 <= i <= n:
    j = 1
    while 1 <= j <= n:
        if (i % j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write(' ')
        j += 1
    i += 1
    stdio.writeln(i - 1)

