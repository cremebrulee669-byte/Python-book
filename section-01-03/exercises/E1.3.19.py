import stdio

i = int(input("gimme a number "))
k = int(input("gimme a base "))

v = 1
while v <= i // k:
    v *= k
while v > 0:
    if i < v:
        stdio.write(0)
    else:
        stdio.write(i // v)
        i -= v
    v //= k
stdio.writeln()
stdio.write("This is the base " + str(k) + " representation of the number you gave me: ")