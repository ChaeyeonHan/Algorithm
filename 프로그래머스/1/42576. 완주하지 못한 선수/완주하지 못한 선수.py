# 해시 : 이름을 키로 사용, 동명이인의 수를 값
def solution(participant, completion):
    d={}  # 빈사전
    for i in participant:
        d[i] = d.get(i, 0) + 1  # 주어진 키 i가 존재하면 그 값을, 없으면 0(디폴트값)을
        # 처음 등장하면 0+1, 동명이인이라면 기존인원수+1

    for j in completion:
        d[j] -= 1  # 이름 한명씩 빼주기
    result = [k for k, v in d.items() if v>0]  # value가 1인 선수 찾기
    answer = result[0]
    print(result)
    print(answer)
    return answer