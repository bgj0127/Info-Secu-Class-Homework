student = ['A', 'B', 'C', 'D', 'E']

# list 길이 : len()
print("list 길이 : " + str(len(student)))

# list 데이터 추가 : append()
student.append('F')
print(student)

# list 데이터 삭제 : pop()
student.pop()  # 가장 마지막 데이터 삭제
print(student)
student.pop(2)  # 인덱스2 데이터 삭제
print(student)

# list 연장 : extend()
student.extend(['G', 'H', 'I'])
print(student)

# 데이터 삽입 : insert()
student.insert(2, 'new data')  # insert(인덱스 번호,데이터)
print(student)

# 특정 데이터 삭제 : remove()
student.remove('new data')
print(student)

# 전체 데이터 삭제 : clear()
student.clear()
print(student)
student.extend([1,6,2,8,10,4,7])

# 데이터 정렬 : sort() 단, 데이터의 형이 같아야 한다.
student.sort(reverse=False)  # 오름차순(default 값)
print(student)
student.sort(reverse=True)  # 내림차순
print(student)

# 데이터 역순 : reverse()
student.reverse()
print(student)

# 데이터 슬라이싱 : [n,m]
myList = ['abc','def','ghi','jkl','mlo']
print(myList)
print(myList[1:3])  # [처음 인덱스 값 : 마지막 인덱스 값 - 1]
print(myList[:5])  # 인덱스 0부터 시작



