import stdio
import random

x = int(input("Enter a number: "))
for i in range(0, x):
    avg = random.random()
    stdio.writeln(avg)
    avg += random.random()
    
Avg = avg/x
stdio.writeln("Average: " + str(Avg))