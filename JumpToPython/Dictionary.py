# 딕셔너리(Dictionary)
dic = {'name':'pey', 'phone':'01012341234', 'birth':'1111'} # {key1:value1, key2:value2, key3:value3} Key : Value 형태로 구성되며 쉼표(,)로 구분 한다.
## - Key에는 변하지 않는값을 사용하고 Value에는 변하는 값, 변하지 않는 값 모두 사용할 수 있다.
a = {1:'hi'}
a = {1:[1,2,3]} # Value로 리스트


# 딕셔너리 쌍 추가, 삭제
## 1. 딕셔너리 쌍 추가
a = {1:'a'}
a[2] = 'b' # {2:b} 쌍 추가
a['name'] = 'pey' # {'name':'pey'} 쌍 추가
a['list'] = [1,2,3] # {'list':[1,2,3]} 쌍 추가

## 2. 딕셔너리 요소 삭제
del a[1] # Key가 1인 key:value 삭
del a['list'] # Key가 'list'인 key:value 삭제


# 딕셔너리 사용 방법
## 딕셔너리 Key 사용해 Value 얻기
grade = {'pey':10, 'julliet':99}
grade['pey'] # Key가 'pey'인 딕셔너리의 Value를 반환
grade['julliet'] # Key가 'julliet'인 딕셔너리의 Value를 반환
a = {1:'a', 2:'b'}
a[1] # Key가 1인 딕셔너리의 Value를 반환,
a[2] # Key가 2인 딕셔너리의 Value를 반환
### - 딕셔너리 변수에서 [] 안의 숫자 1은 두 번째 요소를 의미하는 것이 아니라, Key에 해당하는 1을 나타낸다.
### - 따라서 딕셔너리는 리스트와 튜플에 있는 인덱싱 방법을 사용할 수 없다.)
dic = {'key':'value', 'key2':'value2', 'key3':'value3'}
dic['key'] # dic[key] = value, Key에 해당하는 Value를 얻는다.

## 딕셔너리를 만들때 주의사항
### 1. Key는 고유 값이다.
a = {1:'a', 1:'b'} # 1이라는 Key 값이 중복으로 사용
a # {1: 'b'} 1:'a' 쌍이 무시됨
### 2. Key로 리스트를 쓸 수 없다.
a = {[1,2]:'hi'} # TypeError (리스트는 변하는 값이기 때문에)
### 3. Key로 튜플을 쓸 수 있다.
a = {(1,2):'hi'} # 튜플은 변하지 않는 값이기 때문에
a[(1,2)] # a[1,2]


# 딕셔너리 관련 함수
a = {'name':'pey', 'phone':'01012341234', 'birth':'1111'}

## Key 리스트 만들기(keys)
a.keys() # dict_keys 객체 반환
### 1. keys 활용
for k in a.keys():
    print(k)
### 2. dict_keys 객체를 리스트로 반환
list(a.keys())

## Value 리스트 만들기(values)
a.values() # dict_values 객체 반환
### 1. values 활용
for v in a.values():
    print(v)
### 2. dict_values 객체를 리스트로 반환
list(a.values())

## Key, Value 쌍 얻기(items)
a.items() # dict_items 객체 반환 (Key와 Value를 튜플로 묶은 리스트)
list(a.items()) # dict_items 객체를 리스트로 반환

## Key, Value 쌍 모두 지우기(clear)
a.clear() # 빈 딕셔너리 {} 반환

## Key로 Value 얻기(get)
a = {'name':'pey', 'phone':'01012341234', 'birth':'1111'}
a.get('name') # a['name'] 과 동일
a.get('nokey') # 존재하지 않은 Key를 가져오려고 할 경우 None을 반환 한다. 반면 'a['nokey']' 의 경우 오류 반환
### Key 값이 없을경우 디폴트 값 반환
a.get('nokey', 'default') # default 반환

## 해당 Key가 딕셔너리 안에 있는지 조사(in)
'name' in a # 'key in obj' 가 참인 경우 True 반환
'email' in a # 'key in obj' 가 거인 경우 False 반환짓

## 예제) 딕셔너리 만들기
exam = {'name':'홍길동', 'brith':1128, 'age':30}