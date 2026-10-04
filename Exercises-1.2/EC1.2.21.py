import stdio
import math

t = float(input("Enter the number of years to invest (t): "))
P = float(input("Enter your money you put in initially (P): "))
r = float(input("Enter the annual interest rate (r) as a decimal like 1.04 for 4%: "))

M = P **(r * t)
stdio.writeln(M)