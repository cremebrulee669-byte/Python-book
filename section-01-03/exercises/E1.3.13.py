import stdio

n = int(input("Enter a number pls: "))
for i in range(1, n + 1):
    if 2 ** i <= n:
        stdio.write(str(2 ** i) + ' ')
    else:
        break