import stdio

a = input('Pick a positive number... any number. (Specifically a whole number greater than zero and not negative please Thank You)')
b = input('Pick another positive number... any number. (Specifically a whole number greater than zero and not negative please Thank You)')

a = int(a)
b = int(b)

stdio.writeln("This number is between your numbers:")
stdio.writeln((a + b) / 2)