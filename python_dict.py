# 딕셔너리 (내장함수)

song = {'잔나비' : '주저하는 연인들을 위해', '루시드 폴' : '바람, 어디에서 부는지'}

print(song)

# 하나의 키 : value 쌍을 추가하는 방법
# 딕셔너리형 변수[키] = value

song['태연'] = '사계'

print(song)

# 하나의 키 : value 쌍을 삭제하는 방법 del 함수
# del 변수[키]

del song['태연']

print(song)

# key로 value 얻기, 변수.get(key)

print(song.get('잔나비'))