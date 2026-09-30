import stdio

a = input("Enter a positive integer:")
b = input("Enter another positive integer: ")
c = input("Enter ANOTHER positive INTEGER: ")

if int(a) >= int(b) + int(c):
    stdio.writeln('NO NO NO THIS IS ALL WRONG')
elif int(b) >= int(a) + int(c):
    stdio.writeln('NO NO NO THIS IS ALL WRONG')
elif int(c) >= int(a) + int(b):
    stdio.writeln('NO NO NO THIS IS ALL WRONG')
else:
    stdio.writeln('oui oui, tres bien')