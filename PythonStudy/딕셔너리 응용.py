d = {'a':10,'b':20,'c':30,'d':40}
d.setdefault('e') # setdefault(키)는 딕셔너리에 키-값 쌍을 추가한다.
print(d)

d.setdefault('f',60)
print(d)

d.update(e=50)
print(d)

d.pop('a')
print(d)

del d['b']
print(d)

d.clear()
print(d)