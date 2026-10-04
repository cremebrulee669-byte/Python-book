import stdio
import math
import random

v = random.random()
u = random.random()

w = math.sin(2 * math.pi * v) * (-2 * math.log(u)) ** (1 / 2)
stdio.writeln(v)
stdio.writeln(u)
stdio.writeln(w)
stdio.writeln("This is your number(The third one)")