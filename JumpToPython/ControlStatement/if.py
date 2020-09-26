# if 문
## 돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# if문의 기본 구조
조건문 = True
if 조건문:
    print('수행할 문장1')
    print('수행할 문장2')
else:
    print('수행할 문장A')
    print('수행할 문장B')

## 들여쓰기
### - if문을 만들 때 'if 조건문:' 바로 아래 문장부터 if문에 속하는 모든 문장에 들여쓰기(indentation)을 해야 한다.
if 조건문:
    print('수행할 문장1')
    print('수행할 문장2')
#### - 들여쓰기를 무시하면 들어쓰기 오류 발생
if 조건문:
    print('수행할 문장1')
print('수행할 문장2')
print('수행할 문장3')
### - 들여쓰기는 언제나 같은 너비로 해야한다.
### - 들여쓰기를 4칸 탭으로 하는 것을 권장한다.


# 조건문이란 무엇인가?
## '조건문'이란 참과 거짓을 판단하는 문장을 말한다.
money = True # money가 조건문

## 비교 연산자
### 비교연산자 (<, >, ==, !=, >=, <=)
x = 3
y = 2
x < y # True x가 y보다 작다.
x > y # False x가 y보다 크다.
x == y # False x와 y가 같다.
x != y # True x와 y가 같지 않다.
x >= y # True x가 y보다 크거나 같다.
x <= y # False x가 y보다 작거나 같다.
### 예제) 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라.
money = 2000 # 2000원을 가지고 있다.
if money >= 3000:
    print("택시 타고 가라")
else:
    print("걸어 가라")

## and, or, not
x or y # x와 y 둘 중에 하나만 참이여도 참이다.
x and y # x와 y 모두 참이어야 참이다.
not x # x가 거짓이면 참이다.
### 예제) 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라.
money = 2000 # 2000원을 가지고 있다.
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

## x in s, x not in s
### x in 리스트, x not in 리스트
### x in 튜플, x not in 튜플
### x in 문자열, x not in 문자열
1 in [1,2,3] # True 1이 [1,2,3] 안에 있는가?
1 not in [1,2,3] # False 1이 [1,2,3] 안에 없는가?
'a' in ('a','b','c') # True
'j' not in ('a','b','c') # Ture
### 예제) 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
### 예제) '주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고가라'는 문장을 조건문으로 만들어 보자.
pocket = ['bill', 'money', 'card']
if 'card' not in pocket:
    print("걸어 가라")
else:
    print("버스를 타고 가라")


# 다양한 조건을 판단하는 elif
## 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라
pocket = ['bill', 'money']
card = True
if 'money' in pocket:
    print("택시를 타고 가라") # 주머니에 돈이 있으면
elif card:
    print("택시를 타고 가라") # 주머니에 돈이 없고 카드가 있으면
else:
    print("걸어 가라") # 주머니에 돈도 없고 카드도 없으면


# if 문을 한 줄로 작성하기
if 'money' in pocket: pass
else: print("카드를 꺼내라")


# 조건부 표현식(삼항연산자)
score = 90
if score >= 60:
    message = "success"
else:
    message = "failure"

## 조건부 표현식 예시
print("success") if score >= 60 else print("failure") # 'Ture if 조건 else False'
### 파이썬은 주류 언어들의 삼향 연산자 형태 '조건 ? True : False'를 지원하지 않는다.