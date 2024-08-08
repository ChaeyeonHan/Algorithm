def solution(name):
    total = 0
    for idx, alpha in enumerate(name):
        total += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]) + 1)

    # 문자 이동
    move = len(name)-1
    for left in range(len(name)):
        idx = left+1
        while idx < len(name) and name[idx] == 'A':
            idx += 1
        right = len(name)-idx
        # right가 더 작으면, 끝에서 왼쪽방향으로 먼저 이동하고, 나머지는 오른쪽으로 이동
        # left가 더 작으면, 시작지점에서 오른쪽방향으로 먼저 이동하고, 나머지는 왼쪽방향으로 이동
        back_distance = min(left, right)

        # 오른쪽으로만 이동(최악. N-1)/왼쪽으로 되돌아와서 이동
        move = min(move, left+right+back_distance)
    
    total += move
    return total