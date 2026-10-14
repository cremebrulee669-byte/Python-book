j = 0
for i in range(j, 10):
    j += 1
print(j)
# j = 10

j = 0
for i in range(10):
    j += j
print(j)
# j = 0

for j in range(10):
    j += j
print(j)
# j = 18