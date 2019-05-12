# 리스트(내장함수)

li = [3, 1, '배가', 4, '고파요', 5, 1, 3, 3]

# 인덱싱 슬라이싱

print(li[0:4])

# 리스트의 길이 lng(변수)

print(len(li))

# 리스트의 원소를 오름차순 정렬
li2 = [3,1,4,2,5]

print(li2)

li2.sort()

print(li2)

# 리스트 내의 특정 원소 인덱스를 반환해주는 함수 .index(요소)

print(li.index('배가'))

# 리스트 내의 특정 원소의 갯수 세기 : .count(요소)

print(li.count(3))
