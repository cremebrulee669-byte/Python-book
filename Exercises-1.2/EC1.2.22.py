import stdio

T = input("Enter a value for Temperature in degrees Fahrenheit: ")
T = float(T)
v = input("Enter a value for Wind Speed in miles per hour: ")
v = float(v)

w = 35.74 + 0.6215 * T + (0.4275 * T - 35.75) * v ** 0.16
stdio.writeln(w)
stdio.writeln("This is your wind chill")