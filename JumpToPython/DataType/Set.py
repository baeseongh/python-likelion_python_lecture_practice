# 집합(Set)
s1 = set([1,2,3]) # set() 안에 리스트 입력
s2 = set("Hello") # => {'e', 'H', 'o', 'l'} 를 반환


# 집합 자료형의 특징
## - 중복을 허용하지 않는다.
## - 순서가 없다.(unordered) (인덱싱을 지원하지 않는다.)
## 인덱싱 접근 방법
s1 = set([1,2,3])
l1 = list(s1)
l1[0]
t1 = tuple(s1)
t1


# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

## 교집합
s1 & s2 # {4, 5, 6} 반환
s1.intersection(s2) # s2.intersection(s1)

## 합집합
s1 | s2 # {1, 2, 3, 4, 5, 6, 7, 8, 9} 반환
s1.union(s2) # s2.union(s1)

## 차집합
s1 - s2 # {1, 2, 3} 반환
s1.difference(s2)
s2 - s1 # {8, 9, 7} 반환
s2.difference(s1)


# 집합 자료형 관련 함수
## 값 1개 추가하기(add)
s1 = set([1,2,3])
s1.add(4)
s1

## 값 여러개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
s1

## 특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
s1