import stdio

n = int(input("Enter a number: "))
ruler = '1'
stdio.writeln(ruler)
for i in range(2, n+1):
    ruler = ruler + ' ' + str(i) + ' ' + ruler
    stdio.writeln(ruler)

# it just keeps going on and on and on and on when n = 100