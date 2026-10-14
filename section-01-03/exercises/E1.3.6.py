import stdio

i = int(input("Enter a number: "))

if i%100 == 0:
    stdio.writeln(str(i) + "th hello")
elif i%10 == 1:
    stdio.writeln(str(i) + "st hello")
elif i%10 == 2:
    stdio.writeln(str(i) + "nd hello")
elif i%10 == 3:
    stdio.writeln(str(i) + "rd hello")
else:
    stdio.writeln(str(i) + "th hello")
    