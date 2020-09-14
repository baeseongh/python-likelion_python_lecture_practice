t = int(input("팀원 수 : "))

#리스트 생성
team = []

for i in range(1, t+1): 
    m_num = input(str(i)+"번 팀원의 학번과 이름을 입력해 주세요 : ")
    team.append(m_num)

team.sort(reverse=True)

# for문 을 통한 리스트 출력
for result in team:
    print(result)