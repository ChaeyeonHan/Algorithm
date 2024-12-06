from collections import defaultdict

def solution(friends, gifts):
    n = len(friends)
    table = [[0]* n for _ in range(n)]
    nums = [0] * n
    
    # friends 이름 순서대로 딕셔너리에 저장
    friend_dict = dict()
    for i in range(n):
        friend_dict[friends[i]] = i  #(이름, idx)
    for gift in gifts:
        a, b = gift.split(' ')  # 준 사람, 받은 사람
        idx1, idx2 = friend_dict[a], friend_dict[b]
        table[idx1][idx2] += 1
        nums[idx1] += 1  # 선물지수 업데이트
        nums[idx2] -= 1
    
    next_gift = defaultdict(int)
    for friend in range(n):
        for other in range(n):
            if friend != other and table[friend][other] > table[other][friend]:
                next_gift[friend] += 1
            elif friend != other and table[friend][other] == table[other][friend]:
                if nums[friend] > nums[other]:
                    next_gift[friend] += 1
    return max(next_gift.values(), default=0)