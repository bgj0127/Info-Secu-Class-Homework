# Dictionary : 키(key)와 벨류(value)를 이용한 데이터 관리
dic = {10: 'a', 20: 'b', 30: 'c'}  # 딕셔너리에서 데이터의 중복은 가능하지만, key 값은 중복될 수 없다.
print(dic)

# 딕셔너리 길이 : len()
print(len(dic))

# 데이터 참조 : []
print(dic[20])  # 딕셔너리에서 데이터를 탐색할 땐 key 값으로 찾는다.

# 데이터 삭제 : del
del dic[20]  # 키워드 형태로 존재한다.
print(dic)