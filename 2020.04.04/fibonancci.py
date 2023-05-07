# the 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987 

print(0)
print(1)
print(1)
x = 1
y = 1
z = 1
i = 0
while True:
    z = x + y
    y = x
    x = z
    i = i +1
    print (z)
    if i == 17:
        break

