import stdio
import sys
import math

# program 1.2.5
# leapyear.py

year = int(input('Enter the year: '))

isLeapYear = (year % 4 ==0)
isLeapYear = isLeapYear and ((year % 100) != 0)
isLeapYear = isLeapYear or  ((year % 400) == 0)
stdio.writeln(isLeapYear)