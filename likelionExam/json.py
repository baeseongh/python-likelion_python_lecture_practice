import json

# 1. python 사전형 객체 형태
diary = {
	'id' : 3,
	'title' : 'likelion',
	'content' : 'likelion 7th json study'
}

print(diary)
print(type(diary))

# 2. 사전형을 json 형태로 변환하기
diary_s = json.dumps(diary) #dumps : dictionary 형태, 파이썬 형태의 자료형을 json으로 변환해준다.

print(diary_s) 
print(type(diary_s))

# 3. 문자열을 json 형태로 변환하기
diary_back = json.loads(diary_s)
print(diary_back)
print(type(diary_back))


