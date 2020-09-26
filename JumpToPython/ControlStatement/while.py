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

