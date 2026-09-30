# A program must be composed that takes two positive integers as command-line arguments and writes True if either evenly divides the other.

import stdio
import math

a = input("Enter a positive integer:")
b = input("Enter another positive integer: ")

if int(a) % int(b) == 0 or int(b) % int(a) == 0:
    stdio.writeln(True)
else:
    stdio.writeln(False)
