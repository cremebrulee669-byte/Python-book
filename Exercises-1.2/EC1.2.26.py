import stdio

m = input("month number")
y = input("year")
d = input("day number")

m = float(m)
y = float(y)
d = float(d)

y0 = y - ((14 - m) / 12)
x = y0 + y0 / 4 - y0 / 100 + y0 / 400
m0 = m + 12 * ((14 - m) / 12) - 2
d0 = (d + x + (31 * m0) / 12) % 7
stdio.writeln(int(d0))

# Days follow 1-7 Monday-Sunday, so Monday is 1, Tuesday is 2, so on until Saturday is 6, and zero for Sunday
# This is for a Gregorian Calender