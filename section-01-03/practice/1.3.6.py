import stdio

EPSILON = 1e-15

c = float(input("gimme a number "))
t = c
while abs(t - c/t) > (EPSILON * t):
    t = (c/t + t) / 2.0
    
stdio.writeln(t)