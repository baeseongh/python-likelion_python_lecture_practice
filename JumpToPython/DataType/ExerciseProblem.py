#Q1
hr = {'국어':80, '영어':75, '수학':55}
hr_grade = list(hr.values())
i = 0
for l in hr_grade:
    i += l
res = i / len(hr_grade)
print('홍길동의 평균점수 : ', res, '점')


#Q2
n = int(input('숫자를 입력하세요 : '))
if (n%2 == 0):
    print('짝수')
else:
    print('홀수')


#Q3
pin = "881120-1068234"
## splite
yyyymmdd, num = pin.split('-')
## slicing
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)


#Q4
pin = "881120-1068234"
if pin[7] == "1":
    print('남성')
else:
    print('여성')


#Q5
a = "a:b:c:d"
b = a.replace(":","#")
print(b)


#Q6
a = [1,3,5,4,2]
a.sort(reverse=True)
print(a)


#Q7
a = ['Life','is','too','short']
res = " ".join(a)
print(res)


#Q8
a = (1,2,3)
a = a + (4,)
print(a)


#Q9
a = dict()
a
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' Key로 List를 사용할 수 없다.
a[250] = 'python'


#Q10
a = {'A':90, 'B':80, 'C':70}
res = a.pop('B')
print(a)
print(res)


#Q11
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)


#Q12
a = b = [1,2,3]
a[1] = 4
print(b) # [1,4,3] 출력 (a와 b는 같은 메모리를 가리키고 있기 때문에 a와 b모두 값이 변경된다.)