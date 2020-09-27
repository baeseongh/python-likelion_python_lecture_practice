# for문
리스트 = [1,2]
for 변수 in 리스트: # 또는 튜풀, 문자열 (내용 만큼 실행)
    print("수행1")
    print("수행2")

## for문 예제
### 1. 전형적인 for문
test_list = ['one','two','three']
for i in test_list: # one, two, three를 순서대로 i에 대입
    print(i)
### 2. 다양한 for문의 사용
a = [(1,2),(3,4),(5,6)]
for (first, last) in a: # 튜플 (1,2)가 각각 first: 1, last 2 와 같이 대입된다.
    print(first + last) #  1+2 = 3 ...
### 3. for문의 응용
#### 예제) 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오.
marks = [90,25,67,45,80]
for mark in marks:
    print("%d번 학생 %d점으로 합격" % (marks.index(mark)+1, mark)) if mark > 60 else print("%d번 학생 %d으로 불합격" % (marks.index(mark)+1, mark))


# for문과 continue문
marks = [90,25,67,45,80]
for mark in marks:
    if mark < 60: continue
    print("%d번 학생 축하합니다. %d점으로 합격입니다." % (marks.index(mark)+1, mark))


# for문과 함께 자주 사용하는 range 함수
a = range(10)
a # range(0, 10) 반환 <= 0,1,2,3,4,5,6,7,8,9 (0부터 10-1인 리스트)
a = range(10)
a # range(0, 11) 반환 <= 0,1,2,3,4,5,6,7,8,9,10 (0부터 11-1인 리스트)

## range 함수의 예시
add = 0
for i in range(1,11):
    add+=i # add는 1부터 10까지의 합
print(add)
### 예제)
marks = [90,25,67,45,80]
for n in range(len(marks)):
    if marks[n] < 60: continue
    print("%d번 학생 축하합니다. %d점으로 합격입니다!" %(n+1,marks[n]))
### 예제) for문과 range 함수를 사용하여 1부터 100까지 더해보자.
print("시작값 부터 종료값 까지의 합을 구하는 프로그램 입니다.")
start = int(input("시작값을 입력해주세요 : "))
end = int(input("종료값을 입력해주세요 : "))
hap = 0
for i in range(start,end+1):
    hap += i
print("%d부터 %d까지의 합은 %d입니다." % (start,end,hap))

## for와 range를 사용한 구구단
for i in range(2,10): # 1번 for문 (n,x)는 n단 부터 x-1단 까지
    print("%d단 :" %i , end=" ") # end=" "로 줄바꿈 대신 공백을 넣는다.
    for j in range (1,11): # 2번 for문 (n,x) i * j(n ~ x) 곱
        print(i*j, end=" ")
    print("") # 줄바꿈, end를 지정해주지 않으면, print가 끝나고 자동으로 줄바꿈


# 리스트 내포(list comprehension) 사용하기
## - 리스트 안에 for문을 포함하는 리스트 내포를 사용할 수 있다.
### 예제) a 리스트의 각 항목에 3을 곱한 결과를 res 리스트에 담기
a = [1,2,3,4]
res = []
for num in a:
    res.append(num*3)
print(res)
### 예제) 리스트 내포를 사용 하여 a 리스트의 각 항목에 3을 곱한 결과를 res 리스트에 담기
a = [1,2,3,4]
res = [num*3 for num in a]
print(res)
### 예제) 리스트 내포를 사용과 조건을 설정 하여 a 리스트의 각 항목 중 짝수에만 3을 곱한 결과를 res 리스트에 담기
a = [1,2,3,4]
res = [num*3 for num in a if num%2 == 0] # res = [표현식 for 항목 in 반복객체 if 조건]
print(res)
### 예제) 리스트 내포를 사용하여 구구단 구현
res = [x*y for x in range(2,10)
       for y in range(1,11)]
print(res)