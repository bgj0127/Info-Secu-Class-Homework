# Tuple : List 와 같지만 데이터 수정 불가
myTuple = ('abc','efw','hty','okq','irn')

# 튜플 길이 : len()
print(len(myTuple))

# 튜플 결합 : +
print(myTuple+('a','b','c'))  # 이상하게 여기서만 적용된다. 다른 줄로 넘어가면 결합 안 됨

# 데이터 슬라이싱 : [n,m]
print(myTuple[1:3])

# 인덱스 검색 : index()
print(myTuple.index('abc'))
print(myTuple.index('irn'))

# 데이터 계수 찾기 : count()
print(myTuple)
print(myTuple.count('abc'))
