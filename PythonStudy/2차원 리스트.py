a = [[10, 20], [30, 40], [50, 60]]
print(a)

print(a[0][0])
print(a[0][1])
print(a[1][1])

for x,y in a:
    print(x,y)

print("---------------")

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()

print("---------------")

i = 0
while i < len(a):
    x, y = a[i]
    print(x,y)
    i += 1

print("---------------")

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1