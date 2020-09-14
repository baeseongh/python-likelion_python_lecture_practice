# a 단 부터 9단 까지
a = int(input('단을 입력해 주세요 : '))

for n in range(a, 10):
    for i in range(1, 11):
        print(n, "X",i, "=", n*i)