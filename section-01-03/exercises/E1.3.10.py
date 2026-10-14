import stdio
import math

for n in range(1, 10):
    stdio.write(str(math.log2(n)) + ' ')
    stdio.write(str(n) + ' ')
    stdio.write(str(n * math.log(n)) + ' ')
    stdio.write(str(n ** 2) + ' ')
    stdio.write(str(n ** 3) + ' ')
    stdio.write(str(2 ** n) + ' ')
    stdio.write('\n')