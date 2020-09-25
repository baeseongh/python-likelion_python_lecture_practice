# 문자열(String)
## 큰따옴표
"Hello World"

## 작은따옴표
'Python is fun'

## 큰따옴표 3개
"""Life is too short, You need Python"""

## 작은따옴표 3개
'''Life is too short, You need Python'''


# 문자열 안에 따옴표
## 작은 따옴표
food = "python's favorithe food is perl"

## 큰 따옴표
say = '"Python is very easy" he says.'

## 백슬래시
food = 'python\'s favorithe food is perl'
say = "\"Python is very easy\" he says."


# 줄나눔
## 이스케이프 코드
multiline = "Life is too short\nYou need Python"

## 작은따옴표, 큰따옴표 3개
multiline='''
Life is too short
You need Python
'''
multiline="""
Life is too short
You need Python
"""

# 문자열 연산
## 문자열 더하기
head = "Python"
tail = " is fun!"
print(head + tail)

## 문자열 곱하기
a = "Python"
a * 2
print("=" * 50)
print("My Program")
print("=" * 50)

## 문자열 길이
a = "Life is too short"
len(a)


# 문자열 인덱싱, 슬라이싱
## 인덱싱(Indexing)
a = "Life is too short, You need Python"
a[3]
a[0]
a[12]
a[-1] # 뒤에서 1번째
a[-0] # 0하고 같다.
a[-2] # 뒤에서 2번째

## 슬라이싱(Slicing)
a = "Life is too short, You need Python"
a[0:4] # 0부터 3(4-1)까지
a[0:3]
a[12:17]
a[19:] # 19부터 끝까지
a[:17] # 처음부터 16(17-1)까지
a[1:] # 처음부터 끝까지
a[19:-7] # 19부터 -8(-7-1)까지

## 문자열 나누기(슬라이싱)
a = "20010331Rainy"
date = a[:8]
year = a[:4]
month = a [4:6]
day = a[6:8]
weather = a[8:]
print(date)
print(year+'년'+month+'월'+day+'일')
print(weather)
### 예제)문자열 변경하기(Pithon => Python)
a = "Pithon"
### a[1] = y [x] (문자열 자료형의 요솟값은 바꿀 수 없다.)
P = a[:1]
thon = a[2:]
P+'y'+thon


# 문자열 포매팅(Formatting)
## 1. 숫자 바로 대입
"I eat %d apples" %3 # 숫자 = %d

## 2. 문자열 바로 대입
"I eat %s apples" %"five" # 문자 = %s

## 3. 변수(Number)로 대입
number = 3
"I eat %d apples" %number

## 4. 2개 이상의 값 넣기
number = 19
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)


# %s 문자열 포맷코드 특징
"I have %s apples" %3
"rate is %s" %3.234
"Error is %d%%" %98


# 포맷코드 숫자와 함께 사용하기
## 1. 정렬과 공백
"%10s" %"hi" # 10칸 중 오른쪽 정렬되어 hi표출
"%-10sjane" %"hi" # 10칸 중 왼쪽 정렬되어 hi표출

## 2. 소수점 표현하기
"%0.4f" %3.42134234 # 소수점 4자리 까지 표출
"%10.4f" %3.42134234 # 10칸 중 오른쪽 정렬되어 소수점 4자리 까지 표출


# format 함수를 사용한 포맷팅
## 숫자 바로 대입하기
"I eat {0} apples".format(3)

## 문자열 바로 대입하기
"I eat {0} apples".format("five")

## 숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number)

## 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was for {1} days".format(number, day)

## 이름으로 넣기
"I ate {number} apples. so I was for {day} days".format(number=10, day=3)

## 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was for {day} days".format(10, day=3)

## 왼쪽 정렬
"{0:<10}".format("hi")

## 오른쪽 정렬
"{0:>10}".format("hi")

## 가운데 정렬
"{0:^10}".format("hi")

## 공백 채우기
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")

## 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y) # 소수점 4자리 까지 표출
"{0:10.4f}".format(y) # 10칸 중 오른쪽 정렬되어 소수점 4자리 까지 표출

## {} 문자 표현하기
"{{ and }}".format()


# f문자열 포매팅
## (python 3.6 버전 부터 사용가능)
name = "홍길동"
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
f'나는 내년이면 {age+1}살이 된다.'

## 딕셔너리
d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

## 정렬
f'{"hi":<10}' # 왼쪽 정렬
f'{"hi":>10}' # 오른쪽 정렬
f'{"hi":^10}' # 가운데 정렬

## 공백채우기
f'{"hi":!<10}'
f'{"hi":=^10}'

## 소수점 표현
y = 3.42134234
f'{y:0.4f}' # 소수점 4자리 까지 표출
f'{y:10.4f}' # 10칸 중 오른쪽 정렬되어 소수점 4자리 까지 표출

## {} 문자 표현하기
f'{{ and }}'
## format 함수와 f 문자열 포매팅을 통해 '!!!python!!!' 표현하기
"{0:!^12}".format("python")
f'{"python":!^12}'


# 문자열 관련 함수
## 문자 개수 세기(count)
a = "hobby"
a.count('b') # 문자열 중 b의 개수를 반환

## 위치 알려주기 1(find)
a = "Python is the best choice"
a.find('b') # 문자열 중 b의 첫 위치를 반환
a.find('k') # 존재하지 않는다면 -1 반환

## 위치 알려주기 2(index)
a = "Life is too short"
a.index('t') # t의 첫 위치 반환
a.index('k') # 존재하지 않는다면 오류

## 문자열 삽입(join)
",".join('abcd') # abdc문자열의 각각 문자 사이에 ',' 삽입
",".join(['a','b','c','d'])

## 대문자로 바꾸기(upper)
a = "hi"
a.upper()

## 소문자로 바꾸기(lower)
a = "HI"
a.lower()

## 공백 지우기
a = " hi "
### 왼쪽 공백 지우기(lstrip)
a.lstrip()
### 오른쪽 공백 지우기(rstrip)
a.rstrip()
### 양쪽 공백 지우기(strip)
a.strip()

## 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg") # 왼쪽 값을 오른쪽 값으로 치환

## 문자열 나누기(split)
a = "Life is too short"
a.split() # 공백 기준으로 문자열 나누어 리스트로 반환
b = "a:b:c:d"
b.split(':') # 값을 기준으로 문자열 나누어 리스트로 반환