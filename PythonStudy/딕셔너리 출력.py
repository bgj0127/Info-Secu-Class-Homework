x = {'a':10,'b':20,'c':30,'d':40}
for i in x:
    print(i,end=' ')
print(' ')
print('----------------')
for key, value in x.items():
    print(key,value)

print('----------------')
for key in x.keys():
    print(key, end=' ')
print(' ')
print('----------------')
for value in x.values():
    print(value,end=' ')