import stdio

f = 0
g = 1
for i in range(16):
    stdio.writeln(f)
    f = f + g
    g = f - g
# the code writes 0 , 1, 1, Wait, it actually just does the fibonacci sequence