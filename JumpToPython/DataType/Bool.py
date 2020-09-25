# 불(Bool)
## - 참(True) 와 거짓(False) 두가지 값만 가질 수 있다.
a = True
b = False

## 1. 타입 확인
type(a) # 'type(x)'는 x의 자료형을 확인하는 내장 함수, <class 'bool'> 반환
type(b) # <class 'bool'> 반환

## 2. 불 자료형은 조건문의 반환 값으로도 사용 된다.
1 == 1 # True
2 > 1 # True
2 < 1 # False


# 자료형의 참과 거짓
## - 문자열, 리스트, 튜플, 딕셔너리 는 값이 비어 있으면("", [], (), {}) 거짓(False)가 된다. , 값이 비어있지 않으면 참(True)이다.
## - 숫자형 은 그 값이 0 일 때 거짓(False)가 된다.
## - None은 거짓(False)이다.

## 참 거짓 활용 예시1
a = [1,2,3,4]
while a: # a가 참인동안 while 문 실행
    print(a.pop()) # 리스트 a의 마지막 요소를 하나씩 꺼낸다.

## 참 거짓 활용 예시2
if []: # 만약 [] 가 참이면
    print("참")
else: # 만약 [] 가 참이 아니면
    print("거짓")

## 참 거짓 활용 예시3
if [1,2,3]:
    print("참")
else:
    print("거짓")


# 불 연산
bool('python') # True
bool('') # False
bool([1,2,3]) # True
bool([]) # False
bool(()) # False
bool({}) # False
bool(0) # False
bool(3) # True
