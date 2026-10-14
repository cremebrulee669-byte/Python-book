import stdio

n = int(input("Enter the dimensions of the square: "))

for i in range(n // 2):
    for r in range(n - 1):
        stdio.write(' *')
    stdio.writeln()
    for j in range(n):
        stdio.write('* ')
    stdio.writeln()
if n % 2 == 1:
    for r in range(n - 1):
        stdio.write(' *')
    stdio.writeln()
    