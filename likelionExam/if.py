# 제어문(코드의 흐름을 제어하는 문법) 
# 분기문(if문, 컴퓨터에게 선택의 여지와 조건 부여) 

# if(조건):

## 예제1. 85점 이상 PASS, FAIL

score = int(input('점수를 입력해 주세요 : '))

if (score >= 85) :
    print('PASS')
else :
    print('FAIL')

## 예제2
 
activ = input('활동하는 동아리 이름 : ')

if(activ=='멋쟁이사자처럼'):
    print('아기사자 hi~')
else:
    print('아직 멋사 안하는 흑우 없제?')

## 예제3

money = int(input('지갑에 돈 얼마 있어? : '))

if(money>=5000):
    print('점심은 아웃백')
elif(money>=3000):
    print('점심은 학식')
elif(money>=1000):
    print('점심은 컵라면')
else:
    print('굶즈아ㅏㅏㅏ')





