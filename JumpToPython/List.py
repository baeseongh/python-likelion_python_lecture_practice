# 리스트(List)
odd = [1, 3, 5, 7, 9] # 리스트명 = [요소1, 요소2, 요소3 ...]
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']] # 리스트 안에는 어떠한 자료형도 포함시킬 수 있다.


# 리스트의 인덱싱과 슬라이싱
## 리스트의 인덱싱
a = [1,2,3]
a[0]
a[0]+a[2]
a[-1]
### 이중 리스트 인덱싱
a = [1,2,3,['a','b','c']]
a[3]
a[-1]
a[-1][0]
a[-1][1]
a[-1][2]
### 삼중 리스트 인덱싱
a = [1,2,['a','b',['Life', 'is']]]
a[-1][-1][0]
a[2][2][0]
a[-1][-1][1]
a[2][2][1]

## 리스트의 슬라이싱
a = [1,2,3,4,5]
a[0:2] # 0부터 1(2-1)까지
b = a[:2] # 처음부터 1(2-1)까지
c = a[2:] # 2부터 끝까지
### 예제) A = [1,2,3,4,5]를 슬라이싱해서 리스트 [2,3] 만들기
A = [1,2,3,4,5]
res = A[1:3]

## 중첩된 리스트 슬라이싱
a = [1,2,3,['a','b','c'],4,5]
a[2:5]
a[3][:3]


# 리스트 연산
## 1. 리스트 더하기(+)
a = [1,2,3]
b = [4,5,6]
a + b # 합쳐서 새로운 리스트

## 2. 리스트 반복하기(*)
a = [1,2,3]
a * 3 # 반복되어 새로운 리스트

## 3. 리스트 길이 구하기
a= [1,2,3]
len(a) # 요소 개 수 만큼 나온다.

## 예시) 리스트 연산 오류
a = [1,2,3]
a[2] + "hi" # TypeError (정수형 값에 문자열을 더할 수 없음)
str(a[2]) + "hi" # 숫자를 문자로 바꾸어 더함


# 리스트의 수정과 삭제
## 리스트 값 수정하기
a = [1,2,3]
a[2] = 4
a

## del 함수를 사용해 리스트 요소 삭제하기
a = [1,2,3]
del a[1] # del 함수는 파이썬 자체적으로 가지고 있는 삭제 함수 'del 객체' 형식으로 사용한다.
a
a = [1,2,3,4,5] # 슬라이싱을 통해 삭제
del a[2:]

# 리스트 관련 함수
## 리스트 요소 추가(append)
a = [1,2,3]
a.append(4) # 리스트의 맨 마지막에 4를 추가
a.append([5,6]) # 리스트를 추가할 수 있
a

## 리스트 정렬(sort)
a = [1,4,3,2]
a.sort() #오름차순 정렬
a
a.sort(reverse=True) # 내림차순 정
a = ['a','c','b']렬

## 리스트 뒤집기(reverse)
a = ['a','c','b']
a.reverse() # 정렬이 아닌 뒤집기
a

## 위치반환(index)
a.index(3) # 요소 3의 위치 반환
a.index(1) # 요소 1의 위치 반환
### 존재 하지 않는 값은 위치는 오류 표출

## 리스트에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4) # a[0] 위치에 4 삽입 'insert(a,b)' a번째 위치에 b를 삽입함
a.insert(3,5)

## 리스트 요소 제거(remove)
a = [1,2,3,1,2,3]
a.remove(3) # 첫 번째로 나오는 x를 삭제함

## 리스트 요소 끄집어내기(pop)
a = [1,2,3]
a.pop() # 3, pop()은 맨 마지막 요소를 반환하고 리스트에서 요소를 삭제함
a
a = [1,2,3]
a.pop(1) # 2, 'pop(x)'는 리스트의 x번째 요소를 반환하고 요소를 삭제

## 리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
a.count(1) # 2, 'count(x)'는 리스트안에 x가 몇 개 있는지 파악하여 반환함

## 리스트 확장(extend)
a = [1,2,3]
a.extend([4,5]) # [1,2,3,4,5], 'extend(x)'에서 x에는 리스트만 올 수 있으며, 원래 리스트에 x리스트를 더한다.
a
b = [6,7]
a.extend(b) # 리스트 값을 가진 변수를 더할 수 있다.
a.extend('문자열') # 문자열 각각을 쪼개어 리스트로 더 한다. '문','자','열'
a.extend([1,2,[1,2]]) # 중첩된 리스트를 더할 수 있다.
a