# while문
## - 조건이 참인 동안에 계속 수행한다.
조건문 = True
while 조건문:
    print('수행할 문장1')
    print('수행할 문장2')
    print('수행할 문장3')
    break

## 예제) 열 번 찍어 안넘어가는 나무 없다.
treeHit = 0 # 나무를 찍은 회수
while treeHit < 10: # treeHit가 10보다 작은 동안에 반복
    treeHit += 1 # treeHit를 1씩 증가
    print("나무를 %d번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다~")


# while문 만들기
prompt = """ # 문항 변수
1. Add
2. Del
3. List
4. Quit
Enter number: """
number = 0 # 번호를 입력받을 변수
while number != 4: # 번호가 4가 아닌 동안 반복
    print(prompt)
    number = int(input())
## - 4를 입력하지 않으면 계속해서 prompt 출력, 4를 입력하면 조건문이 거짓이 되어 while문을 빠져나가게 된다.


# while문 강제로 빠져나가기(break)
coffee = 10
money = 300
while money:
    print("%d원을 받았습니다. 커피가 나옵니다." % money)
    coffee -= 1 # while문을 한 번 돌 때 커피가 하나씩 줄어든다.
    if coffee == 0:
        print("커피가 다 떨여졌습니다. 판매를 중지합니다.")
        break

## 예제)
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피가 나옵니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈은 %d 입니다. 커피가 나옵니다." % (money - 300))
        coffee -= 1
    else:
        print("돈이 반환됩니다.")
        print("커피의 재고가 %d개 남았습니다." % coffee)
    if coffee == 0:
        print("커피가 매진 됐습니다. 판매를 중지합니다.")
        break


# while문의 맨 처음으로 돌아가기(continue)
## 예제) 1 부터 10까지 숫자 중 홀수만 출력하는 코드
n = 0
while n < 10:
    n += 1
    if n%2 == 0: continue # a를 2로 나누었을때 나머지가 0이면(짝 수면) 처음으로 돌아간다.
    print(n)

## 예제) 1부터 10까지 숫자 중 3의 배수를 뺀 나머지 값을 출력
i = 0
while i < 10:
    i += 1
    if i % 3 == 0: continue
    print(i)


# 무한루프
## - 수행을 무한히 반복한다.
## - Break등 while문이 끝나는 조건을 설정하지 않으면, while문이 무한히 수행된다.
while True:
    print("Ctrl+C를 툴러야 while문을 빠져나갈 수 있습니다.")
