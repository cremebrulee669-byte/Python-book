
r = int(input("Enter the red component (0-255): "))
g = int(input("Enter the green component (0-255): "))
b = int(input("Enter the blue component (0-255): "))
w = max(r/255, g/255, b/255)
c = (w - r/255) / w
m = (w - g/255) / w
y = (w - b/255) / w
k = 1 - w

print('Your CMYK from RGB are: c =', c, ', m =', m, ', y =', y, ', k =', k)