a = input("Give me a number pls")
b = input("Give me another number pls")
c = input("Give me yet another number pls")

a = float(a)
b = float(b)
c = float(c)

print(max(a, b, c), (a + b + c) - max(a, b, c) - min(a, b, c), min(a, b, c))